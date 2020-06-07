def get_list(names):
    for name in names:
        print ("Hello my name is " + name.title() + ".\n")
#call get_list on usernames

get_list(["Awad", "Urooj", "Fari"])


##person = {}
##while True:
##    first_name = input("Enter your first name: ")
##    if (first_name == 'q'):
##        print "Exiting the program!"
##        break
##
##    last_name = input("Enter your last name: ")
##    if (last_name == 'q'):
##        print "exiting the program!"
##        break
##
##    age = (input("Your age: "))
##
##    person['first_name'] = first_name
##    person['last_name'] = last_name
##    person['age'] = age
##    if age == '':
##        person['age'] = ''
##
##    print person

#If using return, you need to reassign function to a variable to call it
title = {}
##def make_album(artist,album):
##    title['artist'] = artist
##    title['album'] = album
##    return title
##
##singers = make_album('Michael Jackson', 'Beat It')
##print singers

title = {}
while True:
    artist = str(input("Please enter an artist: "))
    album = str(input("Enter an album: \n"))
    if (artist == 'q') or (album == 'q'):
      print (title)
      break
    else:
        title['artist'] = artist
        title['album'] = album
        print (title)




    
