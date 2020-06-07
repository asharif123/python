##Caesar Cipher program
##User enter a text and replaces with Caesar equivaluent
##Ex: 'A' is 'B', 'B' is 'C', 'C' is 'D', etc..
##program skips over non-letters
##if 'Z' is entered, 'Z' becomes 'A'

#code points for capital letters A thru Z (ex: ord('A')):
#Note: ord() returns unicode of string that is of length 1
#A - 65
#B - 66
#C - 67
#D - 68
#E - 69
#F - 70
#G - 71
#H - 72
##etc.., Z - 90

def caesar_cipher(text):
    text = text.upper()
    cipher = ""
    for letter in text:
        if not letter.isalpha():
            continue
        code = ord(letter)+1
        if letter == 'Z':
            code = ord('A')
        cipher += chr(code)
    return cipher
print (caesar_cipher('zyxabc'))
##convert caesar leters to regular alphabets
##Ex: 'Z' is 'y', 'Y' is 'X', 'X' is 'W', 'C' is 'B', 'B' is 'A', etc...
##if 'A', 'A' becomes 'Z'

def decode_caesar(cipher):
    text = ""
    cipher = cipher.upper()
    for char in cipher:
        if not char.isalpha():
            continue
        code = ord(char)-1
        if char == 'A':
            code = ord('Z')
        text += chr(code)
    return text

print (decode_caesar('ZYXAb'))
