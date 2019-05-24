from pynput.keyboard import Key, Controller
from PIL import ImageGrab
from PIL import Image
import time
import datetime
import pytesseract
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

quotation_mark = '"'
space_sign = ''

keyboard = Controller()

#Character Find Function
def Character_Detection():
    if 'A' in output:
        print("A")
        with keyboard.pressed(Key.shift):
            keyboard.press('a')
            keyboard.release('a')
    elif "B" in output:
        print("B")
        with keyboard.pressed(Key.shift):
            keyboard.press('b')
            keyboard.release('b')
    elif "C" in output:
        print("C")
        with keyboard.pressed(Key.shift):
            keyboard.press('c')
            keyboard.release('c')
    elif "D" in output:
        print("D")
        with keyboard.pressed(Key.shift):
            keyboard.press('d')
            keyboard.release('d')
    elif "E" in output:
        print("E")
        with keyboard.pressed(Key.shift):
            keyboard.press('e')
            keyboard.release('e')
    elif "F" in output:
        print("F")
        with keyboard.pressed(Key.shift):
            keyboard.press('f')
            keyboard.release('f')
    elif "G" in output:
        print("G")
        with keyboard.pressed(Key.shift):
            keyboard.press('g')
            keyboard.release('g')
    elif "H" in output:
        print("H")
        with keyboard.pressed(Key.shift):
            keyboard.press('h')
            keyboard.release('h')
    elif "I" in output:
        print("I")
        with keyboard.pressed(Key.shift):
            keyboard.press('i')
            keyboard.release('i')
    elif "J" in output:
        print("J")
        with keyboard.pressed(Key.shift):
            keyboard.press('j')
            keyboard.release('j')
    elif "K" in output:
        print("K")
        with keyboard.pressed(Key.shift):
            keyboard.press('k')
            keyboard.release('k')
    elif "L" in output:
        print("L")
        with keyboard.pressed(Key.shift):
            keyboard.press('l')
            keyboard.release('l')
    elif "M" in output:
        print("M")
        with keyboard.pressed(Key.shift):
            keyboard.press('m')
            keyboard.release('m')
    elif "N" in output:
        print("N")
        with keyboard.pressed(Key.shift):
            keyboard.press('n')
            keyboard.release('n')
    elif "O" in output:
        print("O")
        with keyboard.pressed(Key.shift):
            keyboard.press('o')
            keyboard.release('o')
    elif "P" in output:
        print("P")
        with keyboard.pressed(Key.shift):
            keyboard.press('p')
            keyboard.release('p')
    elif "Q" in output:
        print("Q")
        with keyboard.pressed(Key.shift):
            keyboard.press('q')
            keyboard.release('q')
    elif "R" in output:
        print("R")
        with keyboard.pressed(Key.shift):
            keyboard.press('r')
            keyboard.release('r')
    elif "S" in output:
        print("S")
        with keyboard.pressed(Key.shift):
            keyboard.press('s')
            keyboard.release('s')
    elif "T" in output:
        print("T")
        with keyboard.pressed(Key.shift):
            keyboard.press('t')
            keyboard.release('t')
    elif "U" in output:
        print("U")
        with keyboard.pressed(Key.shift):
            keyboard.press('u')
            keyboard.release('u')
    elif "V" in output:
        print("V")
        with keyboard.pressed(Key.shift):
            keyboard.press('v')
            keyboard.release('v')
    elif "W" in output:
        print("W")
        with keyboard.pressed(Key.shift):
            keyboard.press('w')
            keyboard.release('w')
    elif "X" in output:
        print("X")
        with keyboard.pressed(Key.shift):
            keyboard.press('x')
            keyboard.release('x')
    elif "Y" in output:
        print("Y")
        with keyboard.pressed(Key.shift):
            keyboard.press('y')
            keyboard.release('y')
    elif "Z" in output:
        print("Z")
        with keyboard.pressed(Key.shift):
            keyboard.press('z')
            keyboard.release('z')
    elif "a" in output:
        print("a")
        keyboard.press('a')
        keyboard.release('a')
    elif "b" in output:
        print("b")
        keyboard.press('b')
        keyboard.release('b')
    elif "c" in output:
        print("c")
        keyboard.press('c')
        keyboard.release('c')
    elif "d" in output:
        print("d")
        keyboard.press('d')
        keyboard.release('d')
    elif "e" in output:
        print("e")
        keyboard.press('e')
        keyboard.release('e')
    elif "f" in output:
        print("f")
        keyboard.press('f')
        keyboard.release('f')
    elif "g" in output:
        print("g")
        keyboard.press('g')
        keyboard.release('g')
    elif "h" in output:
        print("h")
        keyboard.press('h')
        keyboard.release('h')
    elif "i" in output:
        print("i")
        keyboard.press('i')
        keyboard.release('i')
    elif "j" in output:
        print("j")
        keyboard.press('j')
        keyboard.release('j')
    elif "k" in output:
        print("k")
        keyboard.press('k')
        keyboard.release('k')
    elif "l" in output:
        print("l")
        keyboard.press('l')
        keyboard.release('l')
    elif "m" in output:
        print("m")
        keyboard.press('m')
        keyboard.release('m')
    elif "n" in output:
        print("n")
        keyboard.press('n')
        keyboard.release('n')
    elif "o" in output:
        print("o")
        keyboard.press('o')
        keyboard.release('o')
    elif "p" in output:
        print("p")
        keyboard.press('p')
        keyboard.release('p')
    elif "q" in output:
        print("q")
        keyboard.press('q')
        keyboard.release('q')
    elif "r" in output:
        print("r")
        keyboard.press('r')
        keyboard.release('r')
    elif "s" in output:
        print("s")
        keyboard.press('s')
        keyboard.release('s')
    elif "t" in output:
        print("t")
        keyboard.press('t')
        keyboard.release('t')
    elif "u" in output:
        print("u")
        keyboard.press('u')
        keyboard.release('u')
    elif "v" in output:
        print("v")
        keyboard.press('v')
        keyboard.release('v')
    elif "w" in output:
        print("w")
        keyboard.press('w')
        keyboard.release('w')
    elif "x" in output:
        print("x")
        keyboard.press('x')
        keyboard.release('x')
    elif "y" in output:
        print("y")
        keyboard.press('y')
        keyboard.release('y')
    elif "z" in output:
        print("z")
        keyboard.press('z')
        keyboard.release('z')
    elif "1" in output:
        print("1")
        keyboard.press('1')
        keyboard.release('1')
    elif "2" in output:
        print("2")
        keyboard.press('2')
        keyboard.release('2')
    elif "3" in output:
        print("3")
        keyboard.press('3')
        keyboard.release('3')
    elif "4" in output:
        print("4")
        keyboard.press('4')
        keyboard.release('4')
    elif "5" in output:
        print("5")
        keyboard.press('5')
        keyboard.release('5')
    elif "6" in output:
        print("6")
        keyboard.press('6')
        keyboard.release('6')
    elif "7" in output:
        print("7")
        keyboard.press('7')
        keyboard.release('7')
    elif "8" in output:
        print("8")
        keyboard.press('8')
        keyboard.release('8')
    elif "9" in output:
        print("9")
        keyboard.press('9')
        keyboard.release('9')
    elif "!" in output:
        print("!")
        with keyboard.pressed(Key.shift):
            keyboard.press('1')
            keyboard.release('1')
    elif "@" in output:
        with keyboard.pressed(Key.shift):
            print("@")
            keyboard.press('2')
            keyboard.release('2')
    elif "#" in output:
        print("#")
        with keyboard.pressed(Key.shift):
            keyboard.press('3')
            keyboard.release('3')
    elif "$" in output:
        print("$")
        with keyboard.pressed(Key.shift):
            keyboard.press('4')
            keyboard.release('4')
    elif "%" in output:
        print("%")
        with keyboard.pressed(Key.shift):
            keyboard.press('5')
            keyboard.release('5')
    elif "^" in output:
        print("^")
        with keyboard.pressed(Key.shift):
            keyboard.press('6')
            keyboard.release('6')
    elif "&" in output:
        print("&")
        with keyboard.pressed(Key.shift):
            keyboard.press('7')
            keyboard.release('7')
    elif "*" in output:
        print("*")
        with keyboard.pressed(Key.shift):
            keyboard.press('8')
            keyboard.release('8')
    elif "(" in output:
        print("(")
        with keyboard.pressed(Key.shift):
            keyboard.press('9')
            keyboard.release('9')
    elif ")" in output:
        print(")")
        with keyboard.pressed(Key.shift):
            keyboard.press('0')
            keyboard.release('0')
    elif "-" in output:
        print("-")
        keyboard.press('-')
        keyboard.release('-')
    elif "_" in output:
        print("_")
        with keyboard.pressed(Key.shift):
            keyboard.press('-')
            keyboard.release('-')
    elif "=" in output:
        print("=")
        keyboard.press('=')
        keyboard.release('=')
    elif "+" in output:
        print("+")
        with keyboard.pressed(Key.shift):
            keyboard.press('=')
            keyboard.release('=')
    elif "[" in output:
        print("[")
        keyboard.press('[')
        keyboard.release('[')
    elif "]" in output:
        print("]")
        keyboard.press(']')
        keyboard.release(']')
    elif "{" in output:
        print("{")
        with keyboard.pressed(Key.shift):
            keyboard.press('[')
            keyboard.release('[')
    elif "}" in output:
        print("}")
        with keyboard.pressed(Key.shift):
            keyboard.press(']')
            keyboard.release(']')
    elif ":" in output:
        print(":")
        with keyboard.pressed(Key.shift):
            keyboard.press(';')
            keyboard.release(';')
    elif ";" in output:
        print(";")
        keyboard.press(';')
        keyboard.release(';')
    elif "," in output:
        print(",")
        keyboard.press(',')
        keyboard.release(',')
    elif "/" in output:
        print("/")
        keyboard.press('/')
        keyboard.release('/')
    elif "." in output:
        print(".")
        keyboard.press('.')
        keyboard.release('.')
    elif "<" in output:
        print("<")
        with keyboard.pressed(Key.shift):
            keyboard.press(',')
            keyboard.release(',')
    elif ">" in output:
        print(">")
        with keyboard.pressed(Key.shift):
            keyboard.press('.')
            keyboard.release('.')
    elif "?" in output:
        print("?")
        with keyboard.pressed(Key.shift):
            keyboard.press('/')
            keyboard.release('/')
    elif "'" in output:
        print(" ' ")
        keyboard.press("\'")
        keyboard.release("\'")
    elif quotation_mark in output:
        print("quotation mark")
        keyboard.press(quotation_mark)
        keyboard.release(quotation_mark)
    elif space_sign in output:
        print("space")
        keyboard.press(Key.space)
        keyboard.release(Key.space)
    elif "|" in output:
        print("|")
        with keyboard.pressed(Key.shift):
            keyboard.press('i')
            keyboard.release('i')
    else:
        print("nothing")

def Space():
    keyboard.press(Key.space)
    keyboard.release(Key.space)

while True:
        time.sleep(1)
        im = ImageGrab.grab(bbox=(925,750,2175,835)) #adjust for your screen
        print("2")
        im.save('output.png')
        #im.show() #if you want to crash you computer, uncomment this
        input = "output.png"
        text = pytesseract.image_to_string(Image.open(input))
        text_file = open("Output.txt", "a")
        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        with open("Output.txt", "a") as text_file:
            text_file.write(text + current_time + '\n')
            #text_file.write(current_time)
        text_file.close()
        y = (len(text))
        x = 0
        while x<y:
            if x<y:
                output = text[x] #fix this problem use if or else
                Character_Detection()
                x += 1
            else:
                print("lols")
        Space()
