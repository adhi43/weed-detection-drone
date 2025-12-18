#!/bin/bash

# TensorRT export script for Jetson Nano
# Run this ON the Jetson device

MODEL_PATH=best.pt

echo "Exporting YOLO model to TensorRT engine..."

yolo export \
  model=$MODEL_PATH \
  format=engine \
  device=0 \
  imgsz=416 \
  half=True

echo "TensorRT engine export completed."
