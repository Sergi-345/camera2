from methods import frame_class
import os
import cv2
import torch
from methods import visualization
from ultralytics import YOLO



def worker(stop_event,ui,MainWindow,q1,q2,model):
    # HOME = os.getcwd()
    # # local_model = YOLO(f'{HOME}/models/best.pt').to("cuda")
    # local_model = YOLO(f'{HOME}/models/best.engine')

    width= MainWindow.params["cut_width"]
    height= MainWindow.params["cut_height"]
    cnt=0
    while True:
        if stop_event.is_set():
            break
        cFrame=[]
        cFrame=q1.get()
        if len(cFrame.frameList)==0:
            return
        cnt+=5
        if cnt%100==0:
            # print("cnt : ", cnt)
            print("q1.qsize() : ",q1.qsize())

        # RT Tensor
        # print("len(cFrame.frameList) : ",len(cFrame.frameList))
        results=[]


        height, width, _ = cFrame.frameList[0].shape

        imgsz = [width,height]

        results = model.predict(source=cFrame.frameList,batch=len(cFrame.frameList), conf=0.3, iou=0.8,imgsz=imgsz,verbose=False,device=0,half=True)

        new_cFrame = frame_class.Frame()
        new_cFrame.results=results
        new_cFrame.timeStampList=cFrame.timeStampList
        new_cFrame.side=cFrame.side
        new_cFrame.results = results

        q2.put(new_cFrame)

