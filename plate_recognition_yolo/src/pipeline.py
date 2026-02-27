class PlateRecognitionPipeline:
    def __init__(self, detector, preprocessor, ocr):
        self.detector = detector
        self.preprocess = preprocessor
        self.ocr = ocr
    
    def run(self, image):
        plates = self.detector.detect(image)
        results = []
        
        for plate in plates:
            processed = self.preprocess(plate)
            text, conf = self.ocr.read(processed)
            results.append((text, conf))

        return results