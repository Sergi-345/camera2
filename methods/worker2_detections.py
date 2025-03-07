import os
import cv2
from methods import visualization
from ultralytics import YOLO



def worker(stop_event,ui,MainWindow,q1):
    HOME = os.getcwd()
    # local_model = YOLO(f'{HOME}/models/best.pt') 
    local_model = YOLO(f'{HOME}/models/best.engine')

    cnt=0
    while True:
        if stop_event.is_set():
            break
        cFrame=[]
        cFrame=q1.get()
        if len(cFrame.frameList)==0:
            return
        cnt+=5
        if cnt%100==0:
            # print("cnt : ", cnt)
            print("q1.qsize() : ",q1.qsize())

        # RT Tensor
        # print("len(cFrame.frameList) : ",len(cFrame.frameList))
        results=[]
        results = local_model.predict(source=cFrame.frameList,batch=len(cFrame.frameList), conf=0.3, iou=0.8,imgsz=[cFrame.height,cFrame.width],verbose=False,device=0,half=True)

        # for result in results:
        #     # Get the original image
        #     orig_img = result.orig_img  # This is a NumPy array (OpenCV format)

        #     # Get bounding boxes and class indices
        #     boxes = result.boxes.xyxy  # (x1, y1, x2, y2) format
        #     class_ids = result.boxes.cls.int().tolist()  # Class indices as integers
        #     names = result.names  # Class names dictionary

        #     # Draw the bounding boxes on the image
        #     for i, box in enumerate(boxes):
        #         x1, y1, x2, y2 = map(int, box)  # Convert coordinates to integers
        #         label = names[class_ids[i]]  # Get class name
        #         color = (0, 255, 0)  # Green color for boxes

        #         # Draw rectangle
        #         cv2.rectangle(orig_img, (x1, y1), (x2, y2), color, 2)
        #         # Put label text
        #         cv2.putText(orig_img, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        
        # cFrame.results=result
        
        # frame=cFrame.frameList[0]
        # result=results[0]
        # print("----------------------------")
        # print("result : ", result)

        if MainWindow.params["visualise"]==1:
            # if q1.qsize()< 5:
            # visualization.plot_results(results,orig_img)
            visualization.update_frame(results,ui,cFrame.side)