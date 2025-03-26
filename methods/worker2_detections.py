from methods import frame_class
import os
import cv2
import torch
from methods import visualization
from methods import yolo_data
from ultralytics import YOLO





def worker(stop_event,ui,MainWindow,q1,q2,model,sideCh,params):

    if sideCh=="L":
        side=0
    else:
        side=1

    cnt=0
    while True:
        if stop_event.is_set():
            break
        frameList=[]
        frameList=q1.get()
        if len(frameList)==0:
            return
        cnt+=len(frameList)

        if cnt%200==0:
            if sideCh=="L":
                MainWindow.qdetL_size = str(q1.qsize())
            if sideCh=="R":
                MainWindow.qdetR_size = str(q1.qsize())

        results=[]
        height, width, _ = frameList[0].shape
        imgsz = [width,height]
        results = model.predict(source=frameList,batch=len(frameList), conf=0.2, iou=0.9,imgsz=imgsz,verbose=False,device=0,half=True)

        cframe_list=[]
        for n in range(len(frameList)):
            cFrame = frame_class.Frame()
            yolo_data.convertData(params,results[n],model,cFrame,side)

            if MainWindow.params["visualise_processed"]==1:
                cFrame.frame=frameList[n]

            cFrame.side=sideCh

            cframe_list.append(cFrame)


        q2.put(cframe_list)

