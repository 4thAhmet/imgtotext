import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'PATH TO TESSERACT FOLDER'

img=Image.open('test.png')
text=pytesseract.image_to_string(img)

print(text)
