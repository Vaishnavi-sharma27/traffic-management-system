from ultralytics import YOLO
import cv2


model = YOLO("yolov8n.pt")

video = cv2.VideoCapture(
    "videos/traffic.mp4.mp4"
)
print("Video Opened:", video.isOpened())
while True:

    ret, frame = video.read()

    if not ret:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow(
        "Traffic Detection",
        annotated_frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()

cv2.destroyAllWindows()