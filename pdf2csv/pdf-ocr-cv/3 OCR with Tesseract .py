import pytesseract
from pytesseract import Output

def extract_text(img):
    data = pytesseract.image_to_data(img,output_type=Output.DICT)


    '''
    For tables we use 
def extract_tsv(img):
    return pytesseract.image_to_data(img, output_type=Output.DATAFRAME)

    '''