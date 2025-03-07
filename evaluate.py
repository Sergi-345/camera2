import cv2
import time
import os
from methods import person_detection
from ultralytics import YOLO


#### CONFIGURATION:
# v4l2-ctl --set-fmt-video=width=1024,height=768,pixelformat=MJPG
# v4l2-ctl --set-parm=120

#### CHECK camera formats:
# v4l2-ctl --list-formats-ext

# # Cambia el índice si tienes más de una cámara conectada.
# #  WORKING BUT SLOWER
# cap = cv2.VideoCapture(0, cv2.CAP_V4L)


# Usa MJPEG si es compatible #### WORKING!!
framerate=120
pipeline = "v4l2src device=/dev/video0 ! image/jpeg, width=960, height=720, framerate=120/1 ! jpegdec ! videoconvert ! appsink" 
pipeline = "v4l2src device=/dev/video0 ! image/jpeg, width=1024, height=768, framerate={}/1 ! jpegdec ! videoconvert ! appsink".format(framerate) 
cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()

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
# out = cv2.VideoWriter(output_file, fourcc, 120, (1024, 768))
# [448,384]
frame_size = (int(actual_width), int(actual_height))

height1=273
height2=657
width1=375
width2=759
width = 384
height = 384

out = cv2.VideoWriter(output_file, fourcc, framerate, (width,height))

## XVID 9.4s cada 5s
## MJPG 17.61s cada 5s
# H264 9.8 cada 5s
## H265 5.9 cada 5s

# Convert Video to 30 fps from terminal:


# fps = 120  # FPS objetivo

cnt=0
init=time.time()

HOME = os.getcwd()
# local_model = person_detection.GPUYOLO(f'{HOME}/original_608_928/from_yolo8n/best.engine')
local_model = YOLO(f'{HOME}/original_608_928/from_yolo8n/best.engine') 
# local_model = YOLO(f'{HOME}/original_608_928/from_yolo8n/best.pt') 
# local_model = YOLO(f'{HOME}/original_608_928/from_yolo8n_support/best.engine') 
points=[]

plot=0

while True:
    init2=time.time()
    ret, frame = cap.read()
    if not ret:
        print("No se pudo capturar el cuadro")
        break
    cnt+=1
    if cnt%(framerate*5)==0:
        print("time after 5 sec: ",time.time()-init, ", cnt : ", cnt)
        init=time.time()
    detcted=0
    frame=frame[height1:height2,width1:width2]

    # height, width, channels = frame.shape
    # print("height : ",height)
    # print("width : ",width)

    img=frame
    
    # [454,378]
    pred_init=time.time()
    if plot==1:
        height, width, channels = frame.shape
        results = local_model.predict(source=frame, conf=0.01, iou=0.4,imgsz=width,verbose=False,device=0,half=True, int8=True)
        # Plot results
        img=frame
        for result in results:
            # img = result.plot()  # Draw bounding boxes

            boxes = result.boxes  # Bounding boxes
            names = result.names  # Class names dictionary

            for box in boxes:
                class_id = int(box.cls)  # Get class ID
                class_name = names[class_id]  # Get class name

                if class_name == "ball" or class_name == "ball_s-d8v6" or class_name == "ball_r":  # Filter only "ball"
                    cnt_no_detcted=0
                    # Get bounding box coordinates
                    x1, y1, x2, y2 = map(int, box.xyxy[0])  # Convert to int
                    conf = float(box.conf[0])  # Confidence score
                    mid_point=[(x2-x1)/2,(y2-y1)/2]
                    
                    # Draw bounding box and label
                    color = (0, 255, 0)  # Green for "ball"
                    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(img, f"{class_name} {conf:.2f}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                    
        # if cnt_no_detcted>=10:
        #     points=[]

        cv2.imshow("YOLO Video Detection", img)
    
    # print("prediction time : ", time.time()-pred_init)
    out.write(img) # Guardar frame en el video

    # cv2.imshow("Cámara ELP", frame)

    if cnt==2400: ### 20 seconds
        break
    
    # if cnt==4800: ### 20 seconds
    #     break

    # Salir con 'q'
    if plot==1:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()