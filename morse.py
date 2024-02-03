morse_dic = {
    'A':'.-', 'B':'-...', 'C':'-.-.',
    'D':'-..', 'E':'.', 'F':'..-.',
    'G':'--.', 'H':'....', 'I':'..',
    'J':'.---', 'K':'-.-', 'L':'.-..',
    'M':'--', 'N':'-.', 'O':'---',
    'P':'.--.', 'Q':'--.-', 'R':'.-.',
    'S':'...', 'T':'-', 'U':'..-',
    'V':'...-', 'W':'.--', 'X':'-..-',
    'Y':'-.--', 'Z':'--..',
    'a':'.-', 'b':'-...', 'c':'-.-.',
    'd':'-..', 'e':'.', 'f':'..-.',
    'g':'--.', 'h':'....', 'i':'..',
    'j':'.---', 'k':'-.-', 'l':'.-..',
    'm':'--', 'n':'-.', 'o':'---',
    'p':'.--.', 'q':'--.-', 'r':'.-.',
    's':'...', 't':'-', 'u':'..-',
    'v':'...-', 'w':'.--', 'x':'-..-',
    'y':'-.--', 'z':'--..',
    '0':'-----', '1':'.----', '2':'..---',
    '3':'...--', '4':'....-', '5':'.....',
    '6':'-....', '7':'--...', '8':'---..',
    '9':'----.',
    '.':'.-.-.-', ':':'---...', ';':'-.-.-.',
    '?':'..--..', '=':'-...-', '/':'-..-.',
    '!':'-.-.--', '-':'-....-', '+':'.-.-.',
    '&':'.-...', '(':'-.--.', ')':'-.--.-',
    ' ':'##'
}

def conversion_text_to_morse(text):
    print("Inter Your Text (Example: word1 word2 ...): ")
    text = input()
    char = ""
    for i in text:
        char += morse_dic[i] + " "
    return char

def conversion_morse_to_text(morse_code):
    print("Inter Your Morse Code (Example: : code1 code2 ## code3 code4 ...): ")
    morse_code = input()
    morse_code = morse_code.split(' ')
    text = ("")
    for i in morse_code:
        if i in morse_dic.values():
            text += list(morse_dic.keys())[list(morse_dic.values()).index(i)]
        else:
            text += ' '
    return text

answer = input("You Have Morse Code Or Text? m/t  ")
if answer == "t":
    text = ''
    print(conversion_text_to_morse(text))
else:
    morse_code = ''
    print(conversion_morse_to_text(morse_code))