"""
Image preprocessing utility for YOLO training.

- Removes corrupted images
- Optionally resizes very large images
- Ensures clean dataset before training
"""

import os
import cv2

MAX_SIZE = 1920  # optional downscale limit

def preprocess_image(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            return False

        h, w = img.shape[:2]

        # Optional: downscale very large images
        if max(h, w) > MAX_SIZE:
            scale = MAX_SIZE / max(h, w)
            img = cv2.resize(img, (int(w * scale), int(h * scale)))
            cv2.imwrite(image_path, img)

        return True
    except Exception:
        return False


def preprocess_folder(image_dir):
    removed = 0
    for img_name in os.listdir(image_dir):
        img_path = os.path.join(image_dir, img_name)

        if not preprocess_image(img_path):
            os.remove(img_path)
            removed += 1

    print(f"Preprocessing complete. Removed {removed} corrupted images.")


if __name__ == "__main__":
    preprocess_folder("split_dataset/images/train")
