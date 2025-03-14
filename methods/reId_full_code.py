import torch
import cv2
import numpy as np
from ultralytics import YOLO
from torchvision import models, transforms
from sklearn.metrics.pairwise import cosine_similarity

# Load YOLOv8 model
yolo_model = YOLO("yolov8n.pt")

# Load ResNet50 for feature extraction (pretrained on ImageNet)
resnet = models.resnet50(pretrained=True)
resnet = torch.nn.Sequential(*list(resnet.children())[:-1])  # Remove final classification layer
resnet.eval()  # Set to evaluation mode

# Define image transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def extract_features(image):
    """Extract feature vector from an object image using ResNet50."""
    image = transform(image).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        features = resnet(image).squeeze().numpy()  # Extract features
    return features / np.linalg.norm(features)  # Normalize features

def find_best_match(prev_features, curr_features):
    """Match objects between frames using cosine similarity."""
    if not prev_features:
        return {i: None for i in range(len(curr_features))}  # No previous data

    similarity_matrix = cosine_similarity(prev_features, curr_features)
    matches = {}

    for i, row in enumerate(similarity_matrix):
        best_match = np.argmax(row)  # Find most similar object
        matches[i] = best_match

    return matches  # Returns {current_obj_index: previous_obj_index}

# Open video capture
cap = cv2.VideoCapture("video.mp4")
prev_objects = []  # Store previous frame's object features

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 detection
    results = yolo_model(frame)

    curr_features = []
    curr_boxes = []

    for box in results[0].boxes.xyxy:
        x1, y1, x2, y2 = map(int, box)
        obj_crop = frame[y1:y2, x1:x2]  # Crop detected object
        if obj_crop.size == 0:
            continue

        # Convert OpenCV image (BGR) to PIL (RGB)
        obj_crop_pil = cv2.cvtColor(obj_crop, cv2.COLOR_BGR2RGB)
        obj_crop_pil = transforms.ToPILImage()(obj_crop_pil)

        # Extract features
        obj_features = extract_features(obj_crop_pil)
        curr_features.append(obj_features)
        curr_boxes.append((x1, y1, x2, y2))

    # Find object matches with previous frame
    matches = find_best_match(prev_objects, curr_features)

    # Draw bounding boxes with assigned IDs
    for curr_idx, prev_idx in matches.items():
        x1, y1, x2, y2 = curr_boxes[curr_idx]
        obj_id = prev_idx if prev_idx is not None else curr_idx  # Assign ID
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"ID: {obj_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Tracking", frame)
    prev_objects = curr_features  # Update previous features

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()