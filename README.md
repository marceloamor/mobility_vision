# Vision-Assisted Navigation System (V1)

This project implements a computer vision system for assisted navigation, designed as a prototype for smart glasses. The system uses YOLOv8 for object detection and OpenCV for video processing, focusing on detecting objects relevant to safe navigation in both indoor and outdoor environments.

## Features

- Real-time object detection using YOLOv8
- Video file processing capabilities
- Detection of navigation-relevant objects:
  - People
  - Cars
  - Bicycles
  - Traffic lights
  - Stop signs
  - Chairs
  - Tables
  - Doors

## Prerequisites

- Python 3.8+
- OpenCV
- YOLOv8 (via Ultralytics)
- CUDA-capable GPU (recommended for optimal performance)

## Installation

1. Clone the repository:
```
git clone <repository-url>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install ultralytics opencv-python numpy
```

## Project Structure

```
src/
├── main.py              # Entry point of the application
├── object_detector.py   # YOLOv8 object detection implementation
└── video_processor.py   # Video processing pipeline
```

## Usage

1. Place your video file in an accessible location

2. Update the video path in `src/main.py`:
```python
video_path = 'path/to/your/video.mp4'
```

3. Run the program:
```bash
python src/main.py
```

4. Controls:
- Press 'q' to quit the video processing

## Technical Details

### Object Detection
- Uses YOLOv8 nano model for initial testing
- Configurable target classes for specific navigation needs
- Real-time bounding box and label rendering

### Video Processing
- Frame-by-frame processing
- Real-time display of processed frames
- Configurable video input source

## Performance Considerations

- Default configuration uses YOLOv8 nano model for balance of speed and accuracy
- GPU acceleration recommended for real-time processing
- Frame processing speed depends on hardware capabilities

## Next Steps

1. Performance optimization
   - Frame rate optimization
   - Model optimization for edge deployment
   - Processing queue implementation

2. Feature additions
   - Distance estimation
   - Motion prediction
   - Audio feedback
   - Real-time camera input support

3. Testing and validation
   - Indoor navigation scenarios
   - Outdoor intersection scenarios
   - Different lighting conditions
   - Performance metrics collection

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
