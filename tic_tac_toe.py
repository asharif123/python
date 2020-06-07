###Create a 3 by 3 tic tac toe game!
#If user selects X, computer selects O and vice versa
#Game ends User wins if he gets 3 in a row before computer
#Computer wins if it gets 3 in a row and game ends
#User has option to play another game or to quit!

import random
from time import sleep
print ("Welcome to Tic Tac Toe!\n")
sleep(2)
##Create a Tic Tac Toe game with 9 empty areas!
##Ex: top_right square is whitespance, so is top mid, top l, middle and bottom rows

#function takes all the keys in theBoard and turns them into a clean boardgame!
#function adds the whitespace values from each key to a '|'


def print_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('_____')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('_____')
    print(board[6] + '|' + board[7] + '|' + board[8])

theBoard = ['0','1','2','3','4','5','6','7','8']
print_board(theBoard)

#function lets user select a letter and start the game!
def play_game():
    while True:
#make theBoard a global variable so that it can be used outside of the print_board() function!
        global theBoard
        #user selects whether to use 'X' or 'O', other selections are invalid!!        
        letters = ["X","O"]
        user_choice = str(input("\nPlease select X or O: ")).upper()
        if (user_choice == "X"):
            value = letters.index("O")
            computer_choice = letters[value]
            print ("\nYou have chosen", user_choice + "." + "\n")
            sleep(1)
            print ("\nComputer will be using", computer_choice + "." +"\n")
            sleep(1)
            break

        elif (user_choice == "O"):
            value = letters.index("X")
            computer_choice = letters[value]
            print ("You have chosen", user_choice + "." + "\n")
            sleep(1)
            print ("Computer will be using", computer_choice + "." +"\n")
            sleep(1)
            break
        else:
            print ("Invalid input!\n")
    print ("Starting the game..\n")
    sleep(2)

#Computer makes the first move!

    computer_move = random.randint(0,8)
    print ("Computer is selecting a spot..\n")
    sleep(2)
    theBoard[computer_move] = computer_choice
    print_board(theBoard)
    sleep(1)

####User has up to 4 chances to get 3 in a row!!
####If there is no winner in 4 turns, it ends as 'Cat's game!'!
    i = 0
    while i < 4:
#User must select a number from 0 to 8 only!!
        while True:
            player_move = int(input("\nSelect a numbered spot: "))
            if player_move not in range(0,9):
                print ("Select a number from 0 to 8!\n")
            else:
                break

##code checks if spot on the tic tac toe board has been occupied or not!

        def check_spot(user_choice):
            if (theBoard[user_choice] == 'X') or (theBoard[user_choice] == 'O'):
                print ("\nSpot has been taken!\n")
        check_spot(player_move)
##user can only select empty spots, checks if spot doesn't have an X or O!!
        if (theBoard[player_move] != user_choice) and (theBoard[player_move] != computer_choice):
            theBoard[player_move] = user_choice
            print_board(theBoard)
            sleep(1)
            print ("\nComputer is selecting...\n")
            sleep(1)
#each turn ends after user selects a spot on the board! computer selects first!
            i = i + 1
    #create a nested while True loop where we force computer to select empty spot!
    #while True forces computer to run an infinite loop until it finds an empty spot!
    #without the while loop, the computer may select an occupied spot, we want it to keep looping until an empty spot is found!
            while True:
                computer_move = random.randint(0,8)
                if ((theBoard[computer_move] != 'X') and (theBoard[computer_move] != 'O')):
                    theBoard[computer_move] = computer_choice
                    print_board(theBoard)
                    break
   
