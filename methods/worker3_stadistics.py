from methods import frame_class
import os
import cv2
import torch
from methods import visualization
from ultralytics import YOLO

from collections import deque




def worker(stop_event,ui,MainWindow,q3,perm_team):


    cnt=0
    while True:
        if stop_event.is_set():
            break
        cFrame=[]
        cFrame=q3.get()
        if len(cFrame.frameList)==0:
            return
        
        cnt+=1
        if cnt%100==0:
            # print("cnt : ", cnt)
            print("q3.qsize(): ",q3.qsize())

        if cFrame.side== "L":
            perm_team.buffer_results_L.append(cFrame.results)

        if cFrame.side== "R":
            perm_team.buffer_results_R.append(cFrame.results)


        

        # if MainWindow.params["visualise"]==1:
        #     # if q1.qsize()< 5:
        #     # visualization.plot_results(results,orig_img)
        #     visualization.update_frame(results,ui,cFrame.side)