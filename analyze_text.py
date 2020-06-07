import os
os.chdir('C:\Users\Awad\Documents')
path = os.getcwd()

def word_exist(term):
    

#print os.listdir(path)
    count = 0
    try:
        
        with open('all_letters.txt') as filename:
            read_file = filename.readlines()
            

    except FileNotFoundError:
        print ("Unable to open file!")

    else:
        
        for word in read_file:
                word = word.split()
                for value in word:
                    if (value == term):
                        count = count + 1
        print ("The word %s appears %s times." %(term, count))
                
