"""
YOLOv8 Real-Time Inference on Jetson Nano
"""

from ultralytics import YOLO
import cv2

model = YOLO("best.pt")
cap = cv2.VideoCapture(0)  # USB camera / CSI camera

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(
        source=frame,
        conf=0.4,
        device=0,
        verbose=False
    )

    annotated = results[0].plot()
    cv2.imshow("Jetson YOLO Inference", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
