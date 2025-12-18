"""
YOLOv8 Model Evaluation Script

Evaluates a trained YOLOv8 weed detection model on the validation dataset
and reports standard detection metrics.
"""

from ultralytics import YOLO

def evaluate_model(
    model_path="runs/detect/train/weights/best.pt",
    data_yaml="dataset.yaml"
):
    model = YOLO(model_path)

    metrics = model.val(
        data=data_yaml,
        save=True
    )

    print("\n📊 Model Evaluation Metrics")
    print(f"mAP@50      : {metrics.box.map50:.4f}")
    print(f"mAP@50-95   : {metrics.box.map:.4f}")
    print(f"Precision   : {metrics.box.p.mean():.4f}")
    print(f"Recall      : {metrics.box.r.mean():.4f}")

    print("\nEvaluation artifacts saved in:")
    print("runs/detect/val/")

if __name__ == "__main__":
    evaluate_model()
