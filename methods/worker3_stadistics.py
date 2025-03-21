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


    batch_size=4
    while True:
        if stop_event.is_set():
            break
        cFrame=[]
        cFrame=q3.get()
        if len(cFrame.results)==0:
            return
        
        if cnt%100==0:

            MainWindow.qstad_size = str(q3.qsize())
            # QMetaObject.invokeMethod(MainWindow, "update_ui", Qt.ConnectionType.QueuedConnection)

        ### Syncronization
        buffer.add_data(cFrame)


        new_cFrame_L=frame_class.Frame()
        new_cFrame_R=frame_class.Frame()
        
        while (results_ts := buffer.data_Extraction()) is not None:
            stad.process(perm_team,results_ts,params,model,cnt)
            cnt+=1
            
            if MainWindow.params["visualise_processed"]==1:
                new_cFrame_L.results.append(results_ts[0])
                new_cFrame_R.results.append(results_ts[1])

                detections2cFrame(perm_team,new_cFrame_R,new_cFrame_L)

        # Convert to list if needed

        if MainWindow.params["visualise_processed"]==1:
            convert2list(new_cFrame_L)
            convert2list(new_cFrame_R)
            q_saveL.put(new_cFrame_L)
            q_saveR.put(new_cFrame_R)

def convert2list(cFrame):
    cFrame.kick_init_list = cFrame.kick_init_list if isinstance(cFrame.kick_init_list, list) else [cFrame.kick_init_list]
    cFrame.reception_player_index_list = cFrame.reception_player_index_list if isinstance(cFrame.reception_player_index_list, list) else [cFrame.reception_player_index_list]
    cFrame.reception_player_id_list = cFrame.reception_player_id_list if isinstance(cFrame.reception_player_id_list, list) else [cFrame.reception_player_id_list]
    cFrame.reception_quadrant_ball_list = cFrame.reception_quadrant_ball_list if isinstance(cFrame.reception_quadrant_ball_list, list) else [cFrame.reception_quadrant_ball_list]
    cFrame.kick_side_list = cFrame.kick_side_list if isinstance(cFrame.kick_side_list, list) else [cFrame.kick_side_list]



def detections2cFrame(perm_team,new_cFrame_R,new_cFrame_L):
    ## ADD PLAYERS
    player_list_L=[]
    player_list_R=[]
    for player in perm_team.player_list:
        if player.side==0:
            player_list_L.append(player)
        else:
            player_list_R.append(player)
    new_cFrame_L.player_list.append(player_list_L)
    new_cFrame_R.player_list.append(player_list_R)

    ## ADD BALLS
    ball_list_L=[]
    ball_list_R=[]

    for ball in perm_team.ball_list:
        if ball.side==0:
            ball_list_L.append(ball)
        else:
            ball_list_R.append(ball)
    new_cFrame_L.ball_list.append(ball_list_L)
    new_cFrame_R.ball_list.append(ball_list_R)

    # ## ADD RACKETS
    # racket_list_L=[]
    # racket_list_R=[]
    # for racket in perm_team.racket_list:
    #     if racket.side==0:
    #         racket_list_L.append(racket)
    #     else:
    #         racket_list_R.append(racket)
    # new_cFrame_L.racket_list.append(racket_list_L)
    # new_cFrame_R.racket_list.append(racket_list_R)

    ## ADD DATA
    new_cFrame_L.kick_init_list.append(perm_team.kick_init)
    new_cFrame_R.kick_init_list.append(perm_team.kick_init)

    new_cFrame_L.reception_player_index_list.append(perm_team.reception_player_index)
    new_cFrame_R.reception_player_index_list.append(perm_team.reception_player_index)

    new_cFrame_L.reception_player_id_list.append(perm_team.reception_player_id)
    new_cFrame_R.reception_player_id_list.append(perm_team.reception_player_id)

    new_cFrame_L.reception_quadrant_ball_list.append(perm_team.reception_quadrant_ball)
    new_cFrame_R.reception_quadrant_ball_list.append(perm_team.reception_quadrant_ball)

    new_cFrame_L.kick_side_list.append(perm_team.kick_side)
    new_cFrame_R.kick_side_list.append(perm_team.kick_side)

    ball_list_L=[]
    ball_list_R=[]
    for ball in perm_team.ballBounceAfterKick_list:
        if ball.side==0:
            ball_list_L.append(ball)
        else:
            ball_list_R.append(ball)
    new_cFrame_L.ballBounceAfterKick_list.append(ball_list_L)
    new_cFrame_R.ballBounceAfterKick_list.append(ball_list_R)
