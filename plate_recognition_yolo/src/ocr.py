import pytesseract
import easyocr
import cv2
import os
import re



class PlateOCR:
        def read(self, image):
            reader = easyocr.Reader(['en'], gpu=False)
            result = reader.readtext(image, detail=1)
            best_text, best_conf = None, 0.0
            for _, text, conf in result:
                text = re.sub(r'[^A-Z0-9]','', text)
                if conf > best_conf and len(text) >= 4:
                    best_text, best_conf = text, float(conf)
            
            correction1 = {
                'G':'6',
                'O':'0',
                'I':'1',
                'B':'8',
                'S':'5',
                'Z':'2',
                'Q':'0'
            }
            
            correction2 = {
                '6':'G',
                '0':'O',
                '1':'I',
                '8':'B',
                '5':'S',
                '2':'Z',
                '0':'Q'
            }
            new_text = ''
            if best_text is not None:
                for i, ch in enumerate(best_text):
                    if i in range(0,2):
                        new_text += ch
                        if ch in correction2:
                            list_new_text = list(new_text)
                            list_new_text[i] = correction2[ch]
                            new_text = ''.join(list_new_text)

                    if i in range(2,4):
                        new_text += ch
                        if ch in correction1:
                            list_new_text = list(new_text)
                            list_new_text[i] = correction1[ch]
                            new_text = ''.join(list_new_text)
                
                    if i in range(4,7):
                        new_text += ch
                        if ch in correction2:
                            list_new_text = list(new_text)
                            list_new_text[i] = correction2[ch]
                            new_text = ''.join(list_new_text)

            return new_text, best_conf