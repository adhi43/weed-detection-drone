## Annotation & Preprocessing Tools

This folder contains utility scripts used during dataset preparation
for the drone-based weed detection pipeline. These tools ensure that
annotations and images are consistent, clean, and ready for training.

---

## Included Utilities

### LabelMe to YOLO Converter
- Converts polygon annotations from LabelMe JSON format
- Generates YOLO-compatible normalized bounding boxes
- Ensures consistent class-to-ID mapping across the dataset
- Used as part of the annotation preprocessing workflow

### YOLO Annotation Visualization
- Visualizes YOLO-format bounding boxes on corresponding images
- Supports batch processing of image directories
- Uses color-coded bounding boxes for different weed classes
- Helps validate annotation accuracy and detect labeling errors

### Dataset Split Utility
- Splits the dataset into train, validation, and test sets
- Maintains class balance during splitting
- Outputs directory structure compatible with YOLO training

### Image Preprocessing
- Validates image files and removes corrupted inputs
- Optionally downsamples extremely large images
- Leaves annotation files unchanged to avoid misalignment

---

## Purpose

These tools are intended to be run **before model training** to ensure:
- Clean and consistent annotations
- Correct dataset structure
- Reduced risk of training-time errors

All scripts are modular and can be executed independently as needed.
