## A complete end-to-end Automatic License Plate Recognition (ALPR) system using YOLOv8 for plate detection and EasyOCR for text recognition.

This project is designed as a production-style pipeline:
    Training on Google Colab (GPU)
    Inference on local machine (VS Code)
    OCR fully handled by EasyOCR, improving accuracy and multi-language support.


## Pipeline Overview
Input Image / Video
        ↓
License Plate Detection (YOLOv8)
        ↓
Plate Cropping
        ↓
Image Preprocessing
        ↓
OCR (EasyOCR)
        ↓
License Plate Text


## Features
    Fast and accurate license plate detection using YOLOv8
    OCR using EasyOCR (supports multiple languages)
    Image preprocessing for improved OCR accuracy
    Lightweight inference (CPU supported)
    Clean, modular, and extensible codebase
    Ready for image, video, or webcam input


## Model Training
YOLOv8 trained on Google Colab with GPU
Custom dataset formatted in YOLO style
Trained model weights (best.pt) are required for inference

## Install Dependencies
pip install -r requirements.txt


## Inference
python inference.py --image plate/images.jpeg --weights weights/best.pt



## Example Output:
Detected Plates: ['plate', 'confidence']


## Technologies Used
Python
YOLOv8 (Ultralytics)
OpenCV
EasyOCR
NumPy


## Limitations & Improvements
OCR accuracy depends on plate quality, angle, and lighting
For best results:
Preprocessing (grayscale, bilateral filter, threshold) is recommended
Multiple languages can be added in EasyOCR reader

---
## results:
for example demo.jpeg:

![prediction](demo.jpeg)

```
[('CCC444', 0.523106337496418)]
```
