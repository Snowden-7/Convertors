from spire.pdf.common import *
from spire.pdf import *
from typing import  List
import os 

inputFile ="Sample.pdf"
outputFile = "Sample.txt"

def WriteAllText(fname: str, text: str):
    with open(fname, "w", encoding="utf-8") as fp:
        fp.write(text)


if not os.path.exists(inputFile):
    print(f"Error : File not found  -{inputFile}")
    exit(1)




doc =PdfDocument()

## Read a pdf file
doc.LoadFromFile(inputFile)

#get the first page 
page = doc.Pages[0]
'''
## Extract text from page keeping white space
#text =page.ExtractText(True)

## Write  a line of text to the file
#WriteAllText(outputFile,text)

'''
## To convert multi  pages of the PDF 
all_text = ""
for i in range(doc.Pages.Count):
    page = doc.Pages[i]
    extractor = PdfTextExtractor(page)
    options = PdfTextExtractOptions()  # Create default options
    page_text = extractor.ExtractText(options)  # Pass options here
    all_text += f"\n--- Page {i + 1} ---\n"
    all_text += page_text + "\n"

### to remove the filter 
def remove_evaluation_warning(text: str) -> str:
    """
    Removes the line containing 'Evaluation Warning : The document was created with Spire.PDF for Python.'
    from the given text.
    """
    lines = text.splitlines()
    filtered_lines = [
        line for line in lines
        if "Evaluation Warning : The document was created with Spire.PDF for Python." not in line
    ]
    return "\n".join(filtered_lines)

clean_text = remove_evaluation_warning(all_text)
WriteAllText(outputFile, clean_text)


doc.Close()

print(f"Text extracted and saved to {outputFile}")