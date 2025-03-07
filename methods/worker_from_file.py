from methods import frame_class
from methods import visualization
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



def worker(stop_event,ui,MainWindow,side,q):
    HOME = os.getcwd()
    # local_model = YOLO(f'{HOME}/models/best.pt') 
    local_model = YOLO(f'{HOME}/models/best.engine') 

    videoSource = MainWindow.params["folder_name"]+"/output_"+side+".avi"

    cap = cv2.VideoCapture(videoSource)
    framerate=60

    # Verificar si se aplicó correctamente
    actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    actual_fps = cap.get(cv2.CAP_PROP_FPS)
    actual_format = cap.get(cv2.CAP_PROP_FOURCC)

    print(f"Resolución: {actual_width}x{actual_height}")
    print(f"FPS: {actual_fps}")
    print(f"Formato: {actual_format}")

    # 🎥 Configurar el guardado del video
    output_file = MainWindow.params["folder_name"]+"/output_"+side+"_processed.avi"
    
    fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Codec eficiente (prueba también "MJPG")
    # out = cv2.VideoWriter(output_file, fourcc, 120, (1024, 768))
    # [448,384]
    frame_size = (int(actual_width), int(actual_height))

    # out = cv2.VideoWriter(output_file, fourcc, framerate, frame_size)
    out2 = cv2.VideoWriter(output_file, fourcc, framerate, frame_size)


    ### VARIABLES
    init=time.time()
    cnt=0
    cntf=-1
    background_subs=0

    if background_subs==1:

        # Read the first frame
        ret, prev_frame = cap.read()
        prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        # prev_frame=prev_frame[height1:height2,width1:width2]


    batch_size=4
    cFrame = frame_class.Frame()
    cFrame.height=actual_height
    cFrame.width=actual_width
    cFrame.side=side
    cnt_jump=0
    while not stop_event.is_set(): 

        ret, frame = cap.read()
        if not ret:
            print("No se pudo capturar el cuadro")
            break

        cnt_jump+=1
        time.sleep(0.012)

        if cnt_jump%4==0:
            continue

        if MainWindow.params["start_file"]==0:
            break

        cnt+=1
        if cnt%(framerate*5)==0:
            diff=time.time()-init
            print("time after 5 sec: ",time.time()-init, ", cnt : ", cnt)

            init=time.time()

        if background_subs==1:
            visualization.substracion(frame,side)

        if MainWindow.params["plot"]==1:
            # results = local_model.predict(source=frame, conf=0.3, iou=0.4,imgsz=[actual_height,actual_width],verbose=False,device=0,half=True)
            # plot_results(results,frame)
            
            #### ADD FRAME TO BATCH
            cntf+=1
            if cntf==0:
                cFrame.frameList=[]
                cFrame.timeStampList=[]

            cFrame.frameList.append(frame)
            cFrame.timeStampList.append(time.time())

            ### SEND BATCH AND RESET CNT
            if len(cFrame.frameList)==batch_size:
                q.put(cFrame)
                cntf=-1

        if MainWindow.params["record"]==1:
            out2.write(frame)

        if 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
