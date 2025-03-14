import parameters
import os
import cv2
#from norfair import Detection, Tracker, Video, draw_tracked_objects
from PIL import Image
# from google.colab.patches import cv2_imshow
import numpy as np
np.bool = np.bool_
from methods import gameData
from methods import tracking
from methods import serve
from methods import team_class
from methods import player_stats
from methods import ball_stats
from methods import ball_draw
from methods import match_stats
from methods import yolo_data
from methods import coord_plot
from methods import tracking_draw
from methods import serve_draw
from methods import tracking_checks
from methods import match_checks
# from deep_sort_realtime.deepsort_tracker import DeepSort
import cv2
import torch

import time
import matplotlib.pyplot as plt
import queue
import threading
from ultralytics import YOLO
import torch
import redis
import json


def worker2(params,q2,q3,perm_team):

    HOME = os.getcwd()
    time_vect=[]

    # deepsort = DeepSort(max_age=100, nn_budget=2000,n_init=10,max_iou_distance=500,max_cosine_distance=0.9)
    if params.WriteProcessedVideo==1:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(params.videoOutput_processed, fourcc,params.fps, (params.frame_width,params.frame_height))
    cnt1=0
    cnt_hist=0
    cnt_w3=0
    cnt_plot=0  
    cnt_ball_detection =0      
    while True:
        det_team = q2.get()
        init=time.time()
        cnt1+=1
        if cnt1%100==0:
            print("q2.qsize() : ",q2.qsize())
            print("cnt q2 : ", cnt_hist)

        cnt=0
        cnt_results=0
        ball_detected_list=[]
        ball_detected_list2=[]
        det_team.ball_list=[]
        det_team.ball_list_fullRange=[]

        for result in det_team.results:

            
            det_team.frame=det_team.frameList[cnt]

            ball_detected_list=[]
            det_team.racket_list=[]
            cnt_hist+=1

            yolo_data.convertData(det_team, params,result,perm_team.local_model,ball_detected_list)
            cnt+=1

            if not tracking.start_tracking(perm_team, det_team, params):
                continue

            if not tracking_checks.check_minimum_detected_players(det_team,perm_team):
                continue
            cnt_w3+=1

            # ASSIGN PLAYERS
            tracking.tracking_management(params,det_team,perm_team,det_team.frame)
            tracking.ids_management(perm_team,params)
            match_stats.check_serveTeam(perm_team,params,cnt_w3)

            # match_stats.change_side(perm_team,det_team,params)
            player_stats.estimate_velocity(perm_team)
            serve.serve_detection(perm_team,params)
            serve.serve_cancel(perm_team,params,ball_detected_list)
            ball_stats.ball_bounce_detection(perm_team,ball_detected_list,params)
            tracking.stadistic_position_state(perm_team)


            if cnt_w3%30==0:
                player_stats.coordinates_vector(perm_team,params)
            # player_stats.stadistic_head_map(perm_team,params)
            if cnt_w3%30==0:
                player_stats.stadistic_km_done(perm_team,cnt_w3)

            if cnt_w3%30==0:
                match_checks.check_ball_size(perm_team)

            # Move data to permanent teams
            perm_team.racket_list=det_team.racket_list

            if cnt_w3%120==0:
                # Create data to send to worker 3
                if len(perm_team.player_list)>0:
                    frameData=gameData.FRAME_DATA()
                    for i in range(4):
                        
                        frameData.counter_in_defense[i] = perm_team.counter_in_defense[i]
                        frameData.counter_in_transition[i] = perm_team.counter_in_transition[i]
                        frameData.counter_in_attack[i] = perm_team.counter_in_attack[i]

                        frameData.coord_matrix[i]=perm_team.coord_matrix[i]

                        frameData.dist_acum_matrix[i] = perm_team.dist_acum_matrix[i]

                    frameData.player_list=[]
                    frameData.player_list= perm_team.player_list
                    frameData.racket_list=perm_team.racket_list
                    frameData.ball_list=perm_team.ballBounceAfterKick_list

                    # Send data to worker 3
                    q3.put(frameData)

            # SHOW VIDEO LIVE
            if params.drawAll==1:

                params.draw_detections(perm_team,det_team.frame)
                # params.draw_detected_ball(det_team.ball_list,det_team.frame)
                params.draw_detected_ball(ball_detected_list,det_team.frame)
                # params.draw_detected_shoes(shoes_detected_list,det_team.frame)
                # shoe_draw.draw_player_shoes(perm_team,det_team.frame)
                params.draw_players_position(perm_team,det_team.frame)
                # player_stats.draw_velocity(perm_team,det_team.frame)
                serve_draw.draw_kick_start(perm_team,det_team.frame,ball_detected_list)
                serve_draw.draw_reception_quadrant_and_player(perm_team,det_team.frame,params)
                ball_draw.draw_ball_bounce_in_kick_start(perm_team,det_team.frame)
                ball_draw.draw_ball_bounce(perm_team,det_team.frame)
                ball_draw.draw_ball_background(perm_team,det_team.frame)
                # match_draw.draw_playing_point(perm_team,det_team.frame)
                # player_stats.plot_velocity(perm_team,cnt_w3)

                if perm_team.match_line1!=[]:
                    tracking_draw.draw_matches(perm_team, det_team.frame)

                cv2.imshow("detection",det_team.frame)

                if params.drawRealWorldCoord==1 :
                    if cnt_w3%300==0: # Draw serve ball
                        #Plot player coordinates
                        coord_plot.plot_player_RWCoordinates(perm_team,params,perm_team.player_list,perm_team.ballBounceAfterKick_list)
                    # if cnt_w3%30==0: # plot player heat map
                    #     player_draw.plot_headMap(perm_team)
        
            # Record processed video
            if params.WriteProcessedVideo==1:
                if cnt==0:
                    out.write(det_team.frame)  # It takes long time
            cnt_results+=1

            time_vect.append(time.time()-init)
            
            if cnt_w3%30==0:
                av_time=sum(time_vect) / len(time_vect)
                percentage_time=av_time/(perm_team.batch_size*0.033)*100
                # print("% time w2: ", percentage_time)
                time_vect=[]

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    if params.WriteProcessedVideo==1:
        out.release()