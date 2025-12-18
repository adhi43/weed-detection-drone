import os
import json
import glob

# Define paths
labelme_dir =  "labelme_annotations"# Change this to your LabelMe JSON directory
yolo_dir ="yolo_labels" # Change this to your YOLO output directory

os.makedirs(yolo_dir, exist_ok=True)

# Define class mapping
class_mapping = {
    "lantana": 0,
    "parthenium": 1,
    "background" :2}  # Assign IDs to each class

# Process all JSON files in the folder
json_files = glob.glob(os.path.join(labelme_dir, "*.json"))

for json_file in json_files:
    with open(json_file, "r") as f:
        data = json.load(f)

    # Extract image dimensions
    image_width = data["imageWidth"]
    image_height = data["imageHeight"]

    yolo_annotations = []

    for shape in data["shapes"]:
        label = shape["label"].lower()  # Ensure label consistency
        if label not in class_mapping:
            continue  # Skip labels not in class_mapping

        class_id = class_mapping[label]
        (x1, y1), (x2, y2) = shape["points"]  # Bounding box coordinates

        # Convert to YOLO format (normalized x_center, y_center, width, height)
        x_center = ((x1 + x2) / 2) / image_width
        y_center = ((y1 + y2) / 2) / image_height
        width = abs(x2 - x1) / image_width
        height = abs(y2 - y1) / image_height

        yolo_annotations.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

    # Save YOLO annotation file
    txt_filename = os.path.join(yolo_dir, os.path.basename(json_file).replace(".json", ".txt"))
    with open(txt_filename, "w") as txt_file:
        txt_file.write("\n".join(yolo_annotations))

print("✅ LabelMe JSON files successfully converted to YOLO format!")
