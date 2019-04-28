from PIL import ImageGrab
from PIL import Image
import time
import pytesseract
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


while True:
    time.sleep(5)
    print("1")
    im = ImageGrab.grab(bbox=(1000,1000,2150,1100))
    print("2")
    im.save('output.png')
    im.show()
    input = "output.png"
    output = pytesseract.image_to_string(Image.open(input))
    print(output)
