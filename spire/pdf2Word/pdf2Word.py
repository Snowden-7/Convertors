'''
    To convert a PDF file to Word DOCX format using Python 
    and the Spire.PDF for Python library
'''
from spire.pdf.common import *
from spire.pdf import *


# Create a Pdf Document object 
pdf = PdfDocument()

# loads a PDF file
pdf.LoadFromFile("Sample.pdf")

## Converts the Pdf file to Word Docx file
pdf.SaveToFile("PdfToDocx.docx",FileFormat.DOCX)

## Close the Pdf object document
pdf.Close()