import os
import shutil
import glob
import random

# Define dataset paths
image_dir = "Path to images"
label_dir = "Path to YOLO labels"
output_dir = "Output folder for train-test split"

# Create split folders
splits = ["train", "val", "test"]
for split in splits:
    os.makedirs(os.path.join(output_dir, "images", split), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "labels", split), exist_ok=True)

# Get all image files
image_files = glob.glob(os.path.join(image_dir, "*.jpg"))  # Modify for PNG if needed

# Group images by class
class_images = {"lantana": [], "parthenium": [],"background":[]}

for image_path in image_files:
    txt_file = os.path.join(label_dir, os.path.basename(image_path).replace(".jpg", ".txt"))
    if not os.path.exists(txt_file):
        continue  # Skip images without labels

    # Determine class based on label file
    with open(txt_file, "r") as f:
        lines = f.readlines()
    
    if not lines:
        continue  # Skip empty labels

    first_class_id = int(lines[0].split()[0])  # Get class from first annotation

    if first_class_id == 0:
        class_images["lantana"].append((image_path, txt_file))
    elif first_class_id == 1:
        class_images["parthenium"].append((image_path, txt_file))

# Define split ratios
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# Function to split and copy files
def split_and_copy(class_name, images, output_dir):
    random.shuffle(images)  # Shuffle to ensure randomness
    total = len(images)
    
    train_count = int(total * train_ratio)
    val_count = int(total * val_ratio)
    test_count = total - train_count - val_count

    split_data = {
        "train": images[:train_count],
        "val": images[train_count:train_count + val_count],
        "test": images[train_count + val_count:]
    }

    for split, files in split_data.items():
        for img_path, label_path in files:
            shutil.copy(img_path, os.path.join(output_dir, "images", split, os.path.basename(img_path)))
            shutil.copy(label_path, os.path.join(output_dir, "labels", split, os.path.basename(label_path)))

    print(f"✅ {class_name}: {train_count} train, {val_count} val, {test_count} test")

# Apply split for both classes
split_and_copy("lantana", class_images["lantana"], output_dir)
split_and_copy("parthenium", class_images["parthenium"], output_dir)
split_and_copy("background", class_images["background"], output_dir)


print("\n🎉 Train-Test Split Completed! Data saved in:", output_dir)
