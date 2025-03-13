from methods import frame_class
import os
import cv2
import torch
from methods import visualization
from ultralytics import YOLO

from collections import deque
import queue as q


def worker(stop_event,ui,MainWindow,q3,perm_team,q_saveL,q_saveR):

    qL = deque(maxlen=100)
    qR = deque(maxlen=100)

    cnt=0
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

        if cFrame.side== "L":
            perm_team.buffer_results_L.append(cFrame.results)
            perm_team.time
        if cFrame.side== "R":
            perm_team.buffer_results_R.append(cFrame.results)



















        if cFrame.side== "L":
            # q_saveL.append(cFrame)
            q_saveL.put(cFrame)
            # perm_team.buffer_results_L.append(cFrame.results)

        if cFrame.side== "R":
            # q_saveR.append(cFrame)
            q_saveR.put(cFrame)
            # perm_team.buffer_results_R.append(cFrame.results)