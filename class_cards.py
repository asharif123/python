##Blackjack class
##Create a 52 card deck, shuffle 10 times, and deal out 1 card to each player
##User can keep drawing unless if he stays, gets 21, or goes over 21
##Computer must hit under 16 and stay at 17 or above
##If user gets 21, gets a higher score than the computer without going over 21, user wins!
##if computer gets 21, gets a higher score than user without exceeding 21, computer wins!

import random
from time import sleep
card_value = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
##use .items() to split each case under key and pair!
card_value = card_value.items()
print ("Welcome to Blackjack!\n")
print ("Dealing out the cards..\n")
sleep(2)

class Blackjack():
 
    def __init__(self):
        self.ranks = ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]
        self.suits = ["Diamonds","Hearts","Clubs","Spades"]
        self.deck = []
        self.player_hand = []
        self.computer_hand = []
        self.points = 0
        self.computer_points = 0
        
    def card_deck(self):       
        for rank in self.ranks:
            for suit in self.suits:
                card = rank + " " + suit
                self.deck.append(card)

    def shuffle_deck(self):
        num = 0
#shuffle the deck 10 times!
        while num < 10:
            random.shuffle(self.deck)
            num = num + 1
       
    def play_game(self):
#each player is dealt one card from the deck!
        num = 0
        while num < 1:
            self.player_hand.append(self.deck.pop(0))
            self.computer_hand.append(self.deck.pop(0))
            num = num + 1
        print ("This is your hand: " + str(self.player_hand) + "\n")
        sleep(2)
        print ("This is the house's hand: " + str(self.computer_hand) + "\n")
        print ("The house must hit at 16 and everything below, and stay at or above 17!\n")
        sleep(1)
    

#########PLAYING BLACKJACK VS. COMPUTER!#################  
        #calculate points from first card in your hand!!
        for sign, value in card_value:
            for card in self.player_hand:
                if (card[0] == sign):
                    self.points = self.points + value
        print ("You have a total of %s points.\n" %(self.points))

        #calculate points in computer's hand!
        for sign_2, value_2 in card_value:
            for card in self.computer_hand:
                if (card[0]) == sign_2:
                    self.computer_points = self.computer_points + value_2
        print ("The computer has a total of %s points.\n" %(self.computer_points))
        
#######################COMPUTER HAS TO STAY AT 17 OR ABOVE AND HIT AT OR BELOW 16!!##########################################
        while True:
            decision = input("Enter Y/y to hit, N/n to stay: ").upper()
            if (decision == "Y"):
                self.player_hand.append(self.deck.pop(0))
                print ("This is your hand: " + str(self.player_hand) + "\n")
                for card in self.player_hand:
                    card = card.split(' ')

                for sign, value in card_value:
                    if (card[0]) == sign:
                        self.points = self.points + value
                    if (card[0] == sign) and (card[0] == "A"):
                        while True:
                            value = int(input('\nDo you want A to equal 1 or 11? '))
                            if value == 1:
                                self.points = (self.points + value) - 1
                                break
                            elif value == 11:
                                self.points = (self.points + value) - 1
                                break
                print ("You now have a total of %s points.\n" %(self.points))

                if (self.points > 21):
                    break
                elif (self.points == 21):
                     break           
            elif (decision == "N"):
                print ("\nYou're staying at %s.\n" %(self.points))
                break
                

#computer must hit under 16 and stay at 17 or above
#The house starts drawing when user quits or busts!
        while True:
            print ("The house is drawing..")
            sleep(2)
            self.computer_hand.append(self.deck.pop(0))
            print ("The house's hand: %s\n" %(self.computer_hand))

            for card in self.computer_hand:
                card = card.split(' ')
            for sign, value in card_value:
                if (card[0]) == sign:
                    self.computer_points = self.computer_points + value

            if (self.computer_points > 21):
                print ("The house hit over 21, you win!\n")
                break

            elif (self.points == 21):
                print ("You hit blackjack, you win!\n")
                break

            elif ((self.computer_points >= 17) and (self.computer_points > self.points) and (self.computer_points < 22)):
                print ("YOU LOSE, computer got a higher score than you!\n")
                break
            
            elif (self.points > 21):
                print ("You went over 21, YOU LOSE!\n")
                break
            
            elif ((self.computer_points >= 17) and (self.computer_points < self.points)):
                print ("You win, you got a higher score than the computer!\n")
                break

            elif ((self.points) == (self.computer_points)) and (self.points != 21):
                 print ("TIE GAME!\n")
                 break
            
        
        decision = input("Press Y to play again or N to quit: ").upper()
        if (decision == 'Y'):
            print ("New game..\n")
            sleep(2)
            playing_cards = Blackjack()
            playing_cards.card_deck()
            playing_cards.shuffle_deck()
            playing_cards.play_game()
                                
        elif (decision == 'N'):
            print ("Exiting the game!\n")
            sleep(1)
            #break
            
playing_cards = Blackjack()
playing_cards.card_deck()
playing_cards.shuffle_deck()
playing_cards.play_game()






        




                     

    
