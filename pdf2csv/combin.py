import cv2
import pytesseract
import pandas as pd

# Load and preprocess image
image = cv2.imread("Sample.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.adaptiveThreshold(
    blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)

# Detect horizontal and vertical lines to extract table
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 1))
vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 25))
horizontal_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel)
vertical_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel)

table_mask = cv2.add(horizontal_lines, vertical_lines)

# Find contours (cells)
contours, _ = cv2.findContours(table_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours top-to-bottom, left-to-right
bounding_boxes = sorted([cv2.boundingRect(c) for c in contours], key=lambda b: (b[1], b[0]))

rows = []
current_row = []
last_y = 0

for (x, y, w, h) in bounding_boxes:
    if y > last_y + 10:
        if current_row:
            rows.append(current_row)
        current_row = []
        last_y = y
    cell = image[y:y+h, x:x+w]
    cell_text = pytesseract.image_to_string(cell, config='--psm 7')
    current_row.append(cell_text.strip())

if current_row:
    rows.append(current_row)

# Convert to CSV/Excel
df = pd.DataFrame(rows)
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
print("[✅] Extracted to output.xlsx")
