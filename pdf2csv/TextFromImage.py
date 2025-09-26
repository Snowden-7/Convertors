from PIL import Image
import pytesseract

## sourcing the image 
inputFile =  "Sample.png"
image = Image.open(inputFile)

#### extractting text 
text= pytesseract.image_to_string(image)

print(text)


import cv2
import pytesseract

img = cv2.imread('Sample.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# Optional: use morphological operations to clean noise
#  gray = cv2.medianBlur(gray, 3)

text = pytesseract.image_to_string(gray)
print(text)