##class that stores and reads texts!
##user can get, read, and delete messages!

class SMS_store():

    def __init__(self):
        self.messages = []

    def add_new_arrival(self,from_number,time_arrived,text_of_SMS,viewed_status='False'):
        self.messages.append('({0}, {1}, {2}, {3})'.format(from_number,time_arrived,text_of_SMS,viewed_status))
        #print (self.messages)

    def message_count(self):
        print ("\nTotal messages in inbox: {0}\n".format((len(self.messages))))
        print (self.messages)

    def delete(self,i):
 #c = index, v = words associated with indeces!       
        for index, word in enumerate(self.messages):
            if (index == i):
#remove word associated with index inputted by user!
                self.messages.remove(word)
        print (self.messages)
                

    def get_message(self,i):
#C == index, v == word associated with indeces!
#User inputs message ahd message status is changed to "Has been viewed!"
       for index, word in enumerate((self.messages)):
           if (index == i):
#Takes each string in list from inidividual index and replaces 'False' w/ 'Viewed'
#Takes word associated with index and replaces with 'Has Been Viewed'
               read_message = word.replace('False','Has Been Viewed')
#Reassign the message that is read with 'Viewed' status to the 'self.messages'!
               self.messages[index] = read_message
       #self.messages = list(self.messages)
       print (self.messages)

    def get_unread_indexes(self):
        total = 0
        for message in self.messages:
            if 'False' in message:
                total = total + 1
        print ("\nTotal number of unread messages: " + str(total) + "." + "\n")

    def clear(self):
        num = 0
        for index, word in enumerate(self.messages):
            self.messages.pop(index)
            num = num + 1
        print (self.messages)
        #print ("Total messages in inbox: " + str(len(self.messages)) + "." + "\n")

my_inbox = SMS_store()
my_inbox.add_new_arrival('7145527522','07-02-2019 10:59 p.m.','Where are you boy?')
my_inbox.add_new_arrival('7145527522','07-02-2019 11:59 p.m.','I will be home soon!')
my_inbox.add_new_arrival('7145527522','07-02-2019 11:59 p.m.','OK!')

#my_inbox.message_count()
#my_inbox.clear()
#my_inbox.delete(1)
my_inbox.clear()
#my_inbox.get_message(0)
#my_inbox.get_unread_indexes()
#my_inbox.clear()


        
