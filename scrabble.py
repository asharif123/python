###Scrabble game!!

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
##for letter in score:
##    print letter, score[letter]

def scrabble_score(word):
    word = word.lower()
    total = 0
    for letter in score:
        if letter in word:
            total = total + score[letter]
    print total
    
    
###Takes the word inputted by user and lowercases them to match whats in score dic
##    word = word.lower()
##    total = 0
##    for character in score:
###Iterate through each letter inputted to ensure it matches each character in score
###Need to iterate thru each letter in word if same letter repeats in inputted word
##        for letter in word:
##            if (character in letter):
##                total = total + score[character]
##    print total
##    
  
