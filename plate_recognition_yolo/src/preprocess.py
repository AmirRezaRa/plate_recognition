import cv2
import matplotlib.pyplot as plt

def preprocess_plate(plate):
    gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    gray = cv2.equalizeHist(gray)
    # gray = cv2.GaussianBlur(gray, (3,3),0)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    # plate_rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    plt.imshow(gray)
    plt.show()
    return gray
    
    # # بزرگ کردن تصویر
    # gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # # حذف نویز سبک
    # gray = cv2.bilateralFilter(gray, 9, 75, 75)

    # # کنتراست بهتر
    # clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    # gray = clahe.apply(gray)

    # # باینری کردن حرفه‌ای
    # thresh = cv2.adaptiveThreshold(
    #     gray, 255,
    #     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #     cv2.THRESH_BINARY_INV,
    #     11, 2
    # )
    # plt.imshow(thresh)
    # plt.show()
    # return thresh