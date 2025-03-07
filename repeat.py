import cv2
import time

def play_video(nFrames,frame_count):
    print("repeating video")
    # Open the original high-FPS video
    input_file="/home/aitech/GIT/videos/output_120fps.avi"
    cap = cv2.VideoCapture(input_file)

    # Get properties
    #advance to the last nFrames
    print("frame_count : ", frame_count)
    print("nFrames : ", nFrames)
    if frame_count==0:
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if nFrames>1:
        # Ensure there are at least 60 frames
        if frame_count > nFrames:
            start_frame = frame_count - nFrames  # Start position for the last 60 frames
        else:
            start_frame = 0  # If less than 60 frames, start from the beginning

        # Move to the last 60 frames
        print("start_frame : ", start_frame)
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    fps_original = int(cap.get(cv2.CAP_PROP_FPS))  # Should be 120
    frame_size = (int(cap.get(3)), int(cap.get(4)))
    print("frame_count : ", frame_count)
    print(f"Original FPS: {fps_original}")
    print(f"Total frames: {frame_count}")

    cnt=0
    cnt_balls=0

    while cap.isOpened():

        cnt+=1
        ret, frame = cap.read()
        # try:
        #     if cnt<100:
        #         continue

        #     if cnt%60==0:
        #         cnt_balls+=1

        #     if cnt<start_frame:
        #         continue
                
        #     if not ret:
        #         break
            
        cv2.imshow("test",frame)
        # except:
        #     pass

        if cv2.waitKey(50) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("✅ Repeat finished!")

if __name__ == "__main__":
    play_video(1)
