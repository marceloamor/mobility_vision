# Assets Directory Structure

This directory contains all the media files and outputs for the vision-assisted navigation system.

## Directory Structure

```
assets/
├── input/
│   ├── videos/        # Store input video files for processing
│   └── images/        # Store individual images for processing
├── output/
│   ├── annotated_videos/    # Processed videos with object detection
│   ├── annotated_images/    # Processed images with object detection
│   └── logs/               # Processing logs and analytics
└── models/                 # Store trained models and weights
```

## Usage

1. Input Directory
   - Place your source videos in `input/videos/`
   - Place individual images in `input/images/`
   - Supported formats: .mp4, .avi, .mov (videos), .jpg, .png (images)

2. Output Directory
   - Processed videos will be saved in `output/annotated_videos/`
   - Processed images will be saved in `output/annotated_images/`
   - Processing logs are stored in `output/logs/`

3. Models Directory
   - Store YOLOv8 model weights and configurations
   - Default model will be downloaded automatically on first run

Note: Large media files should not be committed to the repository. 