

##Computer randomly selects where on the board to place enemy ship
##User guesses which position the enemy ship is located at
##If user gueeses where ship is in less than 4 guesses, user wins!
##If user fails in 4 guesses, the enemy ship is revealed!
import random
from time import sleep
print ('Welcome to Battleship!\n')
sleep(2)
##Create a 5 by 5 board battleship game!
board = []
for i in range(5):
    board.append(['0','1','2','3','4'])

#Function cleans the board up by stripping quotes and commas!
def print_board(board):
    for row in board:
        row = ' '.join(row)
        print (row)
print_board(board)

print ('The objective is to sink the enemy ship!')
sleep(1)
print ('Select a number between 0 to 4 for row and column positions of the enemy ship!\n')
print ('Starting the game..')
sleep(1)

def play_game():
    global board

#Position of enemy ship!
    players = int(input('\nEnter 1 for 1 player or 2 for 2 players: '))
    if players == 1:
        ship_row = random.randint(0,4)
        ship_col = random.randint(0,4)
#4 guesses to sink the ship!!
        i = 0
        while i < 4:
            user_row = int(input("\nPlease enter a row position: "))
            user_col = int(input("Please enter a column position: "))

            if ((user_row == ship_row) and (user_col == ship_col)):
                print ('\nCongratulations, you sank the battleship!\n')
                sleep(1)
                board[ship_row][ship_col] = 'S'
                print_board(board)
                decision = input('\nPress Y\y to play again, N or n to quit: ').upper()
                if (decision == 'Y'):
                    print ('\nRestarting game..\n')
                    sleep(2)
                    board = []
                    for i in range(5):
                        board.append(['0','1','2','3','4'])
                    print_board(board)
                    play_game()
                elif (decision == 'N'):
                    print ('Exiting the game..\n')
                    sleep(1)
                    break

            elif (board[user_row][user_col] == '0') or (board[user_row][user_col] == '1') or (board[user_row][user_col] == '2') or (board[user_row][user_col] == '3') or (board[user_row][user_col] == '4'):
                print ('Sorry, try again!\n')
                board[user_row][user_col] = 'X'
                print_board(board)
                i = i + 1

            elif ((board[user_row][user_col]) == 'X'):
                print ('You guessed that one already!\n')
                print_board(board)

            elif ((user_row < 0) or (user_row > 4) or (user_col < 0) or (user_col > 4)):
                print ('Invalid entry! Please enter a number between 0 to 4!\n')
                print_board(board)
#the game is over if player is unable to guess correct location in 4 guesses!
            if (i == 4) and ((user_row != ship_row) or (user_col != ship_col)):
                print ('\nGAME OVER!\n')
                print ('The enemy ship is located on position = ' + '{' + str(ship_row) + ',' + str(ship_col) + ')' + "." + '\n')
                sleep(2)
                board[ship_row][ship_col] = 'S'
                print_board(board)
                decision = input('\nPress Y\y to play again, N or n to quit: ').upper()
                if (decision == 'Y'):
                    print ('\nRestarting game..\n')
                    sleep(2)
                    board = []
                    for i in range(5):
                        board.append(['0','1','2','3','4'])
                    print_board(board)
                    play_game()
                elif (decision == 'N'):
                    print ('Exiting the game..\n')
                    sleep(1)
                    break
#play_game()
#if number of players is equal to 2!
    elif players == 2:
        board = []
        for i in range(5):
            board.append(['0','1','2','3','4'])
        print_board(board)

        ship_row = random.randint(0,4)
        ship_col = random.randint(0,4)
        print ('Player 1 is X, Player 2 is C.\n')
        sleep(2)
        print('Player 1 (P1) goes first, starting game..')
        sleep(2)
        i = 0
        while i < 4:
#player 1's
            p1_row = int(input('\nP1 enter a row position: '))
            p1_col = int(input('P1 enter a col position: '))
#player 2's turn
            p2_row = int(input('\nP2 enter a row position: '))
            p2_col = int(input('P2 enter a col position: '))

#player 1 wins if he sinks the ship before 4 turns!!

            if (p1_row == ship_row) and (p1_col == ship_col):
                print ('\nPlayer 1 WINS!\n')
                board[p1_row][p1_col] = 'S'
                print_board(board)
                decision = input('\nPress Y\y to play again, N or n to quit: ').upper()
                if (decision == 'Y'):
                    board = []
                    for i in range(5):
                        board.append(['0','1','2','3','4'])
                    print_board(board)
                    play_game()
                elif (decision == 'N'):
                    print ('Exiting the game..\n')
                    sleep(1)
                    break

            elif (p2_row == ship_row) and (p2_col == ship_col):
                print ('\nPlayer 2 WINS!\n')
                board[p2_row][p2_col] = 'S'
                print_board(board)
                decision = input('\nPress Y\y to play again, N or n to quit: ').upper()
                if (decision == 'Y'):
                    board = []
                    for i in range(5):
                        board.append(['0','1','2','3','4'])
                    print_board(board)
                    play_game()
                elif (decision == 'N'):
                    print ('Exiting the game..\n')
                    sleep(1)
                    break

            elif ((p1_row == p2_row) and (p1_col == p2_col)):
                print ('\nPlayer 2 cannot select same coordinates as player 1! Both players must select again!\n')
                print_board(board)
#If p1 or p2 selects occupied spot, both players must reselect coordinates!!
#This code needs to be put before the 'Sorry try again' code so that turns will not increment until both players select unoccupied spots!!
                
            elif ((board[p1_row][p1_col] == 'X') or (board[p1_row][p1_col] == 'C') or (board[p2_row][p2_col] == 'X') or (board[p2_row][p2_col] == 'C')):
                print ('\nSpot has been taken! Both players must reselect!\n')
                print_board(board)

            elif ((board[p1_row][p1_col] != 'X') or (board[p1_row][p1_col] != 'C') or (board[p2_row][p2_col] != 'X') or (board[p2_row][p2_col] != 'C')):
                print ('Sorry, try again!\n')
                board[p1_row][p1_col] = 'X'
                board[p2_row][p2_col] = 'C'
                sleep(1)
                print_board(board)
                i = i + 1
            
            if (i == 4) and ((p1_row != ship_row) or (p1_col != ship_col)) and ((p2_row != ship_row) or (p2_col != ship_col)):
                print ('\nGAME OVER!\n')
                print ('The enemy ship is located on position = ' + '{' + str(ship_row) + ',' + str(ship_col) + ')' + "." + '\n')
                sleep(2)
                board[ship_row][ship_col] = 'S'
                print_board(board)
                decision = input('\nPress Y\y to play again, N or n to quit: ').upper()
                if (decision == 'Y'):
                    print ('\nRestarting game..\n')
                    sleep(2)
                    board = []
                    for i in range(5):
                        board.append(['0','1','2','3','4'])
                    print_board(board)
                    play_game()
                elif (decision == 'N'):
                    print ('Exiting the game..\n')
                    sleep(1)
                    break
play_game()
            
       

