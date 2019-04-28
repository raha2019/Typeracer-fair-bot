#opencv scanner for the text
'''
from PIL import ImageGrab
import numpy as np
import cv2
while(True):
    img = ImageGrab.grab(bbox=(200,10,400,780))
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("test", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''

import numpy as np
import cv2
from PIL import ImageGrab as ig
from PIL import Image
import time
import pytesseract
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

last_time = time.time()
while(True):
    screen = ig.grab(bbox=(1000,1000,2150,1100))
    print('Loop took {} seconds',format(time.time()-last_time))
    cv2.imshow("Live", np.array(screen))
    last_time = time.time()
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        ImageGrab.grab_to_file('output.png')
        cv2.destroyAllWindows()
        break

#ImageGrab.grab_to_file('im.png')

input = np.array(screen)
output = pytesseract.image_to_string(Image.open(input))
print(output)
