import cv2
import time
from object_detector import ObjectDetector
import os
from pathlib import Path

class VideoProcessor:
    def __init__(self):
        self.detector = ObjectDetector()
        
    def process_video(self, video_path):
        # Open video file
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            print("Error: Could not open video.")
            return
            
        # Get video properties
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        
        # Create output path
        input_filename = Path(video_path).stem
        output_dir = 'assets/output/annotated_videos'
        os.makedirs(output_dir, exist_ok=True)
        output_path = f'{output_dir}/{input_filename}_annotated.mp4'
        
        # Initialize video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
        
        try:
            while True:
                ret, frame = cap.read()
                
                if not ret:
                    print("End of video file.")
                    break
                
                # Process frame
                processed_frame = self.detector.process_frame(frame)
                
                # Write the frame to output video
                out.write(processed_frame)
                
                # Display frame (optional)
                cv2.imshow('Processed Video', processed_frame)
                
                # Break loop on 'q' press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
        finally:
            # Clean up
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            
            if os.path.exists(output_path):
                print(f"Processed video saved to: {output_path}") 