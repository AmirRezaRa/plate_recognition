from ultralytics import YOLO
import cv2


class PlateDetector:
    def __init__(self, model_path: str):
        print("Loading model from:", model_path)
        self.model = YOLO(model_path)
        self.model.to('cpu')
        print("Model loaded")
    
    def detect(self, image):
        # image = cv2.imread(image)
        results = self.model(image, device='cpu', conf=0.1)
        h, w = image.shape[:2]
        plates = []
        if results is None:
            print('None is in results...')
        for box in results[0].boxes:
            
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                plate = image[y1:y2+6, x1-7:x2+7]
                
                plates.append(plate)

        
        return plates

