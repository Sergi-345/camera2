import cv2
import time

# Open the original high-FPS video
name="/home/aitech/GIT/videos/output_120fps"
input_file = name+".avi"
cap = cv2.VideoCapture(input_file)

# Get properties
fps_original = cap.get(cv2.CAP_PROP_FPS)  # Should be 120
frame_size = (int(cap.get(3)), int(cap.get(4)))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration_original = frame_count / fps_original

print(f"Original FPS: {fps_original}")
print(f"Total frames: {frame_count}")
print(f"Original Duration: {duration_original:.2f} seconds")

# Define new FPS for slow-motion effect
fps_slow = 15  # Slow motion target FPS
output_file = name+"_slowmotion.avi"

# Use a codec that supports high quality
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Use "FFV1" for lossless
out = cv2.VideoWriter(output_file, fourcc, fps_slow, frame_size)
init=time.time()
cnt=0
while cap.isOpened():
    cnt+=1
    if cnt%120==0:
        print("cnt : ", cnt)
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)  # Write all frames at 30 FPS

print("conversion time : ", time.time()-init)
cap.release()
out.release()
cv2.destroyAllWindows()

print("✅ Video saved in slow motion at 30 FPS")