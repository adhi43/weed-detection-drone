## TensorRT Optimization (Jetson Nano)

This folder contains utilities for optimizing the trained YOLOv8 weed
detection model using NVIDIA TensorRT for high-performance inference
on Jetson Nano.

### Why TensorRT
- Significantly improves inference FPS on Jetson devices
- Reduces latency for real-time drone applications
- Performs layer fusion and precision optimization
- Optimized specifically for NVIDIA GPU hardware

### Exporting the Model
TensorRT engine files must be generated **on the target Jetson device**.

Run the following command on Jetson Nano:

```bash
bash export_tensorrt.sh
