import cv2
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal, pyqtSlot, Qt)

def update_frame(cFrame_list,gui,side, width_resize,height_resize):
    # cv2.cvtColor(self.modFrame, cv2.COLOR_RGB2BGR, self.modFrame)
    cnt=0
    for cFrame in cFrame_list:
        cnt+=1
        # Get the original image        
        frame_size = (int(width_resize), int(height_resize))

        resized_frame = cv2.resize(cFrame.frame, frame_size)

        cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB, resized_frame)   
        bytesPerLine = 3 * width_resize
        QImg = QImage(resized_frame.data, width_resize, height_resize, bytesPerLine,QtGui.QImage.Format.Format_RGB888
    )
        cFrame.frame=resized_frame
        pixmap = QPixmap.fromImage(QImg)
        if side==0:
            gui.initFrame_label.setPixmap(pixmap)
        elif side==1:
            gui.initFrame2_label.setPixmap(pixmap)

def update_frame_raw(frameList,gui,side):

    cnt=0
    for frame  in frameList:
        if cnt%10!=0:
            continue
        cnt+=1
        # Get the original image 
        width_resize = 400
        height_resize = 300  
        frame_size = (int(width_resize), int(height_resize))

        resized_frame = cv2.resize(frame, frame_size)

        cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB, resized_frame)   
        bytesPerLine = 3 * width_resize
        QImg = QImage(resized_frame.data, width_resize, height_resize, bytesPerLine,QtGui.QImage.Format.Format_RGB888
    )
        frame=resized_frame
        pixmap = QPixmap.fromImage(QImg)
        if side==0:
            gui.initFrame_label.setPixmap(pixmap)
        elif side==1:
            gui.initFrame2_label.setPixmap(pixmap)




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


def plot_results(result,frame):
 
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
            

def substraction(frame,side):
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