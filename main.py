from PIL import Image
import pytesseract as tes
from PIL import ImageEnhance,ImageFilter
tes.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img=Image.open("C:\\Users\\aryan\\Pictures\\Screenshots\\hp_first_page.png")
scale=2
enhacner=ImageEnhance.Contrast(img)
img=img.resize((img.width*scale,img.height*scale),Image.LANCZOS)
img=img.convert("L")
enchance=enhacner.enhance(2)
img=img.filter(ImageFilter.MedianFilter())
img.show()
pix=img.load()
stuff=tes.image_to_string(img,config="--psm 6")
print(stuff)