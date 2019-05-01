import re
from PIL import ImageGrab
from PIL import Image
import time
import pytesseract
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#Lowercase Letters
a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
f = 'f'
g = 'g'
h = 'h'
i = 'i'
j = 'j'
k = 'k'
l = 'l'
m = 'm'
n = 'n'
o = 'o'
p = 'p'
q = 'q'
r = 'r'
s = 's'
t = 't'
u = 'u'
v = 'v'
w = 'w'
x = 'x'
y = 'y'
z = 'z'

#Uppercase Letters
A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'
G = 'G'
H = 'H'
I = 'I'
J = 'J'
K = 'K'
L = 'L'
M = 'M'
O = 'O'
P = 'P'
Q = 'Q'
R = 'R'
S = 'S'
T = 'T'
U = 'U'
V = 'V'
W = 'W'
X = 'X'
Y = 'Y'
Z = 'Z'

#Numbers
zero = '0'
one = '1'
two = '2'
three = '3'
four = '4'
five = '5'
six = '6'
seven = '7'
eight = '8'
nine = '9'

#Symbols
at_symbol = '@'
hashtags = '#'
us_dollar = '$'
percentage = '%'
caret = '^'
and_symbol = '&'
asterisk = '*'
left_parenthesis = '('
right_parentheis = ')'
hyphen_minus = '-'
underscore = '_'
plus_sign = '+'
equal_sign = '='
left_bracket = '['
right_bracket = ']'
left_curly_bracket = '{'
right_curly_bracket = '}'
vertical_bar = '|'
slash = '/'

#Punctuation
period = '.'
comma = ','
question_mark = '?'
exclamtion_point = '!'
quotation_mark = '"'

#space sign and backspace
space_sign = ''
backspace = ''

#Program
while True:
    #time.sleep(10)
    #im = ImageGrab.grab(bbox=(925,750,2175,835))
    print("2")
    #im.save('output.png')
    #im.show()
    input = "output.png"
    output = pytesseract.image_to_string(Image.open(input))
    print(output)
    result = re.match(a, output)
        #result_e = re.match(b, output)
    if result:
        print("a found successfully")
        #elif result_e:
        #    print("e found success")
        #result = re.match(e, output)
        #if result:
        #    print("e found success")


        #elif result:
            #print("testing")
