#Pig latin translator
#Take one word, take first letter of that word, put it at end, and add ay!

pyg = 'ay'

original = str(raw_input('Enter a word: '))

#.isalpha is used to ensure input is all letters
word = ((original[1:]) + original[0] + 'ay')
print word
