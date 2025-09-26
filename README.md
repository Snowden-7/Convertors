# ⚡ Convertors

**Convertors** is your Swiss Army Knife for PDF workflows—a comprehensive Python toolkit to convert, extract, encrypt, and process PDF files into formats like **CSV, Excel, Word, PowerPoint, images, and text**. With built-in OCR (Tesseract + OpenCV), it can digitize even scanned tables and complex documents.

---

## ⚡ Features

- **PDF → CSV/Excel** (with OCR for scanned tables)
- **PDF → PowerPoint** (`.pptx`, editable slides)
- **PDF → Word**, **Text**, **Images**
- **PDF Encryption** (passwords, restrictions)
- **PDF Creation** (sample/test PDFs from Python)

---

## ⚡ Quick Start

Convert your PDF into all major formats in just a few commands 🚀

```bash
# Clone and install
git clone https://github.com/Snowden-7/Convertors.git
cd Convertors
pip install -r requirements.txt
```

### ⚡ PDF → CSV / Excel (with OCR)

```bash
cd pdf2csv/pdf-ocr-cv
python "1 Pdf2Image.py" && python "2 Preproccess image.py" && \
python "3 OCR with Tesseract .py" && python "4 Write to csv.py"
```
✅ Output: `output/extracted_data.csv` and `output/extracted_data.xlsx`

---

### ⚡ PDF → PowerPoint

```bash
cd pdf2PowerPoint
python pdf2ppt.py
```
✅ Output: `output.pptx`

---

### ⚡ PDF → Word

```bash
cd spire/pdf2Word
python pdf2Word.py
```
✅ Output: `PdfToDocx.docx`

---

### ⚡ PDF → Text

```bash
cd spire/pdf2Text
python pdf2text.py
```
✅ Output: `Sample.txt`

---

### ⚡ PDF → Images

```bash
cd spire/pdf2Images
# Generates page_1.png, page_2.png, etc.
```

---

### ⚡ Encrypt a PDF

```bash
cd spire/pdf_Encryptation
python encryptor.py
```
✅ Output: `encrypted.pdf`

---

## ⚡ Project Layout

```
Convertors/
│
├── pdf2csv/                # OCR PDF → CSV/Excel
│   ├── combin.py
│   ├── TextFromImage.py
│   ├── output.csv / output.xlsx
│   └── pdf-ocr-cv/         # OCR pipeline (image → text → CSV/Excel)
│       ├── 1 Pdf2Image.py
│       ├── 2 Preproccess image.py
│       ├── 3 OCR with Tesseract .py
│       ├── 4 Write to csv.py
│       ├── combined.py
│       ├── output/        # OCR results (CSV/XLSX + images)
│       └── images_output/ # Intermediate image outputs

├── pdf2PowerPoint/         # PDF → PPTX
│   └── pdf2ppt.py

├── spire/                  # Spire.PDF utilities
│   ├── pdf/                # Create PDFs
│   │   └── Creating_pdf.py
│   ├── pdf2Excel/
│   │   └── pdf2excel.py
│   ├── pdf2Images/
│   ├── pdf2PowerPoint/
│   │   └── pdf2ppt.py
│   ├── pdf2Text/
│   │   └── pdf2text.py
│   ├── pdf2Word/
│   │   ├── pdf2Word.py
│   │   ├── pdf2Word2.py
│   │   └── PdfToDocx.docx
│   └── pdf_Encryptation/
│       └── encryptor.py

├── Sample.pdf / testing.pdf
└── requirements.txt
```

---

## ⚡ Requirements

- **Python 3.9+**
- OCR: `tesseract`, `opencv-python`, `pdf2image`, `pillow`
- Converters: `PyPDF2`, `pdfplumber`, `python-docx`, `python-pptx`
- Data: `pandas`, `openpyxl`, `numpy`
- **External:** [Spire.PDF](https://www.e-iceblue.com/Introduce/pdf-for-python.html)

Install all dependencies:
```bash
pip install -r requirements.txt
```

⚠️ **Spire.PDF Notice**:  
To use Spire-based tools, download and install Spire.PDF manually from  
👉 [Spire.PDF official site](https://www.e-iceblue.com/Introduce/pdf-for-python.html)  

---

## ⚡ Roadmap

- [ ] Unified CLI (`convertor.py`) for all conversions
- [ ] Batch PDF conversion support
- [ ] GUI frontend (Tkinter or PyQt)
- [ ] Docker image for portability

---

## 🤝 Contribution

Contributions are welcome!

1. Fork the repo
2. Create a new branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Added new feature'`
4. Push branch: `git push origin feature-name`
5. Open a Pull Request

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

Developed by **Snowden 7**  
📧 Contact: [snowden 7](mailto:segawaabdul@gmail.com)  
💼 GitHub: [Snowden-7](https://github.com/Snowden-7)

---
