import torch
import numpy as np

class ObjectDetection:
    def __init__(self, model_path):
        """
        Initialize the ObjectDetection class by loading the YOLOv8 model.
        Args:
            model_path (str): Path to the YOLOv8 model weights.
        """
        self.model = torch.hub.load("ultralytics/yolov8", model_path)  # Load YOLOv8 model

    def detect_objects(self, frame):
        """
        Detect objects in a frame using the YOLOv8 model.
        Args:
            frame (np.ndarray): Input frame from the camera feed.
        
        Returns:
            list: List of detections with bounding boxes, class labels, and confidence scores.
        """
        # Perform inference on the frame
        results = self.model(frame)

        # Extract results: Get the bounding boxes, classes, and confidences
        detections = []
        for bbox, conf, cls in zip(results.xywh[0], results.conf[0], results.cls[0]):
            bbox = bbox.tolist()
            conf = conf.item()
            cls = int(cls.item())
            label = results.names[cls]  # Get the class label by its ID

            # Append the detection information
            detections.append({
                'bbox': [int(bbox[0] - bbox[2] / 2), int(bbox[1] - bbox[3] / 2),
                         int(bbox[0] + bbox[2] / 2), int(bbox[1] + bbox[3] / 2)],
                'label': label,
                'confidence': conf
            })

        return detections
