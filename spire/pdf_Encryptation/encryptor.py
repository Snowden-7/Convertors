from spire.pdf.common import *
from spire.pdf import *

# Create the PDF dcoument  object 
doc = PdfDocument()

## load a sample PDF file
doc.LoadFromFile("tesing.pdf")

## Encrypt the PDF file with an open password and a persmission password 
doc.Security.Encrypt("openPsd","permissionPsd",PdfPermissionsFlags.FillFields, PdfEncryptionKeySize.Key128Bit)

## save the document 
doc.SaveToFile("Output/Encrypted.pdf", FileFormat.PDF)

