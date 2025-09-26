import cv2
import pytesseract
import pandas as pd
from pdf2image import convert_from_path
import numpy as np
import os

# === CONFIGURATION ===
INPUT_PDF = "o4.pdf"          # Your PDF file here
OUTPUT_DIR = "output"
DPI = 300                       # DPI for PDF to image conversion
DEBUG = True                    # Set True to see debug image previews

os.makedirs(OUTPUT_DIR, exist_ok=True)

def preprocess_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )
    return thresh

def extract_table_cells(img, debug=False):
    preprocessed = preprocess_image(img)

    # Detect horizontal and vertical lines
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 40))

    horizontal_lines = cv2.morphologyEx(preprocessed, cv2.MORPH_OPEN, horizontal_kernel)
    vertical_lines = cv2.morphologyEx(preprocessed, cv2.MORPH_OPEN, vertical_kernel)

    table_mask = cv2.add(horizontal_lines, vertical_lines)

    contours, _ = cv2.findContours(table_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours top-to-bottom, left-to-right
    bounding_boxes = sorted([cv2.boundingRect(c) for c in contours], key=lambda b: (b[1], b[0]))

    rows = []
    current_row = []
    last_y = -1
    y_threshold = 10

    # For debug visualization
    debug_img = img.copy()

    for (x, y, w, h) in bounding_boxes:
        if y > last_y + y_threshold:
            if current_row:
                rows.append(current_row)
            current_row = []
            last_y = y


        cell_img = img[y:y+h, x:x+w]
        # OCR config: single line, no dictionary corrections
        cell_text = pytesseract.image_to_string(cell_img, config="--psm 7").strip()
        current_row.append(cell_text)

        if debug:
            cv2.rectangle(debug_img, (x, y), (x + w, y + h), (0, 255, 0), 1)

    if current_row:
        rows.append(current_row)

    if debug:
        cv2.imshow("Detected Table Cells", debug_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return rows

def main():
    # Step 1: Convert PDF pages to images
    pages = convert_from_path(INPUT_PDF, dpi=DPI)
    all_rows = []

    for i, page in enumerate(pages):
        print(f"[INFO] Processing page {i+1} / {len(pages)}")

        img_path = os.path.join(OUTPUT_DIR, f"page_{i+1}.png")
        page.save(img_path, "PNG")

        img = cv2.imread(img_path)

        # Step 2 + 3: Extract table cells and OCR text
        rows = extract_table_cells(img, debug=DEBUG)
        all_rows.extend(rows)

    # Step 4: Export combined results to CSV and Excel
    df = pd.DataFrame(all_rows)
    csv_path = os.path.join(OUTPUT_DIR, "extracted_data.csv")
    excel_path = os.path.join(OUTPUT_DIR, "extracted_data.xlsx")

    df.to_csv(csv_path, index=False, header=False)
    df.to_excel(excel_path, index=False, header=False)



    print(f"[SUCCESS] Data extracted to:\n- {csv_path}\n- {excel_path}")

if __name__ == "__main__":
    main()
