import cv2
import numpy as np
import os


def save_frame(MainWindow,ui,side):
    # video_path, frame_num, result_path
    
    folder_src =MainWindow.params["folder_name"]
    video1= folder_src+"/output_"+side+".avi"

    cap = cv2.VideoCapture(video1)

    if not cap.isOpened():
        return

    folder_dst=MainWindow.params["folder_name"]+"/images"+side+"/"
    print("folder_dst : ", folder_dst)
    os.makedirs(os.path.dirname(folder_dst), exist_ok=True)

    videoSource=video1
    cap = cv2.VideoCapture(videoSource)

    cnt=0
    cnt2=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            cnt+=1

            if cnt%10==0:
                cnt2+=1
                cv2.imwrite(folder_dst+str(cnt)+".jpg", frame)
                cv2.imshow('frame',frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # if cnt2==200:
            #     break
        else:
            break

    # Release everything if job is finished
    cap.release()
    cv2.destroyAllWindows()