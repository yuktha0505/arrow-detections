import cv2
from ultralytics import YOLO

weights_path = r"C:\Users\yukth\Desktop\yolo11\runs\detect\train\weights\best.pt"
model = YOLO(weights_path)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break


    results = model(frame)

   
    annotated_frame = results[0].plot()


    cv2.imshow("YOLO Detection", annotated_frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()