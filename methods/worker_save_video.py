from methods import visualization
import cv2
import time



def save_video(stop_event,ui,MainWindow,side,q):

    # 🎥 Configurar el guardado del video
    output_file = "/home/aitech/GIT/videos/match/output_"+side+".avi"
    fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Codec eficiente (prueba también "MJPG")
    
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

def save_video_processed(stop_event,ui,MainWindow,side,q):

    # 🎥 Configurar el guardado del video
    output_file = MainWindow.params["folder_name"]+"/output_"+side+"_processed.avi"
    fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Codec eficiente (prueba también "MJPG")
    
    actual_height = int(MainWindow.params["cut_height"])
    actual_width = int(MainWindow.params["cut_width"])
    frame_size = (int(actual_width), int(actual_height))
    framerate=60

    out = cv2.VideoWriter(output_file, fourcc, framerate, frame_size)

    cnt=0
    while not stop_event.is_set(): 
        
        cFrame= q.get()
        # if q:
        #     cFrame = q.popleft()  # Safe pop
        # else:
        #     time.sleep(0.016)
        #     continue

        if MainWindow.params["visualise"]==1:
            visualization.update_frame(cFrame.results,ui,cFrame.side)

        if MainWindow.params["record"]==1:
            for result in cFrame.results:
                out.write(result.orig_img)

        cnt+=1
            # for frame in cFrame.frameList:
            #     cnt+=1
            #     out.write(frame)

        if cnt%100==0:
            # print("cnt : ", cnt)
            print("qsave.qsize(): ",q.qsize())