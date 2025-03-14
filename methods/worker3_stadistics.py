from methods import frame_class
from methods import synchronization as syn
import os
import cv2
import torch
from methods import visualization
from methods import stadistics as stad
from ultralytics import YOLO


def worker(stop_event,ui,MainWindow,q3,perm_team,q_saveL,q_saveR,params,model):

    cnt=0

    buffer = syn.buffer_data()
    while True:
        if stop_event.is_set():
            break
        cFrame=[]
        cFrame=q3.get()
        if len(cFrame.results)==0:
            return
        
        cnt+=1
        if cnt%100==0:
            print("q3.qsize(): ",q3.qsize())

        ### Syncronization
        buffer.add_data(cFrame)

        new_cFrame=frame_class.Frame()
        while (results_ts := buffer.data_Extraction()) is not None:
            
            stad.process(perm_team,results_ts,params,model)

        ### PLOT AND SAVE
        if cFrame.side== "L":
            # q_saveL.append(cFrame)
            q_saveL.put(cFrame)
            # perm_team.buffer_results_L.append(cFrame.results)

        if cFrame.side== "R":
            # q_saveR.append(cFrame)
            q_saveR.put(cFrame)
            # perm_team.buffer_results_R.append(cFrame.results)