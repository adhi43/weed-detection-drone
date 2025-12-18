"""
Jetson Nano YOLO Inference with DroneKit Servo Control
"""

from ultralytics import YOLO
from dronekit import connect
import cv2
import time

# ------------------ DroneKit Setup ------------------
vehicle = connect(
    '/dev/ttyACM0',   # or /dev/ttyUSB0
    baud=57600,
    wait_ready=True
)

SPRAY_CHANNEL = '9'     # AUX OUT → SERVO9
SPRAY_ON_PWM = 1900
SPRAY_OFF_PWM = 1100

def spray_on():
    vehicle.channels.overrides[SPRAY_CHANNEL] = SPRAY_ON_PWM
    print("Spray ON")

def spray_off():
    vehicle.channels.overrides[SPRAY_CHANNEL] = SPRAY_OFF_PWM
    print("Spray OFF")

# ------------------ YOLO Setup ------------------
model = YOLO("best.pt")   # or best.engine (TensorRT)

CONF_THRESHOLD = 0.5
TARGET_CLASSES = ["lantana", "parthenium"]

cap = cv2.VideoCapture(0)
spray_active = False

# ------------------ Main Loop ------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(
        source=frame,
        conf=CONF_THRESHOLD,
        imgsz=416,
        device=0,
        verbose=False
    )

    detected = False

    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        cls_name = model.names[cls_id]
        conf = float(box.conf[0])

        if cls_name in TARGET_CLASSES and conf > CONF_THRESHOLD:
            detected = True
            break

    if detected and not spray_active:
        spray_on()
        spray_active = True

    elif not detected and spray_active:
        spray_off()
        spray_active = False

    annotated = results[0].plot()
    cv2.imshow("Jetson Weed Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ------------------ Cleanup ------------------
cap.release()
vehicle.close()
cv2.destroyAllWindows()
