from random import randrange, randint
from time import sleep

def DisplayBoard(board):
    # the function creates a board from scratch!
    print ('+-------+-------+-------+')
    print ('|       |       |       |')
    print ('|   '+str(board[1])+'   |'+'   '+str(board[2])+'   |''   '+str(board[3])+'   |')
    print ('|       |       |       |')
    print ('+-------+-------+-------+')
    print ('|       |       |       |')
    print ('|   '+str(board[4])+'   |'+'   '+str(board[5])+'   |''   '+str(board[6])+'   |')
    print ('|       |       |       |')
    print ('+-------+-------+-------+')
    print ('|       |       |       |')
    print ('|   '+str(board[7])+'   |'+'   '+str(board[8])+'   |''   '+str(board[9])+'   |')
    print ('|       |       |       |')
    print ('+-------+-------+-------+')

def inputLetter():
    letters = ['X','O']
    global user_input
    global computer_input
    while True:
        user_input = input("\nDo you want to be X or O: ").upper()
        if user_input == "X":
            print ("You selected X.\n")
            sleep(1)
            computer_input = letters[letters.index("O")]
            print ("Computer will play as O.\n")
            sleep(1)
            print ("Starting game...")
            sleep(2)
            break
        elif user_input == "O":
            print ("You selected O.\n")
            sleep(1)
            computer_input = letters[letters.index("X")]
            print ("Computer will play as X.\n")
            sleep(1)
            print ("Starting game...\n")
            sleep(2)
            break
        else:
            print ("Invalid input!\n")


def PlayerMove(board):
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
    while True:
        global user_move
        user_move = int(input("\nEnter a digit from 1 to 9: "))
        if ((user_move < 1) or (user_move > 9)):
            print ("Select a number from 1 to 9!\n")
        elif (board[user_move] == "X") or (board[user_move] == "O"):
            print ("Space is taken!\n")
        elif (type(user_move) != int):
            print ("Invalid input!\n")
        else:
            board[user_move] = user_input
            break

def VictoryFor(board, sign):
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
    if ((board[1] == sign) and (board[2] == sign) and (board[3] == sign) or 
    (board[4] == sign) and (board[5] == sign) and (board[6] == sign) or
    (board[7] == sign) and (board[8] == sign) and (board[9] == sign) or
    (board[1] == sign) and (board[5] == sign) and (board[9] == sign) or
    (board[3] == sign) and (board[5] == sign) and (board[7] == sign) or
    (board[1] == sign) and (board[4] == sign) and (board[7] == sign) or
    (board[2] == sign) and (board[5] == sign) and (board[8] == sign) or
    (board[3] == sign) and (board[6] == sign) and (board[9] == sign)):
        return True

##function that determines if there is a tie game!
def isBoardFull(board):
    total = 0
    for i in range(1,10):
        if (board[i] == "X") or (board[i] == "O"):
            total += 1
    if total == 9:
        return True

def ComputerMove(board):
# the function draws the computer's move and updates the board
    global computer
    while True:
        computer = randrange(1,10)
#computer selects a number that is not occupied!
        if (type(board[computer]) == int):
            board[computer] = computer_input
            DisplayBoard(board)
            break
#if this condition is true where board is full, break out of loop immediately
        if isBoardFull(board):
            break
        
def GameSetup():
    global board
    board = ['',1,2,3,4,5,6,7,8,9]
    DisplayBoard(board)
    inputLetter()


print ("Welcome to Tic Tac Toe!")
sleep(2)
GameSetup()
while True:
    PlayerMove(board)
    print ("Computer is selecting...")
    sleep(1)
    ComputerMove(board)
##Player wins
    if VictoryFor(board,user_input):
        print ("\nYOU WIN!\n")
        sleep(1)
        DisplayBoard(board)
        decision = input("\nEnter Y to play again, N to quit: ").upper()
        if decision == "Y":
            print ("Resetting board...")
            sleep(1)
            GameSetup()
            PlayerMove(board)
            print ("Computer is selecting...")
            sleep(1)
            ComputerMove(board)
        elif decision == "N":
            print ("\nEXITING GAME...\n")
            sleep(1)
            break
##Computer wins
    elif VictoryFor(board,computer_input):
        print ("\nSORRY, YOU LOSE!\n")
        sleep(1)
        DisplayBoard(board)
        decision = input("\nEnter Y to play again, N to quit: ").upper()
        if decision == "Y":
            print ("Resetting board...")
            sleep(1)
            GameSetup()
            PlayerMove(board)
            print ("Computer is selecting...")
            sleep(1)
            ComputerMove(board)
        elif decision == "N":
            print ("\nEXITING GAME...\n")
            sleep(1)
            break
##Cat's game condition
    elif isBoardFull(board) and not VictoryFor(board,user_input) and not VictoryFor(board,computer_input):
        print ("\nCAT'S GAME!\n")
        sleep(1)
        DisplayBoard(board)
        decision = input("\nEnter Y to play again, N to quit: ").upper()
        if decision == "Y":
            print ("Resetting board...")
            sleep(1)
            GameSetup()
            PlayerMove(board)
            print ("Computer is selecting...")
            sleep(1)
            ComputerMove(board)
        elif decision == "N":
            print ("\nEXITING GAME...\n")
            sleep(1)
            break

