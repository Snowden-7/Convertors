from spire.pdf.common import * 
from spire.pdf import *

outputFile = "testing.pdf"

## Create the PDF document object 
doc = PdfDocument()

## Create  a Page 
page = doc.Pages.Add()

s= "Hello , World"
x = 10.0
y = 10.0

font = PdfFont(PdfFontFamily.TimesRoman,20.0)
color = PdfRGBColor(Color.get_Black())
textBrush = PdfSolidBrush(color)

#Draw the text 
page.Canvas.DrawString(s, font , textBrush, x, y)

# save the document 
doc.SaveToFile(outputFile)
doc.Close()