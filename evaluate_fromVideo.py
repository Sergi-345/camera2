import cv2
import time
import os
from methods import person_detection
from ultralytics import YOLO



videoSource="/home/aitech/GIT/videos/output_120fps.avi"
cap = cv2.VideoCapture(videoSource)

if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()
# Verificar si se aplicó correctamente
actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
actual_fps = cap.get(cv2.CAP_PROP_FPS)
actual_format = cap.get(cv2.CAP_PROP_FOURCC)

print(f"Resolución: {actual_width}x{actual_height}")
print(f"FPS: {actual_fps}")
print(f"Formato: {actual_format}")

# 🎥 Configurar el guardado del video
output_file = "/home/aitech/GIT/videos/output_120fps_2.avi"
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Codec eficiente (prueba también "MJPG")
# out = cv2.VideoWriter(output_file, fourcc, 120, (1024, 768))
# [448,384]
out = cv2.VideoWriter(output_file, fourcc, 15, (448,384))


# Convert Video to 30 fps from terminal:

fps = 120  # FPS objetivo
frame_size = (int(actual_width), int(actual_height))

out = cv2.VideoWriter(output_file, fourcc, fps, frame_size)
cnt=0
init=time.time()

HOME = os.getcwd()
# local_model = person_detection.GPUYOLO(f'{HOME}/original_608_928/from_yolo8n/best.engine')
local_model = YOLO(f'{HOME}/original_608_928/from_yolo8n/best.engine') 
plot=1
cnt=0
points=[]
cnt_not_detected=0
text=""

while True:
    cnt+=1
    init2=time.time()
    ret, frame = cap.read()
    if not ret:
        print("No se pudo capturar el cuadro")
        break
    cnt+=1

    pred_init=time.time()
    detected=0

    # text=""
    red=(0, 0, 255)
    blue=(255, 0, 0)
    green=(0, 255, 0)
    color= blue
    if plot==1:
        height, width, channels = frame.shape
        results = local_model.predict(source=frame, conf=0.2, iou=0.4,imgsz=int(actual_width),verbose=False,device=0,half=True, int8=True)
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
                    detected=1
                    # Get bounding box coordinates
                    x1, y1, x2, y2 = map(int, box.xyxy[0])  # Convert to int
                    conf = float(box.conf[0])  # Confidence score
                    mid_point=[x1+int((x2-x1)/2),y1+int((y2-y1)/2)]

                    points.append(mid_point)
                    
                    # Draw bounding box and label
                    color = (0, 255, 0)  # Green for "ball"
                    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(img, f"{class_name} {conf:.2f}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        if len(points)>1:

            #### PRINT POINTS
            for i in range(len(points)-1):
                # print("points[i] : ", points[i])
                # print("points[i] : ", points[i+1])
                xInit=points[i][0]
                xEnd=points[i+1][0]
                yInit=points[i][1]
                yEnd=points[i+1][1]

                cv2.line(img, points[i], points[i+1], blue, thickness=2)

            #### DETECT GOOD OR BAD
            for i in range(len(points)-1):
                xInit=points[i][0]
                xEnd=points[i+1][0]
                yInit=points[i][1]
                yEnd=points[i+1][1]

                color=blue

                xDirection = ""
                yDirection = ""
                

                if  xInit - xEnd>0: ## Going To the wall
                    # cv2.line(img, points[i], points[i+1], blue, thickness=2)
                    xDirection = "toWall"

                if  xInit - xEnd<0: ## Coming Back from the wall
                    # cv2.line(img, points[i], points[i+1], red, thickness=2)
                    xDirection = "fromWall"

                if  yInit - yEnd>0: ## Going To the wall
                    # cv2.line(img, points[i], points[i+1], blue, thickness=2)
                    yDirection = "Up"

                if  yInit - yEnd<0: ## Coming Back from the wall
                    # cv2.line(img, points[i], points[i+1], red, thickness=2)
                    yDirection = "Down"
                
                if xDirection=="fromWall":
                    if yDirection=="Up":
                        text="good"
                        color=green
                        break
                    if yDirection=="Down":
                        text="bad"
                        color=red
                        break

    cv2.putText(img, text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

    if detected==1:          
        cnt_not_detected=0
    else:
        cnt_not_detected+=1

    if cnt_not_detected>=10:
        points=[]

    out.write(frame) # Guardar frame en el video

    cv2.imshow("Cámara ELP", frame)


    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # if 0xFF == ord('q'):
    #     break

cap.release()
cv2.destroyAllWindows()