import cv2


def preproccess_image(img):
    image =cv2.imreading(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    blur = cv2.GaussianBlur(gray, (3,3),0)
    thresh = cv2.adaptiveThreshold(
        blur, 255 ,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2
    )
    return thresh