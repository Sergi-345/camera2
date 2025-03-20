from methods import visualization
from methods import player_draw
import cv2
import time
from PyQt6.QtCore import QThread, QTimer
from PyQt6.QtCore import QMetaObject, Qt



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
    while not stop_event.is_set(): 
        
        frameList = q.get()
        top_frames= len(frameList)-3
        cnt_frames=0
        for frame in frameList:
            cnt+=1
            out.write(frame)
            cnt_frames+=1

        if cnt%100==0:
            # print("cnt : ", cnt)
            print("qsave.qsize(): ",q.qsize())


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
    while not stop_event.is_set(): 
        
        cFrame= q.get()

        if MainWindow.params["visualise"]==1:

            player_draw.draw_players_quadrant(cFrame,params)

            visualization.update_frame(cFrame.results,ui,side)

        if MainWindow.params["record"]==1:
            for result in cFrame.results:
                resized_frame = cv2.resize(result.orig_img, frame_size)
                out.write(resized_frame)

        cnt+=1
        if cnt%10==0:
            if side=="L":
                MainWindow.qsaveL_size = str(q.qsize())
            if side=="R":
                MainWindow.qsaveR_size = str(q.qsize())
                # QTimer.singleShot(0, lambda: MainWindow.update_ui())
                QMetaObject.invokeMethod(MainWindow, "update_ui", Qt.ConnectionType.QueuedConnection)


