from methods import visualization
from methods import player_draw
from methods import ball_draw
from methods import racket_draw
from methods import serve_draw
import cv2
import time
import os


def save_video(stop_event,ui,MainWindow,side,q):

    # 🎥 Configurar el guardado del video

    exp_name = ui.exp_name_textEdit.toPlainText()

    path = "/home/aitech/GIT/videos/match/"+exp_name

    if not os.path.exists(path):
        os.makedirs(path)
    
    output_file = path+"/output0_"+side+".avi"
    print("output_file : ", output_file)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Codec eficiente (prueba también "MJPG")
    ## XVID 9.4s cada 5s
    ## MJPG 17.61s cada 5s
    # H264 9.8 cada 5s
    ## H265 5.9 cada 5s
    
    actual_height = int(MainWindow.params["cut_height"])
    actual_width = int(MainWindow.params["cut_width"])
    frame_size = (int(actual_width), int(actual_height))
    framerate=60

    out = cv2.VideoWriter(output_file, fourcc, framerate, frame_size)

    cnt=0

    if side=="L":
        sideCh="L"
        side=0
    else:
        side=1
        sideCh="R"
    
    cnt_batch=0
    cnt_video=0

    while not stop_event.is_set(): 
        
        cnt+=1

        cnt_batch+= MainWindow.params["batch_size"]

        frameList = q.get()

        if MainWindow.params["record"]==1:
            for frame in frameList:
                out.write(frame)

        if MainWindow.params["visualise_raw"]==1:
                visualization.update_frame_raw(frameList,ui,side)

        if cnt%20==0:
            if side==0:
                MainWindow.qsaveL_size = str(q.qsize())
            if side==1:
                MainWindow.qsaveR_size = str(q.qsize())

        ## Create new video
        if cnt_batch==MainWindow.params["video_size"]: ## 18000 ->5 min
            cnt_batch=0
            cnt_video+=1 
            print("Changing to video ", cnt_video)
            out.release()

            output_file = path+"/output"+str(cnt_video)+"_"+sideCh+".avi"
            out = cv2.VideoWriter(output_file, fourcc, framerate, frame_size)


def save_video_processed(stop_event,ui,MainWindow,params,side,q):

    # 🎥 Configurar el guardado del video
    path=MainWindow.params["folder_name"]
    output_file = path+"/output0_"+side+"_processed.avi"
    fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Codec eficiente (prueba también "MJPG")
    
    actual_height = int(MainWindow.params["cut_height"])
    actual_width = int(MainWindow.params["cut_width"])
    frame_size = (int(actual_width), int(actual_height))
    framerate=60
    height_resize=400
    width_resize=500
    frame_size = (int(width_resize), int(height_resize))
    out = cv2.VideoWriter(output_file, fourcc, framerate, frame_size)

    cnt=0
    sideCh=side

    if side=="L":
        side=0
    else:
        side=1

    cnt_video=0
    cnt_batch=0
    
    while not stop_event.is_set(): 
        
        cFrame_list= q.get()

        cnt_batch+= len(cFrame_list)

        if MainWindow.params["visualise_processed"]==1:

            player_draw.draw_players_quadrant(cFrame_list,params)
            player_draw.draw_player(cFrame_list)
            ball_draw.draw_ball(cFrame_list)
            # racket_draw.draw_racket(cFrame)

            # serve_draw.draw_kick_start(cFrame)
            serve_draw.draw_reception_quadrant_and_player(cFrame_list,params,side)

            ball_draw.draw_ball_bounce_in_kick_start(cFrame_list)
            # ball_draw.draw_ball_bounce(perm_team,det_team.frame)

            visualization.update_frame(cFrame_list,ui,side, width_resize,height_resize)

        if MainWindow.params["record"]==1:
            for cframe in cFrame_list:
                out.write(cframe.frame)

            ## Create new video
            if cnt_batch>MainWindow.params["video_size"]: ## 18000 ->5 min
                cnt_batch=0
                cnt_video+=1 
                print("Changing to video ", cnt_video)
                out.release()

                output_file = path+"/output"+str(cnt_video)+"_"+sideCh+"_processed.avi"
                out = cv2.VideoWriter(output_file, fourcc, framerate, frame_size)

        cnt+=1
        if cnt%20==0:
            if side==0:
                MainWindow.qsaveL_size = str(q.qsize())
            if side==1:
                MainWindow.qsaveR_size = str(q.qsize())
                # QTimer.singleShot(0, lambda: MainWindow.update_ui())
                # QMetaObject.invokeMethod(MainWindow, "update_ui", Qt.ConnectionType.QueuedConnection)


