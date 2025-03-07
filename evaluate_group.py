import cv2
import time
import os
from methods import person_detection
import queue
import threading


#### CONFIGURATION:
# v4l2-ctl --set-fmt-video=width=1024,height=768,pixelformat=MJPG
# v4l2-ctl --set-parm=120

#### CHECK camera formats:
# v4l2-ctl --list-formats-ext

# # Cambia el índice si tienes más de una cámara conectada.
# #  WORKING BUT SLOWER
# cap = cv2.VideoCapture(0, cv2.CAP_V4L)


# Usa MJPEG si es compatible #### WORKING!!
pipeline = "v4l2src device=/dev/video0 ! image/jpeg, width=960, height=720, framerate=120/1 ! jpegdec ! videoconvert ! appsink" 
pipeline = "v4l2src device=/dev/video0 ! image/jpeg, width=1024, height=768, framerate=120/1 ! jpegdec ! videoconvert ! appsink" 
cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()
desired_fps=120

# # # # # SET RESOLUTION

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)
# # Forzar formato MJPEG (IMPORTANTE para lograr 120 FPS)
# cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

# # Intentar configurar FPS a desired_time
# cap.set(cv2.CAP_PROP_FPS, desired_fps)

# Verificar si se aplicó correctamente
actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
actual_fps = cap.get(cv2.CAP_PROP_FPS)
actual_format = cap.get(cv2.CAP_PROP_FOURCC)

print(f"Resolución: {actual_width}x{actual_height}")
print(f"FPS: {actual_fps}")
print(f"Formato: {actual_format}")

# 🎥 Configurar el guardado del video
output_file = "/home/aitech/GIT/videos/output_120fps.avi"
fourcc = cv2.VideoWriter_fourcc(*"H264")  # Codec eficiente (prueba también "MJPG")
out = cv2.VideoWriter(output_file, fourcc, 120, (1024, 768))


## XVID 9.4s cada 5s
## MJPG 17.61s cada 5s
# H264 9.8 cada 5s
## H265 5.9 cada 5s

# Convert Video to 30 fps from terminal:

fps = 120  # FPS objetivo
frame_size = (int(actual_width), int(actual_height))

out = cv2.VideoWriter(output_file, fourcc, fps, frame_size)
cnt=0
init=time.time()

## activate model
HOME = os.getcwd()
local_model = person_detection.GPUYOLO(f'{HOME}/original_608_928/from_yolo8n/best.pt')

#ACTIVATE QUEUES AND WORKERS
q1 = queue.Queue()

threading.Thread(target=worker1_predictions.worker1,  args=(q1,q2,perm_team), daemon=True).start()


while True:
    init2=time.time()
    ret, frame = cap.read()
    if not ret:
        print("No se pudo capturar el cuadro")
        break
    cnt+=1
    if cnt%(desired_fps*5)==0:
        print("time after 5 sec: ",time.time()-init, ", cnt : ", cnt)
        init=time.time()
    height1=209
    height2=657
    width1=375
    width2=759
    frame=frame[height1:height2,width1:width2]
    [454,378]
    results = local_model.predict(source=frame, conf=0.4, iou=0.4,imgsz=[448,384],verbose=False,device=0,half=False)
        
    # out.write(frame) # Guardar frame en el video

    # cv2.imshow("Cámara ELP", frame)

    if cnt==2400: ### 20 seconds
        break
    
    # if cnt==4800: ### 20 seconds
    #     break

    # Salir con 'q'
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

    if 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()