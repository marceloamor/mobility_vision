import cv2
import time
from object_detector import ObjectDetector

class VideoProcessor:
    def __init__(self):
        self.detector = ObjectDetector()
        
    def process_video(self, video_path):
        # Open video file
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            print("Error: Could not open video.")
            return
        
        while True:
            ret, frame = cap.read()
            
            if not ret:
                print("End of video file.")
                break
            
            # Process frame
            processed_frame = self.detector.process_frame(frame)
            
            # Display frame
            cv2.imshow('Processed Video', processed_frame)
            
            # Break loop on 'q' press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows() 