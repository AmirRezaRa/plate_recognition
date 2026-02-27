import argparse
import cv2
from src.detector import PlateDetector
from src.preprocess import preprocess_plate
from src.ocr import PlateOCR
from src.pipeline import PlateRecognitionPipeline





def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--weights", default="D:/main_project_vi/plate/best.pt")
    args = parser.parse_args()
    
    
    image = cv2.imread(args.image)
    if image is None:
        raise ValueError("Image not loaded. Check image path!")
    detector = PlateDetector(args.weights)
    ocr = PlateOCR()
    pipeline = PlateRecognitionPipeline(detector, preprocess_plate, ocr)


    plates = pipeline.run(image)
    print(plates)
    

if __name__ == "__main__":
    main()