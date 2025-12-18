## Annotation Utilities

This folder contains preprocessing and validation utilities used in the
drone-based weed detection pipeline. These tools ensure annotation
consistency, dataset integrity, and quality before model training.

### LabelMe to YOLO Converter
- Converts polygon annotations from LabelMe JSON format
- Generates YOLO-compatible normalized bounding boxes
- Ensures consistent class-to-ID mapping across the dataset
- Used as part of the annotation preprocessing workflow

### YOLO Annotation Visualization
- Visualizes YOLO-format bounding boxes over corresponding images
- Supports batch processing of entire image directories
- Uses color-coded bounding boxes for different weed classes
- Helps validate annotation accuracy and detect labeling errors
- Used for dataset quality assurance prior to training

### Dataset Train/Validation/Test Split
- Splits YOLO-annotated images into train, validation, and test sets
- Preserves class balance across Lantana and Parthenium samples
- Maintains YOLO-compatible directory structure for images and labels
- Skips images without valid annotations
- Used to prepare clean and balanced datasets before training
