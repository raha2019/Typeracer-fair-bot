from PIL import ImageGrab
from PIL import Image
import time
import pytesseract
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

quotation_mark = '"'
space_sign = ''
backspace = ''

#Character Find Function

def Character_Detection():
    if 'A' in output:
        print("A")
    elif "B" in output:
        print("B")
    elif "C" in output:
        print("C")
    elif "D" in output:
        print("D")
    elif "E" in output:
        print("E")
    elif "F" in output:
        print("F")
    elif "G" in output:
        print("G")
    elif "H" in output:
        print("H")
    elif "I" in output:
        print("I")
    elif "J" in output:
        print("J")
    elif "K" in output:
        print("K")
    elif "L" in output:
        print("L")
    elif "M" in output:
        print("M")
    elif "N" in output:
        print("N")
    elif "O" in output:
        print("O")
    elif "P" in output:
        print("P")
    elif "Q" in output:
        print("Q")
    elif "R" in output:
        print("R")
    elif "S" in output:
        print("S")
    elif "T" in output:
        print("T")
    elif "U" in output:
        print("U")
    elif "V" in output:
        print("V")
    elif "W" in output:
        print("W")
    elif "X" in output:
        print("X")
    elif "Y" in output:
        print("Y")
    elif "Z" in output:
        print("Z")
    elif "a" in output:
        print("a")
    elif "b" in output:
        print("b")
    elif "c" in output:
        print("c")
    elif "d" in output:
        print("d")
    elif "e" in output:
        print("e")
    elif "f" in output:
        print("f")
    elif "g" in output:
        print("g")
    elif "h" in output:
        print("h")
    elif "i" in output:
        print("i")
    elif "j" in output:
        print("j")
    elif "k" in output:
        print("k")
    elif "l" in output:
        print("l")
    elif "m" in output:
        print("m")
    elif "n" in output:
        print("n")
    elif "o" in output:
        print("o")
    elif "p" in output:
        print("p")
    elif "q" in output:
        print("q")
    elif "r" in output:
        print("r")
    elif "s" in output:
        print("s")
    elif "t" in output:
        print("t")
    elif "u" in output:
        print("u")
    elif "v" in output:
        print("v")
    elif "w" in output:
        print("w")
    elif "x" in output:
        print("x")
    elif "y" in output:
        print("y")
    elif "z" in output:
        print("z")
    elif "1" in output:
        print("1")
    elif "2" in output:
        print("2")
    elif "3" in output:
        print("3")
    elif "4" in output:
        print("4")
    elif "5" in output:
        print("5")
    elif "6" in output:
        print("6")
    elif "7" in output:
        print("7")
    elif "8" in output:
        print("8")
    elif "9" in output:
        print("9")
    elif "!" in output:
        print("!")
    elif "@" in output:
        print("@")
    elif "#" in output:
        print("#")
    elif "$" in output:
        print("$")
    elif "%" in output:
        print("%")
    elif "^" in output:
        print("^")
    elif "&" in output:
        print("&")
    elif "*" in output:
        print("*")
    elif "(" in output:
        print("(")
    elif ")" in output:
        print(")")
    elif "-" in output:
        print("-")
    elif "_" in output:
        print("_")
    elif "=" in output:
        print("=")
    elif "+" in output:
        print("+")
    elif "[" in output:
        print("[")
    elif "]" in output:
        print("]")
    elif "{" in output:
        print("{")
    elif "}" in output:
        print("}")
    elif ":" in output:
        print(":")
    elif ";" in output:
        print(";")
    elif "," in output:
        print(",")
    elif "/" in output:
        print("/")
    elif "." in output:
        print(".")
    elif "<" in output:
        print("<")
    elif ">" in output:
        print(">")
    elif "?" in output:
        print("?")
    elif "'" in output:
        print(" ' ")
    elif quotation_mark in output:
        print("quotation mark")
    elif space_sign in output:
        print("space")
    else:
        print("nothing")

while True:
    time.sleep(2)
    #im = ImageGrab.grab(bbox=(925,750,2175,835)) #adjust for your screen
    #print("2")
    #im.save('output.png')
    #im.show() #if you want to crash you computer and see the images
    input = "output.png"
    text = pytesseract.image_to_string(Image.open(input))
    #text = "Every artist is a man who has freed himself"
    x = 0
    while x<40:
        output = text[x]
        Character_Detection()
        x += 1

if __name__ == '__main__':
    main()
