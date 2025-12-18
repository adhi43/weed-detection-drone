## Inference & Deployment (Jetson Nano)

This folder contains scripts used for **deployment-time inference**
of the trained YOLOv8 model on NVIDIA Jetson Nano, along with
integration to the drone flight controller.

---

## Supported Inference Modes

### Image Inference
- Runs YOLOv8 on single images
- Used for quick validation and debugging

### Video / Camera Inference
- Runs real-time inference on live camera feed
- Displays bounding boxes and class labels
- Optimized for edge deployment

### Jetson Nano + Flight Controller Integration
- Performs real-time weed detection on Jetson Nano
- Uses DroneKit (MAVLink) to communicate with the flight controller
- Triggers auxiliary servo outputs for selective spraying
- Keeps perception (AI) and actuation (control) cleanly separated

---

## TensorRT Support
- Supports TensorRT-optimized YOLO models (`.engine`)
- Provides higher FPS and lower latency on Jetson Nano
- Engine files are generated per device and are not committed

---

## Output
- Live visualization via OpenCV window
- Physical actuation via flight controller AUX outputs
- Sample images and demo videos are stored separately under `outputs/`

---

## Notes
- Inference scripts are intended to run on Jetson Nano
- Training and evaluation are handled in separate modules
- Safety logic (confidence thresholds, servo control) is applied
  before triggering any actuation
