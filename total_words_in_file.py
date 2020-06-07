##Count words in a file
import os
os.chdir('C:/Users/Awad/Documents')
def total_words_in_file(filename):
    try:
        with open(filename) as contents:
            file_read = contents.readlines()
    except FileNotFoundError:
        print ('DNE!\n')
    else:
        total = 0
        for line in file_read:
            words = line.split(' ')
            for word in words:
                total = total + 1
        print ('Total words in file: ' + str(total) + '\n')

