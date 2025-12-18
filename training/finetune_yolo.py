"""
Fine-tunes an existing YOLOv8 weed detection model.
"""

from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

model.train(
    data="dataset.yaml",
    epochs=20,
    batch=16,
    imgsz=416,
    device="cpu"
)
