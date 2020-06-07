##caesar cipher function where user enters shifting amount
##each letter is shifted by amount of shift
##'A' to 'Z' outputs codes 65 to 90
##'a' to 'z' outputs codes 97 to 122!
def caesar_cipher_shift(text,shift):
    if shift not in range(1,26):
        print ("Please enter a shift from 1 to 25!\n")
    else:
        cipher = ""
        for letter in text:
            if letter.isalpha():
                code = ord(letter)
#if letter is 'z' and shift entered is 1, convert that letter to 'a'
                if letter.islower() and shift == 1 and code+shift > ord('z'):
                    code = ord('a')
                    shifted_letter = code
#Use 'chr()' to convert code point back to letter!
                    cipher += chr(shifted_letter)
#if letter is 'Z' and shift entered is 1, convert that letter to 'A'
                elif letter.isupper() and shift == 1 and code+shift > ord('Z'):
                    code = ord('A')
                    shifted_letter = code
                    cipher += chr(shifted_letter)
#if letter is 'A' and shift > 1, convert that letter to letter corresponding..
#to number of shifts! ensure that only letters are entered
#'-25+(shift-1)' formula is used to ensure that only letter is shifted to letter
#and not to puncuation marks!
                elif letter.isupper() and shift > 1 and code+shift > ord('Z'):
                    code = ord(letter)-25+(shift-1)
                    shifted_letter = code
                    cipher += chr(shifted_letter)
                elif letter.islower() and shift > 1 and code+shift > ord('z'):
                    code = ord(letter)-25+(shift-1)
                    shifted_letter = code
                    cipher += chr(shifted_letter)
                else:
                    shifted_letter = code+shift
                    cipher += chr(shifted_letter)
##Add in letters that are NOT letters as-is!
            else:
                cipher += letter
#print out the new caesar cipher letters after shifting
        return cipher
print (caesar_cipher_shift("abcxyzABCxyz 123",2))
print (caesar_cipher_shift('The die is cast',25))              
