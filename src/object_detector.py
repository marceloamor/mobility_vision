import cv2
from ultralytics import YOLO
import numpy as np
import time

class ObjectDetector:
    def __init__(self):
        # Initialize YOLO model
        self.model = YOLO('yolov8n.pt')  # Using the nano model for initial testing
        
        # Classes we're interested in for navigation
        self.target_classes = [
            'person', 'car', 'bicycle', 'traffic light', 'stop sign',
            'chair', 'table', 'door'
        ]
        
    def process_frame(self, frame):
        # Perform detection
        results = self.model(frame)
        
        # Process results
        annotated_frame = frame.copy()
        
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Get box coordinates
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                
                # Get class and confidence
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                
                # Get class name
                class_name = results[0].names[cls]
                
                # Only process if it's in our target classes
                if class_name in self.target_classes:
                    # Draw box
                    cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    
                    # Add label
                    label = f'{class_name} {conf:.2f}'
                    cv2.putText(annotated_frame, label, (x1, y1 - 10),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        return annotated_frame 