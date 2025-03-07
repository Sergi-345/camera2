import cv2
import os


def find_unprocessed_avi_files(directory):
    avi_files = [f for f in os.listdir(directory) if f.endswith(".avi") and not f.endswith("_processed.avi")]
    return avi_files

# Example usage
def extract_frame(video_path, frame_number, output_image):
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    success, frame = cap.read()
    if success:
        cv2.imwrite(output_image, frame)
    cap.release()

def extract_img_from_video(folder,MainWindow):
    unprocessed_files = find_unprocessed_avi_files(folder)
    print("unprocessed_files : ", unprocessed_files)

    print("Unprocessed AVI files:")
    for file in unprocessed_files:
        print(file)
        video_path = os.path.join(folder, file)
        output_image = f"{os.path.splitext(file)[0]}_frame_100.jpg"
        filename=os.path.splitext(file)[0]
        output_image = folder+"/"+filename+"_frame_100.jpg"
        extract_frame(video_path, 100, output_image)
        print(f"Extracted frame 100 from {file} to {output_image}")

        print("contains_outputL(video_path) : ", contains_outputL(video_path))

        if contains_outputL(video_path):
            MainWindow.params["templateL"]=output_image
        if contains_outputR(video_path):
            MainWindow.params["templateR"]=output_image

def contains_outputL(path):
    return "output_L" in os.path.basename(path)

def contains_outputR(path):
    return "output_R" in os.path.basename(path)

def draw_points(MainWindow,actions,side):
    
    extract_img_from_video(MainWindow.params["folder_name"],MainWindow)

    exp_json=MainWindow.params["folder_name"]+"/points.json"
    
    if os.path.exists(exp_json):
        actions.load_data(exp_json)
    else:
        actions.load_data("points.json")

    if side=="L":
        imageSource = MainWindow.params["templateL"]
    else:
        imageSource = MainWindow.params["templateR"]

    print("imageSource : ", imageSource)


    actions.img = cv2.imread(imageSource, 1)
    
    actions.draw_circles(side)
    cv2.imshow('image', actions.img) 

    if side=="L":
        cv2.setMouseCallback('image', actions.click_event_L) 
    else:
        cv2.setMouseCallback('image', actions.click_event_R)


    while True:
        actions.img=[]
        actions.img = cv2.imread(imageSource, 1) 
        
        cv2.waitKey(500)

def save_points(MainWindow,actions):
    json_path1=MainWindow.params["folder_name"]+"/points.json"
    actions.save_points(json_path1)
    json_path2="points.json"
    actions.save_points(json_path2)