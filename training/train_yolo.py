"""
YOLOv8 Training Script

Trains a YOLOv8 model on a custom weed detection dataset
using CPU-friendly settings.
"""

from ultralytics import YOLO

# Load YOLOv8 Nano model (lightweight, suitable for CPU training)
model = YOLO("yolov8n.pt")

# Train the model
model.train(
    data=r"C:\Users\Admin\Downloads\Dataset29\dataset2.yaml",
    epochs=50,
    batch=16,
    imgsz=416,
    device="cpu"
)
