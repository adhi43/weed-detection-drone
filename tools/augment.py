"""
Albumentations-based augmentation for YOLO bounding boxes
Creates augmented images and corresponding YOLO annotation files.
"""

import os
import cv2
import albumentations as A

transform = A.Compose(
    [
        A.HorizontalFlip(p=0.5),
        A.RandomBrightnessContrast(p=0.3),
        A.Rotate(limit=15, p=0.3),
        A.MotionBlur(p=0.2),
    ],
    bbox_params=A.BboxParams(
        format="yolo",
        label_fields=["class_labels"],
        min_visibility=0.3
    )
)

def augment_image(image_path, label_path, output_img_dir, output_lbl_dir):
    os.makedirs(output_img_dir, exist_ok=True)
    os.makedirs(output_lbl_dir, exist_ok=True)

    image = cv2.imread(image_path)
    if image is None:
        return

    bboxes = []
    class_labels = []

    with open(label_path) as f:
        for line in f:
            cls, x, y, bw, bh = map(float, line.split())
            bboxes.append([x, y, bw, bh])
            class_labels.append(int(cls))

    if len(bboxes) == 0:
        return

    augmented = transform(
        image=image,
        bboxes=bboxes,
        class_labels=class_labels
    )

    img_name = os.path.basename(image_path)
    base, ext = os.path.splitext(img_name)

    aug_img_name = f"{base}_aug{ext}"
    aug_lbl_name = f"{base}_aug.txt"

    cv2.imwrite(
        os.path.join(output_img_dir, aug_img_name),
        augmented["image"]
    )

    with open(os.path.join(output_lbl_dir, aug_lbl_name), "w") as f:
        for cls, box in zip(augmented["class_labels"], augmented["bboxes"]):
            f.write(f"{cls} {' '.join(map(str, box))}\n")
