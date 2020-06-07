# IBAN Validator
##NOTE: CANNOT ITERATE THRU A STRING!
iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')
if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    if not iban.isalnum():
        print ("Invalid IBAN entry!")
    elif not iban[0:2].isalpha() or not iban[2:4].isdigit():
        print ("Invalid IBAN entry!")
    else:
        iban = iban.upper()
        iban = list(iban)
        iban = iban + iban[0:4]
        iban[0:4] = [''*4]
        iban = ''.join(iban)
        for letter in iban:
            if letter.isalpha():
                code = ord(letter)-55
                iban = iban.replace(letter,str(code))
iban = int(iban)
if (iban % 97) == 1:
    print ("IBAN number is valid!")
else:
    print ("IBAN number is NOT valid!")


        


