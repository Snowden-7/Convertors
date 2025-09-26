'''
    Extracts out image  from pdf 
'''

from pdf2image import convert_from_path

pages = convert_from_path("o4.pdf" , dpi=300)
for i ,page in enumerate(pages):
    page.save(f"page_{i+1}.png","PNG")