from ultralytics import YOLO
import cv2
from controllers.smart_controller import get_controller  # aj ki
print("Program Started")
model = YOLO("yolov8n.pt")
controller = get_controller()   # aj ki

video = cv2.VideoCapture(
    "videos/traffic.mp4.mp4"
)
lane_data = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0
}
print("Video Opened:", video.isOpened())
vehicle_classes = [
    "car",
    "truck",
    "bus",
    "motorcycle",
    "bicycle"
]
def start_detection(): # aj 
  while True:

    ret, frame = video.read()

    if not ret:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    vehicle_count = 0

    for box in results[0].boxes:

       class_id = int(box.cls[0])

       class_name = model.names[class_id]

       if class_name in [
           "car",
           "truck",
           "bus",
           "motorcycle",
           "bicycle"
       ]:
        vehicle_count += 1
        
    lane_data["A"] = vehicle_count
    controller.update_lane("A", vehicle_count)   # aj ki
     # print("Lane A:", vehicle_count)           # hr frame ke liye output print hogaaa
    cv2.putText(
        annotated_frame,
        f"Lane A Vehicles: {lane_data['A']}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )
         

    cv2.imshow(
        "Traffic Detection",
        annotated_frame
    )

    # print(
    #     "Vehicle Count:",
    #     vehicle_count         becoz infinite no. of output is printed for every frame
    # )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

  video.release()
  cv2.destroyAllWindows()