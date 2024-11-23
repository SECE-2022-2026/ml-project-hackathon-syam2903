from ultralytics import YOLO
import cv2

class AROverlay:
    def __init__(self, model_path, obj_path):
        self.model = YOLO(model_path)  # Loading YOLOv8 model
        self.obj_path = obj_path
        self.frame = None  # Frame to overlay 3D object

    def overlay_3d_on_frame(self):
        if self.frame is None:
            print("Error: Frame is None. Please provide a valid frame.")
            return

        results = self.model(self.frame)  # YOLO inference
        boxes = results[0].boxes.cpu().numpy()  # Extract bounding boxes
        
        for box in boxes:
            if len(box) == 4:
                x1, y1, x2, y2 = box  # Extract coordinates
                print(f"Bounding box: {x1}, {y1}, {x2}, {y2}")
        
        if self.frame.shape[0] > 0 and self.frame.shape[1] > 0:
            cv2.imshow("AR Overlay", self.frame)
        else:
            print("Error: Frame has invalid size.")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()

    def set_frame(self, frame):
        """Sets the current frame"""
        self.frame = frame
