import os

def search_word(search_word):
    os.chdir('C:/Users/Awad/Documents/')
    try:
        with open('reading_book.txt') as read_file:
            contents = read_file.readlines()
            total = 0
            for lines in contents:
                line = lines.split(' ')
                for word in line:
                    if word == search_word:
                        total = total + 1

    except FileNotFoundError:
        print ('THAT FILE DOES NOT EXIST!\n')

    else:
        print ("The word " + str(search_word) + " appears " + str(total) + " times in the reading_book.txt file.\n")
        
