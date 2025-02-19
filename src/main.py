from video_processor import VideoProcessor

def main():
    processor = VideoProcessor()
    
    # Replace with your video file path
    video_path = 'assets/input/videos/1university_video.mp4'
    
    processor.process_video(video_path)

if __name__ == "__main__":
    main() 