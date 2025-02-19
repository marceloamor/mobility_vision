import cv2
from ultralytics import YOLO
import numpy as np
import time
import os

class ObjectDetector:
    def __init__(self):
        # Create models directory if it doesn't exist
        models_dir = 'assets/models'
        os.makedirs(models_dir, exist_ok=True)
        
        # Initialize YOLO model
        model_path = f'{models_dir}/yolov8n.pt'
        self.model = YOLO('yolov8n.pt')  # First run will download to current directory
        
        # Move the model file if it's in the root directory
        if os.path.exists('yolov8n.pt'):
            os.rename('yolov8n.pt', model_path)
            self.model = YOLO(model_path)
        
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