from pynput.keyboard import Key, Controller
from PIL import ImageGrab
from PIL import Image
import time
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
        keyboard.press('A')
        keyboard.release('A')
    elif "B" in output:
        print("B")
        keyboard.press('B')
        keyboard.release('B')
    elif "C" in output:
        print("C")
        keyboard.press('C')
        keyboard.release('C')
    elif "D" in output:
        print("D")
        keyboard.press('D')
        keyboard.release('D')
    elif "E" in output:
        print("E")
        keyboard.press('E')
        keyboard.release('E')
    elif "F" in output:
        print("F")
        keyboard.press('F')
        keyboard.release('F')
    elif "G" in output:
        print("G")
        keyboard.press('G')
        keyboard.release('G')
    elif "H" in output:
        print("H")
        keyboard.press('H')
        keyboard.release('H')
    elif "I" in output:
        print("I")
        keyboard.press('I')
        keyboard.release('I')
    elif "J" in output:
        print("J")
        keyboard.press('J')
        keyboard.release('J')
    elif "K" in output:
        print("K")
        keyboard.press('K')
        keyboard.release('K')
    elif "L" in output:
        print("L")
        keyboard.press('L')
        keyboard.release('L')
    elif "M" in output:
        print("M")
        keyboard.press('M')
        keyboard.release('M')
    elif "N" in output:
        print("N")
        keyboard.press('N')
        keyboard.release('N')
    elif "O" in output:
        print("O")
        keyboard.press('O')
        keyboard.release('O')
    elif "P" in output:
        print("P")
        keyboard.press('P')
        keyboard.release('P')
    elif "Q" in output:
        print("Q")
        keyboard.press('Q')
        keyboard.release('Q')
    elif "R" in output:
        print("R")
        keyboard.press('R')
        keyboard.release('R')
    elif "S" in output:
        print("S")
        keyboard.press('S')
        keyboard.release('S')
    elif "T" in output:
        print("T")
        keyboard.press('T')
        keyboard.release('T')
    elif "U" in output:
        print("U")
        keyboard.press('U')
        keyboard.release('U')
    elif "V" in output:
        print("V")
        with keyboard.pressed(Key.shift):
            keyboard.press('v')
            keyboard.release('v')
    elif "W" in output:
        print("W")
        keyboard.press('W')
        keyboard.release('W')
    elif "X" in output:
        print("X")
        keyboard.press('X')
        keyboard.release('X')
    elif "Y" in output:
        print("Y")
        with keyboard.pressed(Key.shift):
            keyboard.press('y')
            keyboard.release('y')
    elif "Z" in output:
        print("Z")
        keyboard.press('Z')
        keyboard.release('Z')
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
        keyboard.press('!')
        keyboard.release('!')
    elif "@" in output:
        print("@")
        keyboard.press('@')
        keyboard.release('@')
    elif "#" in output:
        print("#")
        keyboard.press('#')
        keyboard.release('#')
    elif "$" in output:
        print("$")
        keyboard.press('$')
        keyboard.release('$')
    elif "%" in output:
        print("%")
        keyboard.press('%')
        keyboard.release('%')
    elif "^" in output:
        print("^")
        keyboard.press('^')
        keyboard.release('^')
    elif "&" in output:
        print("&")
        keyboard.press('&')
        keyboard.release('&')
    elif "*" in output:
        print("*")
        keyboard.press('*')
        keyboard.release('*')
    elif "(" in output:
        print("(")
        keyboard.press('(')
        keyboard.release('(')
    elif ")" in output:
        print(")")
        keyboard.press(')')
        keyboard.release(')')
    elif "-" in output:
        print("-")
        keyboard.press('-')
        keyboard.release('-')
    elif "_" in output:
        print("_")
        keyboard.press('_')
        keyboard.release('_')
    elif "=" in output:
        print("=")
        keyboard.press('=')
        keyboard.release('=')
    elif "+" in output:
        print("+")
        keyboard.press('+')
        keyboard.release('+')
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
        keyboard.press('{')
        keyboard.release('{')
    elif "}" in output:
        print("}")
        keyboard.press('}')
        keyboard.release('}')
    elif ":" in output:
        print(":")
        keyboard.press(':')
        keyboard.release(':')
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
        keyboard.press('<')
        keyboard.release('<')
    elif ">" in output:
        print(">")
        keyboard.press('>')
        keyboard.release('>')
    elif "?" in output:
        print("?")
        keyboard.press('?')
        keyboard.release('?')
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
    else:
        print("nothing")

while True:
    time.sleep(2)
    im = ImageGrab.grab(bbox=(925,750,2175,835)) #adjust for your screen
    print("2")
    im.save('output.png')
    #im.show() #if you want to crash you computer, uncomment this
    input = "output.png"
    text = pytesseract.image_to_string(Image.open(input))

    #add a log for all the sentences and input files

    x = 0
    while x<40:
        output = text[x] #Use a different loop, bug
        Character_Detection()
        x += 1
