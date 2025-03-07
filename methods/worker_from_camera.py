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



def update_frame(frame,gui,side):
    # cv2.cvtColor(self.modFrame, cv2.COLOR_RGB2BGR, self.modFrame)
    height, width, bytesPerComponent = frame.shape
    new_w, new_h = int(width), int(height)
    newFrame=frame
    newFrame=cv2.resize(newFrame, (new_w, new_h)) 
    bytesPerLine = 3 * new_w
    cv2.cvtColor(newFrame, cv2.COLOR_BGR2RGB, newFrame)   
    QImg = QImage(newFrame.data, new_w, new_h, bytesPerLine,QtGui.QImage.Format.Format_RGB888
)
    pixmap = QPixmap.fromImage(QImg)
    if side=="L":
        gui.initFrame2_label.setPixmap(pixmap)
    else:
        gui.initFrame_label.setPixmap(pixmap)

def update_frame2(frame, gui):
    # Ensure frame is resized properly
    height, width = frame.shape  # Since it's grayscale, only two values
    new_w, new_h = int(width), int(height)
    newFrame = cv2.resize(frame, (new_w, new_h))  

    # Convert grayscale image to QImage format
    bytesPerLine = new_w  # Since grayscale, bytesPerLine is width
    QImg = QImage(newFrame.data, new_w, new_h, bytesPerLine, QImage.Format.Format_Grayscale8)

    # Convert QImage to QPixmap and display in QLabel
    pixmap = QPixmap.fromImage(QImg)
    gui.initFrame2_label.setPixmap(pixmap)

def worker(stop_event,ui,MainWindow,side):
    HOME = os.getcwd()
    local_model = YOLO(f'{HOME}/from_yolo8n/best.engine') 


    # Usa MJPEG si es compatible #### WORKING!!
    framerate=60
    if side=="L":
        pipeline = "v4l2src device=/dev/video2 ! image/jpeg, width=1024, height=768, framerate={}/1 ! jpegdec ! videoconvert ! appsink".format(framerate) 
        cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

        if not cap.isOpened():
            print("AAAAAAAAAAAAAAAAAA No se pudo abrir la cámara ")
            pipeline = "v4l2src device=/dev/video3 ! image/jpeg, width=1024, height=768, framerate={}/1 ! jpegdec ! videoconvert ! appsink".format(framerate) 
            cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
            if not cap.isOpened():
                exit()
    else:
        pipeline = "v4l2src device=/dev/video0 ! image/jpeg, width=1024, height=768, framerate={}/1 ! jpegdec ! videoconvert ! appsink".format(framerate) 
        cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

    # Verificar si se aplicó correctamente
    actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    actual_fps = cap.get(cv2.CAP_PROP_FPS)
    actual_format = cap.get(cv2.CAP_PROP_FOURCC)

    print(f"Resolución: {actual_width}x{actual_height}")
    print(f"FPS: {actual_fps}")
    print(f"Formato: {actual_format}")

    # 🎥 Configurar el guardado del video
    output_file = "/home/aitech/GIT/videos/match/output_"+side+"_processed.avi"
    output_file2 = "/home/aitech/GIT/videos/match/output_"+side+".avi"
    
    fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Codec eficiente (prueba también "MJPG")
    # out = cv2.VideoWriter(output_file, fourcc, 120, (1024, 768))
    # [448,384]
    frame_size = (int(actual_width), int(actual_height))

    width = 1024
    height = 768

    # out = cv2.VideoWriter(output_file, fourcc, framerate, frame_size)
    out2 = cv2.VideoWriter(output_file2, fourcc, framerate, frame_size)

    ## XVID 9.4s cada 5s
    ## MJPG 17.61s cada 5s
    # H264 9.8 cada 5s
    ## H265 5.9 cada 5s

    cnt=0
    init=time.time()

    # local_model = YOLO(f'{HOME}/from_yolo8n/best.pt') 
    points=[]

    ### VARIABLES
    cnt=0
    points=[]
    cnt_not_detected=0
    text=""

    background_subs=0

    if background_subs==1:

        # Read the first frame
        ret, prev_frame = cap.read()
        prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        # prev_frame=prev_frame[height1:height2,width1:width2]


    while not stop_event.is_set(): 

        if MainWindow.params["start"]==0:
            time.sleep(1)
            break

        ret, frame = cap.read()
        if not ret:
            print("No se pudo capturar el cuadro")
            break

        cnt+=1
        if cnt%(framerate*5)==0:
            print("time after 5 sec: ",time.time()-init, ", cnt : ", cnt)
            init=time.time()

        red=(0, 0, 255)
        blue=(255, 0, 0)
        green=(0, 255, 0)
        color= blue

        if background_subs==1:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Compute absolute difference between current and previous frame
            diff_frame = cv2.absdiff(gray_frame, prev_frame)

            # Apply thresholding to highlight the differences
            _, thresh_frame = cv2.threshold(diff_frame, 25, 255, cv2.THRESH_BINARY)

            if side=="L":
                cv2.imshow("thresh_frameL",thresh_frame )
            else:
                cv2.imshow("thresh_frameR",thresh_frame )
            # Update previous frame
            prev_frame = gray_frame


        if MainWindow.params["plot"]==1:
            # results = local_model.predict(task="detect",source=frame, conf=0.3, iou=0.4,imgsz=width,verbose=False,device=0,half=False, int8=False)
            # results = local_model.predict(task="detect",source=frame, conf=0.3, iou=0.4,imgsz=[height,width],verbose=False,device=0,half=False)
            results = local_model.predict(task="detect", conf=0.3, iou=0.4,imgsz=[actual_height,actual_width],verbose=False,device=0,half=True)
            plot_results(results,frame)

        if MainWindow.params["record"]==1:
            out2.write(frame)

        if MainWindow.params["visualise"]==1:
            update_frame(frame,ui,side)

        if 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def plot_results(results,frame):
    for result in results:
            
        boxes = result.boxes  # Bounding boxes
        names = result.names  # Class names dictionary

        for box in boxes:
            class_id = int(box.cls)  # Get class ID
            class_name = names[class_id]  # Get class name

            # if class_name == "ball" or class_name == "ball_s-d8v6" or class_name == "ball_r":  # Filter only "ball"
            # Get bounding box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Convert to int
            conf = float(box.conf[0])  # Confidence score
            mid_point=[x1+int((x2-x1)/2),y1+int((y2-y1)/2)]
            
            # Draw bounding box and label
            color = (0, 255, 0)  # Green for "ball"
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{class_name} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)