import queue
import cv2
import time
import os
from methods import tools
from methods import frame_class
from ultralytics import YOLO
import numpy as np
from collections import deque
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal, pyqtSlot, Qt)
from PyQt6.QtCore import QMetaObject, Qt



# def update_frame(frame,gui,side):
#     # cv2.cvtColor(self.modFrame, cv2.COLOR_RGB2BGR, self.modFrame)
#     height, width, bytesPerComponent = frame.shape

#     qimage_height = 600
#     aspect_ratio = width / height
#     qimage_width = int(qimage_height * aspect_ratio)

#     resized_frame = cv2.resize(frame, (qimage_width, qimage_height))

#     cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB, resized_frame)   
#     bytesPerLine = 3 * qimage_width
#     QImg = QImage(resized_frame.data, qimage_width, qimage_height, bytesPerLine,QtGui.QImage.Format.Format_RGB888
# )
#     pixmap = QPixmap.fromImage(QImg)
#     if side=="L":
#         gui.initFrame2_label.setPixmap(pixmap)
#         # cv2.imshow("left",frame)
#     else:
#         gui.initFrame_label.setPixmap(pixmap)
#         # cv2.imshow("right",frame)


def worker(stop_event,ui,MainWindow,side,q_save,q_detect):

    # Usa MJPEG si es compatible #### WORKING!!
    framerate=60
    width = int(MainWindow.params["width"])
    height= int(MainWindow.params["height"])
    if side=="L":
        pipeline = f"v4l2src device=/dev/video2 ! image/jpeg, framerate={framerate}/1 ! jpegdec ! videoconvert ! videoscale ! video/x-raw, width={width}, height={height} ! appsink"


        cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

        if not cap.isOpened():
            pipeline = f"v4l2src device=/dev/video3 ! image/jpeg, framerate={framerate}/1 ! jpegdec ! videoconvert ! videoscale ! video/x-raw, width={width}, height={height} ! appsink"
        #     # pipeline = "v4l2src device=/dev/video3 ! image/jpeg, width={width}, height={height}}, framerate={framerate}/1 ! jpegdec ! videoconvert ! appsink"
        #     cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
            if not cap.isOpened():
                exit()
    else:
        pipeline = f"v4l2src device=/dev/video0 ! image/jpeg, framerate={framerate}/1 ! jpegdec ! videoconvert ! videoscale ! video/x-raw, width={width}, height={height} ! appsink"
        # pipeline = "v4l2src device=/dev/video0 ! image/jpeg, width={width}, height={height}}, framerate={framerate}/1 ! jpegdec ! videoconvert ! appsink"
        cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

    # Verificar si se aplicó correctamente
    actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    actual_fps = cap.get(cv2.CAP_PROP_FPS)
    actual_format = cap.get(cv2.CAP_PROP_FOURCC)

    print(f"Resolución: {actual_width}x{actual_height}")
    print(f"FPS: {actual_fps}")
    print(f"Formato: {actual_format}")

    init=time.time()

    ### VARIABLES
    cnt=0

    batch_size=4
    frameList=[]
    cntf=-1
    cnt_jump=0

    cut_width=MainWindow.params["cut_width"]
    cut_height=MainWindow.params["cut_height"]

    cFrame = frame_class.Frame()
    cFrame.height=cut_height
    cFrame.width=cut_width
    cFrame.side=side

    while not stop_event.is_set(): 

        if MainWindow.params["start"]==0:
            time.sleep(1)
            break

        ret, frame = cap.read()
        if not ret:
            print("No se pudo capturar el cuadro")
            break

        if side=="L":
            MainWindow.start_vect[0]=1
        else:
            MainWindow.start_vect[1]=1

        if sum(MainWindow.start_vect[:])!=2:
            time.sleep(0.05)
            continue

        cnt_jump+=1

        # JUMPS
        if cnt_jump%MainWindow.params["jumps"]==0:
            continue

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

        ### Modify frame size
        frame = tools.cut_frame(frame,MainWindow,actual_height,actual_width)


        if MainWindow.params["plot"]==1:
            
            #### ADD FRAME TO BATCH
            cntf+=1
            if cntf==0:
                cFrame.frameList=[]
                cFrame.timeStampList=[]

            cFrame.frameList.append(frame)
            cFrame.timeStampList.append(time.time())

            ### SEND BATCH AND RESET CNT
            if len(cFrame.frameList)==batch_size:
                q_detect.put(cFrame)
                cntf=-1

        
        #### ADD FRAME TO BATCH
        cntf+=1
        if cntf==0:
            frameList=[]

        frameList.append(frame)

        ### SEND BATCH AND RESET CNT
        if len(frameList)==batch_size:
            q_save.put(frameList)
            
            cntf=-1



        if 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


