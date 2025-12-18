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
    data="dataset.yaml",
    epochs=50,
    imgsz=416,
    batch=16,
    device="cpu",

    # Augmentation controls
    augment=True,      # Enable augmentation (default: True)
    mosaic=1.0,        # Probability of Mosaic
    mixup=0.2,         # Probability of MixUp
    hsv_h=0.015,       # Hue jitter
    hsv_s=0.7,         # Saturation jitter
    hsv_v=0.4,         # Value jitter
    fliplr=0.5,        # Horizontal flip
    translate=0.1,
    scale=0.5
)

