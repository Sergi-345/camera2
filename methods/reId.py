import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50
from PIL import Image
# from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


Step-by-Step Implementation
1️⃣ Extract Features Using a Pretrained CNN
We can use a model like ResNet50 (pretrained on ImageNet) to extract features from object images.


# Load a pretrained ResNet50 model
resnet = resnet50(pretrained=True)
resnet = torch.nn.Sequential(*list(resnet.children())[:-1])  # Remove final classification layer
resnet.eval()  # Set to evaluation mode

# Define image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize to ResNet input size
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def extract_features(image_path):
    """Extract feature vector from an object image."""
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        features = resnet(image)
    return features.squeeze().numpy()  # Convert to numpy array
2️⃣ Compute Cosine Similarity
Now, we compare feature vectors from different frames to determine which objects are the most similar.

python
Copy
Edit
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def find_best_match(prev_features, curr_features):
    """
    Match objects based on cosine similarity.
    :param prev_features: List of feature vectors from the previous frame
    :param curr_features: List of feature vectors from the current frame
    :return: Dictionary mapping previous objects to best-matched current objects
    """
    similarity_matrix = cosine_similarity(prev_features, curr_features)
    matches = {}

    for i, row in enumerate(similarity_matrix):
        best_match = np.argmax(row)  # Index of the most similar object
        matches[i] = best_match

    return matches  # Returns a dictionary {prev_object_index: best_curr_object_index}
3️⃣ Use This in YOLOv8 Tracking
When running YOLOv8 detection, crop each detected object and extract its feature vector:

python
Copy
Edit
from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Dictionary to store object features
prev_features = []

# Process video frame-by-frame
cap = cv2.VideoCapture("video.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO detection
    results = model(frame)

    # Extract bounding boxes
    curr_features = []
    for box in results[0].boxes.xyxy:
        x1, y1, x2, y2 = map(int, box)
        obj_crop = frame[y1:y2, x1:x2]  # Crop detected object
        obj_features = extract_features(obj_crop)  # Extract features
        curr_features.append(obj_features)

    # Compare with previous frame's objects
    if prev_features:
        matches = find_best_match(prev_features, curr_features)
        print("Object Matches:", matches)

    prev_features = curr_features  # Update for next frame

cap.release()
cv2.destroyAllWindows()