
#Takes a string and prints it in reverse!
def reverse(text):
  text = str(text)
  return text[::-1]

##### Function takes a sentence and strips out vowels from it! #####
def anti_vowel(sentence):
  #reassign text to sentence since text is original input and you don't change
  #original input!!
  
  for vowel in "aeiouAEIOU":
  #searches for vowel in inputted text and removes it!
    if vowel in sentence:
#if vowel exists in inputted sentence, remove that vowerl with empty space!
      sentence = sentence.replace(vowel, "")
    #count = count + 1
  print sentence
##print anti_vowel('Hey Hey Hey in there!')

def censor(sentence, word):
  if word in sentence:
      sentence = sentence.replace(word, "*"*len(word))
  print sentence

  
