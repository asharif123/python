###Takes a word that exists in a sentence and replaces with asterisks!
##2 arguments: text is sentence and word is replaces by asterisks in sentence
##To replace word in text, split it and the use ' '.join
def censor(sentence, word):
##    sentence = sentence.split()
##    print sentence
##    print sentence
    for letter in sentence:
        if word == letter:
            sentence = sentence.replace(word, ('*'*len(letter)))
        print sentence
            
##            sentence = ' '.join(sentence)

            
