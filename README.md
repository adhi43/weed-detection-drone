
# Drone-Based Weed Detection and Selective Spraying 🚁🌿

An end-to-end edge-AI system for **real-time weed detection and selective spraying**
using **YOLOv8**, **NVIDIA Jetson Nano**, and **DroneKit-based flight controller integration**.

This project demonstrates a full pipeline from **data preparation and model training**
to **onboard inference and real-world actuation**.

---

## Problem Statement

Invasive weeds such as **Lantana** and **Parthenium** significantly reduce crop yield
and require precise treatment. Manual spraying is inefficient, labor-intensive,
and often damages surrounding crops.

---

## Solution Overview

This project implements a **drone-mounted vision system** that:

- Detects target weeds in real time using deep learning
- Runs inference on **Jetson Nano (edge device)**
- Communicates with the **flight controller via DroneKit (MAVLink)**
- Triggers a **sprayer/relay selectively**, avoiding non-target areas

---

## System Pipeline

Data Collection
↓
Annotation (LabelMe)
↓
LabelMe → YOLO Conversion
↓
Dataset Validation & Train/Val/Test Split
↓
Preprocessing (Image Quality Checks)
↓
YOLOv8 Training (Built-in Augmentation)
↓
Model Evaluation (mAP, Precision, Recall)
↓
Jetson Nano Inference (Real-Time)
↓
DroneKit → Flight Controller (AUX Servo)
↓
Selective Spraying


---

## Tech Stack

- **Programming Language**: Python
- **Model**: YOLOv8 (Nano / Small)
- **Frameworks**: Ultralytics YOLO, OpenCV
- **Edge Device**: NVIDIA Jetson Nano
- **Flight Control**: Pixhawk / Cube (ArduPilot)
- **Communication**: DroneKit (MAVLink)
- **Optimization**: TensorRT
- **Annotation Tool**: LabelMe

---

## Repository Structure

weed-detection-drone/
├── data_collection/        # Scripts for dataset collection (research use)
│   └── scrape_images.py
│
├── tools/                  # Annotation & preprocessing utilities
│   ├── labelme_to_yolo.py
│   ├── visualize_yolo_annotations.py
│   ├── split_dataset.py
│   ├── preprocess_images.py
│   └── README.md
│
├── training/               # Model training and fine-tuning
│   ├── train_yolo.py
│   └── finetune_yolo.py
│
├── evaluation/             # Model evaluation and metrics
│   └── evaluate_yolo.py
│
├── inference/              # Deployment & real-time inference
│   ├── infer_image.py
│   ├── infer_video.py
│   ├── jetson_dronekit_infer.py
│   └── README.md
│
├── optimization/           # TensorRT optimization for Jetson
│   ├── export_tensorrt.sh
│   └── README.md
│
├── outputs/                # Sample outputs (images, videos, logs)
│   ├── images/
│   ├── videos/
│   └── logs/
│
├── dataset.yaml            # YOLO dataset configuration
├── README.md               # Project overview and pipeline
└── .gitignore




---

## Dataset

- **Classes**
  - `lantana`
  - `parthenium`
- Dataset prepared using:
  - Manual image collection
  - Web-based reference images (research use)
  - LabelMe polygon annotations
- Converted to YOLO format and split into train/validation/test

> **Note**: Full dataset is not included due to size and IP constraints.

---

## Preprocessing & Augmentation

### Preprocessing
- Image validation and corruption checks
- Optional downscaling of extremely large images
- Labels remain untouched to avoid misalignment

### Augmentation
- YOLOv8 built-in augmentation:
  - Mosaic
  - MixUp
  - HSV jitter
  - Scaling and flipping

No offline augmentation is required for standard training.

---

## Model Training

- Base model: `yolov8n.pt` / `yolov8s.pt`
- CPU-friendly settings for experimentation
- Early stopping via **patience**
- Reproducible training using `dataset.yaml`

---

## Model Evaluation

Evaluation performed on validation data using:
- **mAP@0.5**
- **mAP@0.5:0.95**
- **Precision**
- **Recall**
- Confusion matrix and prediction visualizations

Artifacts are saved automatically under `runs/detect/val/`.

---

## Jetson Nano Inference

- Real-time inference using USB / CSI camera
- Optimized input size for FPS vs accuracy trade-off
- Supports:
  - PyTorch inference
  - TensorRT-optimized inference (`.engine`)

---

## Flight Controller Integration

- Jetson communicates with the flight controller using **DroneKit**
- AUX servo outputs are used to control:
  - Relay
  - Pump
  - Sprayer

### Trigger Logic
- If target weed detected → **SPRAY ON**
- If no target detected → **SPRAY OFF**
- Ensures selective and controlled spraying

---

## TensorRT Optimization

- YOLO model exported to TensorRT on Jetson Nano
- Provides significantly higher FPS and lower latency
- Engine files are **not committed** (hardware-specific)
- Export scripts are provided for reproducibility

---

## Demo & Outputs

Due to GitHub limitations on video preview:



▶️ **Demo Video**:  
lantana - https://drive.google.com/drive/folders/1mAF7guROvbUGA6PAaTVY89e-JJCryNdG?usp=sharing
parthenium - https://drive.google.com/drive/folders/1XYsGFoF6a56EdG9odOfs-lNb-xFzzvXN?usp=sharing

---

## Safety & Reliability Considerations

- Confidence thresholding to reduce false triggers
- Servo control via flight controller (not direct GPIO)
- Separation of perception (AI) and actuation (control)
- Easy integration of debounce and failsafe logic

---

## Key Learnings

- End-to-end ML system design (not just model training)
- Edge AI deployment constraints and optimization
- Real-time integration between AI and embedded systems
- Importance of clean pipelines and reproducibility

---

## Future Improvements

- Pixel-wise weed segmentation
- Multi-class weed detection
- GPS-aware spraying logic
- Autonomous navigation without GPS
- Advanced failsafe and debounce mechanisms

---

## Author

**Adarsh Anil**  
AI & Computer Vision Engineer  
Drone-based Edge AI Systems  

---

## License

This project is released under the **MIT License**.