#play_game()
    #########################cases where user wins the game!#################################################
            
        if ((theBoard[0] == user_choice) and (theBoard[1] == user_choice) and (theBoard[2] == user_choice)):
            print ("\nYOU WIN THE GAME!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
#if user wishes to play another game, reset the board!
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break


        elif ((theBoard[3] == user_choice) and (theBoard[4] == user_choice) and (theBoard[5] == user_choice)):
            print ("\nYOU WIN THE GAME!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
        #if user wishes to play another game, reset the board11
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break
            
        elif ((theBoard[6] == user_choice) and (theBoard[7] == user_choice) and (theBoard[8] == user_choice)):
            print ("\nYOU WIN THE GAME!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
        #if user wishes to play another game, reset the board11
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break

        elif ((theBoard[0] == user_choice) and (theBoard[4] == user_choice) and (theBoard[8] == user_choice)):
            print ("\nYOU WIN THE GAME!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
        #if user wishes to play another game, reset the board11
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break

        elif ((theBoard[2] == user_choice) and (theBoard[4] == user_choice) and (theBoard[6] == user_choice)):
            print ("\nYOU WIN THE GAME!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
        #if user wishes to play another game, reset the board11
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break

        elif ((theBoard[0] == user_choice) and (theBoard[3] == user_choice) and (theBoard[6] == user_choice)):
            print ("\nYOU WIN THE GAME!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
        #if user wishes to play another game, reset the board11
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break


        elif ((theBoard[1] == user_choice) and (theBoard[4] == user_choice) and (theBoard[7] == user_choice)):
            print ("\nYOU WIN THE GAME!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
        #if user wishes to play another game, reset the board11
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break


        elif ((theBoard[2] == user_choice) and (theBoard[5] == user_choice) and (theBoard[8] == user_choice)):
            print ("\nYOU WIN THE GAME!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
        #if user wishes to play another game, reset the board11
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break

        #########################Cases where computer wins the game!!##############################################################################3
        elif ((theBoard[0] == computer_choice) and (theBoard[1] == computer_choice) and (theBoard[2] == computer_choice)):
            print ("\nSORRY, YOU LOST!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
        #if user wishes to play another game, reset the board11
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break


        elif ((theBoard[3] == computer_choice) and (theBoard[4] == computer_choice) and (theBoard[5] == computer_choice)):
            print ("\nSORRY, YOU LOST!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
        #if user wishes to play another game, reset the board11
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break

                        
        elif ((theBoard[6] == computer_choice) and (theBoard[7] == computer_choice) and (theBoard[8] == computer_choice)):
            print ("\nSORRY, YOU LOST!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
        #if user wishes to play another game, reset the board11
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break

                
        elif ((theBoard[0] == computer_choice) and (theBoard[4] == computer_choice) and (theBoard[8] == computer_choice)):
            print ("\nSORRY, YOU LOST!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
        #if user wishes to play another game, reset the board11
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break


        elif ((theBoard[2] == computer_choice) and (theBoard[4] == computer_choice) and (theBoard[6] == computer_choice)):
            print ("\nSORRY, YOU LOST!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
        #if user wishes to play another game, reset the board11
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break

        elif ((theBoard[0] == computer_choice) and (theBoard[3] == computer_choice) and (theBoard[6] == computer_choice)):
            print ("\nSORRY, YOU LOST!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
        #if user wishes to play another game, reset the board11
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break

        elif ((theBoard[1] == computer_choice) and (theBoard[4] == computer_choice) and (theBoard[7] == computer_choice)):
            print ("\nSORRY, YOU LOST!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
        #if user wishes to play another game, reset the board11
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break

        elif ((theBoard[2] == computer_choice) and (theBoard[5] == computer_choice) and (theBoard[8] == computer_choice)):
            print ("\nSORRY, YOU LOST!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
        #if user wishes to play another game, reset the board11
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break


        elif (i == 4):
            print ("\nCat's game!\n")
            print_board(theBoard)
            decision = input("\nPress Y to play again or N to quit: ").upper()
        #if user wishes to play another game, reset the board11
            if (decision == "Y"):
                print ("Resetting the board..\n")
                sleep(2)
                theBoard = ['0','1','2','3','4','5','6','7','8']
                print_board(theBoard) 
                play_game()
            elif (decision == "N"):
                break
                print ("Exiting the game..\n")
                break
        #if user selects occupied spot, program will remind user that it is taken!!
        #call the 'check_spot' function for player_move

play_game()

      
            
            
                
                    

    
    
    
    




 

    
    




