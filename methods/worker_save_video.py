from methods import visualization
from methods import player_draw
from methods import ball_draw
from methods import racket_draw
from methods import serve_draw
import cv2
import time


def save_video(stop_event,ui,MainWindow,side,q):

    # 🎥 Configurar el guardado del video
    output_file = "/home/aitech/GIT/videos/match/output_"+side+".avi"
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
        side=0
    else:
        side=1
    
    while not stop_event.is_set(): 
        
        frameList = q.get()
        cnt_frames=0
        for frame in frameList:
            cnt+=1
            out.write(frame)
            cnt_frames+=1

        if cnt%100==0:
            # print("cnt : ", cnt)
            # print("qsave.qsize(): ",q.qsize())
            if side==0:
                MainWindow.qsaveL_size = str(q.qsize())
            if side==1:
                MainWindow.qsaveR_size = str(q.qsize())


def save_video_processed(stop_event,ui,MainWindow,params,side,q):

    # 🎥 Configurar el guardado del video
    output_file = MainWindow.params["folder_name"]+"/output_"+side+"_processed.avi"
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
    if side=="L":
        side=0
    else:
        side=1
    
    while not stop_event.is_set(): 
        
        cFrame= q.get()

        if MainWindow.params["visualise_processed"]==1:

            player_draw.draw_players_quadrant(cFrame,params)
            player_draw.draw_player(cFrame)
            ball_draw.draw_ball(cFrame)
            # racket_draw.draw_racket(cFrame)

            # serve_draw.draw_kick_start(cFrame)
            serve_draw.draw_reception_quadrant_and_player(cFrame,params,side)

            ball_draw.draw_ball_bounce_in_kick_start(cFrame)
            # ball_draw.draw_ball_bounce(perm_team,det_team.frame)

            visualization.update_frame(cFrame.results,ui,side, width_resize,height_resize)

        if MainWindow.params["record"]==1:
            for result in cFrame.results:
                out.write(result.orig_img)

        cnt+=1
        if cnt%20==0:
            if side==0:
                MainWindow.qsaveL_size = str(q.qsize())
            if side==1:
                MainWindow.qsaveR_size = str(q.qsize())
                # QTimer.singleShot(0, lambda: MainWindow.update_ui())
                # QMetaObject.invokeMethod(MainWindow, "update_ui", Qt.ConnectionType.QueuedConnection)


