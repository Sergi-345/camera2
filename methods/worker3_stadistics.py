from methods import frame_class
from methods import synchronization as syn
from methods import visualization
from methods import stadistics as stad
import os
import cv2
import copy
from PyQt6.QtCore import QMetaObject, Qt


def worker(stop_event,ui,MainWindow,q3,perm_team,q_saveL,q_saveR,params,model):

    cnt=0

    buffer = syn.buffer_data()

    while True:
        if stop_event.is_set():
            break
        cFrame_list=[]
        cFrame_list=q3.get()
        
        if cnt%100==0:
            MainWindow.qstad_size = str(q3.qsize())
            # QMetaObject.invokeMethod(MainWindow, "update_ui", Qt.ConnectionType.QueuedConnection)

        ### Syncronization
        buffer.add_data(cFrame_list)

        cFrame_list_L=[]
        cFrame_list_R=[]

        
        while (cFrame_list2 := buffer.data_Extraction()) is not None:
            stad.process(perm_team,cFrame_list2,params,cnt)
            cnt+=1
            
            if MainWindow.params["visualise_processed"]==1:

                detections2cFrame(perm_team,cFrame_list2[0],cFrame_list2[1])
                
                cFrame_list_L.append(cFrame_list2[0])
                cFrame_list_R.append(cFrame_list2[1])

        # Convert to list if needed
        if MainWindow.params["visualise_processed"]==1:
            q_saveL.put(cFrame_list_L)
            q_saveR.put(cFrame_list_R)



def detections2cFrame(perm_team,cFrame_L,cFrame_R):

    cFrame_R.player_list=[]
    cFrame_L.player_list=[]
    for player in perm_team.player_list:
        if player.side==0:
            cFrame_L.player_list.append(player)
        if player.side==1:
            cFrame_R.player_list.append(player)

    cFrame_R.ball_list=[]
    cFrame_L.ball_list=[]
    for ball in perm_team.ball_list:
        if ball.side==0:
            cFrame_L.ball_list.append(ball)
        if ball.side==1:
            cFrame_R.ball_list.append(ball)

    ## ADD DATA
    cFrame_L.kick_init=perm_team.kick_init
    cFrame_R.kick_init=perm_team.kick_init

    cFrame_L.reception_player_index = perm_team.reception_player_index
    cFrame_R.reception_player_index = perm_team.reception_player_index

    cFrame_L.reception_player_id = perm_team.reception_player_id
    cFrame_R.reception_player_id = perm_team.reception_player_id

    cFrame_L.reception_quadrant_ball = perm_team.reception_quadrant_ball
    cFrame_R.reception_quadrant_ball = perm_team.reception_quadrant_ball

    cFrame_L.kick_side = perm_team.kick_side
    cFrame_R.kick_side = perm_team.kick_side

    ball_list_L=[]
    ball_list_R=[]
    for ball in perm_team.ballBounceAfterKick_list:
        if ball.side==0:
            ball_list_L.append(ball)
        else:
            ball_list_R.append(ball)

    cFrame_L.ballBounceAfterKick_list = ball_list_L
    cFrame_R.ballBounceAfterKick_list = ball_list_R
    ## Assert list
    cFrame_L.ballBounceAfterKick_list = cFrame_L.ballBounceAfterKick_list if isinstance(cFrame_L.ballBounceAfterKick_list, list) else [cFrame_L.ballBounceAfterKick_list]
    cFrame_R.ballBounceAfterKick_list = cFrame_R.ballBounceAfterKick_list if isinstance(cFrame_R.ballBounceAfterKick_list, list) else [cFrame_R.ballBounceAfterKick_list]

