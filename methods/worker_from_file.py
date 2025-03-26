from methods import frame_class
from methods import visualization
from methods import tools
import queue
import cv2
import time
import os
from ultralytics import YOLO
import numpy as np
from collections import deque
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal, pyqtSlot, Qt)
from PyQt6.QtCore import QMetaObject, Qt


def worker(stop_event,ui,MainWindow,side,q):
    HOME = os.getcwd()
    # local_model = YOLO(f'{HOME}/models/best.pt') 
    # local_model = YOLO(f'{HOME}/models/best.engine') 

    videoSource = MainWindow.params["folder_name"]+"/output0_"+side+".avi"

    cap = cv2.VideoCapture(videoSource)
    framerate=60

    # Verificar si se aplicó correctamente
    actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    actual_fps = cap.get(cv2.CAP_PROP_FPS)
    actual_format = cap.get(cv2.CAP_PROP_FOURCC)

    MainWindow.curr_width = int(actual_width)
    MainWindow.curr_height = int(actual_height)

    print(f"Resolución: {actual_width}x{actual_height}")
    print(f"FPS: {actual_fps}")
    print(f"Formato: {actual_format}")

    ### VARIABLES
    init=time.time()
    cnt=0
    cntf=-1

    batch_size=4
    cFrame = frame_class.Frame()
    cFrame.height=actual_height
    cFrame.width=actual_width
    cFrame.side=side
    cnt_jump=0
    videoNumber=0

    while not stop_event.is_set(): 

        ret, frame = cap.read()
        if not ret:
            videoNumber+=1
            print("openning source video number ", videoNumber)
            videoSource = MainWindow.params["folder_name"]+"/output"+str(videoNumber)+"_"+side+".avi"
            cap = cv2.VideoCapture(videoSource)
            ret, frame = cap.read()
            if not ret:
                print("Video "+side+" finished")
                break

        if side=="L":
            MainWindow.start_vect[0]=1
        else:
            MainWindow.start_vect[1]=1

        if sum(MainWindow.start_vect[:])!=2:
            time.sleep(0.05)
            continue

        cnt_jump+=1
        time.sleep(MainWindow.params["time_sleep_processed"])

        if cnt_jump%MainWindow.params["jumps"]==0:
            time.sleep(0.011)
            continue

        if MainWindow.params["start_file"]==0:
            break

        ### Modify frame size
        frame = tools.cut_frame(frame,MainWindow,actual_height,actual_width)

        cnt+=1
        if cnt%(framerate*5)==0:
            diff=time.time()-init
            # print("time after 5 sec: ",time.time()-init, ", cnt : ", cnt)
            if side == "L":
                MainWindow.velL= str(diff)
                QMetaObject.invokeMethod(MainWindow, "update_ui", Qt.ConnectionType.QueuedConnection)
            if side == "R":
                MainWindow.velR= str(diff)

            init=time.time()

        if MainWindow.params["plot"]==1:
            
            #### ADD FRAME TO BATCH
            cntf+=1
            if cntf==0:
                frameList=[]


            frameList.append(frame)
            
            ### SEND BATCH AND RESET CNT
            if len(frameList)==batch_size:
                q.put(frameList)
                cntf=-1

        if 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
