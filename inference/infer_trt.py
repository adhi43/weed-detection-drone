"""
YOLOv8 TensorRT Inference Script (Jetson Nano)
"""

from ultralytics import YOLO
import cv2

model = YOLO("best.engine")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(
        source=frame,
        conf=0.45,
        imgsz=416,
        device=0,
        verbose=False
    )

    annotated = results[0].plot()
    cv2.imshow("Jetson TensorRT Inference", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
