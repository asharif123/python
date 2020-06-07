##count total words in each individual multiple file
import os
#Navigate to directory containing .txt files!
os.chdir('C:/Users/Awad/Documents')
print (os.getcwd())

# *files ensures you can input multiple files!
def read_multiple_files(*files):
    try:
        total = 0
#open one file at a time and read contents from that file
        for file in files:
            with open(file) as filename:
                read_file = filename.readlines()
#first read each line and then split each line in individual words!
                for line in read_file:
                    words = line.split(' ')
                    for word in words:
                        total = total + 1
            print ('Total words in ' + str(file) + ' file = ' + str(total) + '\n')
#Reset the total to 0 to ensure you don't add words from previous text files!
            total = 0
    except FileNotFoundError:
        print (str(file) + ' does not exist!\n')


