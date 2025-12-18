"""
YOLOv8 Image Inference Script (Jetson Nano)
"""

from ultralytics import YOLO
import cv2

MODEL_PATH = "best.pt"        # Copy your trained model to Jetson
IMAGE_PATH = "test.jpg"       # Test image
CONF_THRES = 0.4

# Load model
model = YOLO(MODEL_PATH)

# Run inference
results = model.predict(
    source=IMAGE_PATH,
    conf=CONF_THRES,
    device=0,        # 0 = GPU (Jetson), "cpu" if CUDA not available
    show=True
)

# Save result
results[0].save(filename="output.jpg")
