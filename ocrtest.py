import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\kaiy2\OCR\tesseract.exe"
)

image = Image.open("test.png")

text = pytesseract.image_to_string(
    image,
    lang="jpn"
)

print(text)
