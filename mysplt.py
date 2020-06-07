def mysplit(strng):
#user enters a string and converts it to list
#if strng is empty or has spaces, return empty list
#create new word and new empty list
#iterate thru each letter in strng and add characters that are not spaced.
#if space is encountered, add word to new list and reset new word
#start new iteration adding new letters
    empty_list = []
    word = ""
    if strng.isspace() or len(strng) == 0:
        return empty_list
    strng = strng.strip()
    strng = strng + ' '
    for letter in strng:
        word += letter
        if letter.isspace():
            empty_list.append(word.strip())
            word = ""
    return empty_list
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))


