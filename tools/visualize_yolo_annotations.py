import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import os
import glob

# Paths (Modify these)
image_dir = "Path to the images folder"
yolo_label_dir = "Path to YOLO labels"

# Define class labels and colors
class_labels = {0: "lantana", 1: "parthenium",2:"background"}
class_colors = {0: "red", 1: "blue"}

# Get all image files (modify extensions if needed)
image_files = glob.glob(os.path.join(image_dir, "*.jpg"))  # Change to "*.png" if needed

# Process each image
for image_path in image_files:
    # Find corresponding YOLO label file
    image_filename = os.path.basename(image_path).replace(".jpg", ".txt")  # Modify if using PNG
    yolo_txt_path = os.path.join(yolo_label_dir, image_filename)

    # Skip if annotation file does not exist
    if not os.path.exists(yolo_txt_path):
        print(f"Skipping {image_filename} (No YOLO annotation found)")
        continue

    # Load image
    image = Image.open(image_path)
    image_width, image_height = image.size

    # Create a Matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(image)

    # Read YOLO annotations
    with open(yolo_txt_path, "r") as f:
        lines = f.readlines()

    # Draw bounding boxes
    for line in lines:
        values = line.strip().split()
        class_id = int(values[0])
        x_center, y_center, width, height = map(float, values[1:])

        # Convert YOLO format (normalized) to pixel coordinates
        x1 = (x_center - width / 2) * image_width
        y1 = (y_center - height / 2) * image_height
        box_width = width * image_width
        box_height = height * image_height

        # Create a rectangle patch
        rect = patches.Rectangle((x1, y1), box_width, box_height, linewidth=2,
                                 edgecolor=class_colors.get(class_id, "green"), facecolor='none')
        ax.add_patch(rect)

        # Add label text
        ax.text(x1, y1 - 5, class_labels.get(class_id, "unknown"), color=class_colors.get(class_id, "green"),
                fontsize=12, fontweight="bold", bbox=dict(facecolor='white', alpha=0.5))

    # Hide axes
    ax.axis("off")
    plt.title(f"YOLO Bounding Box Visualization: {image_filename}")
    plt.show()
