#####Sudoku game
##Create 9 by 9 board with each having 9 mini-squares (3 by 3 tiles)
##user enters 9-digit numbers 9 times
##each of the nine digits are outputted in each row and column of game_board
##Each row and column must have digits 0 to 9
##Each 3 by 3 grid must have digits 0 to 9


game_board = [['[]']*9 for i in range(9)]
def print_board(board):
    for row in board:
        print (' '.join(row))

def fill_sudoku_board():
    i = 0
    while i < 9:
        nine_digits = int(input("\nPlease enter a 9-digit number: "))
        if len(str(nine_digits)) != 9:
            print ("\nPlease enter a nine digit number!\n")
      
        elif (str(nine_digits).find('0') != -1):
            print ("All digits must be between 1 to 9!\n")
      
        elif (nine_digits) < 0:
            print ("Please enter a number greater than 0!\n")
#take each digit of 9 digit number and fill each row of the board
        nine_digits = list(str(nine_digits))
        for j in range(9):
            game_board[i][j] = (nine_digits[j])
        i += 1
##check all rows have digits 1 to 9 and no repeating digits!
#return True if there are repeating digits in any rows!
#return means immediately return a value and terminate the function!
def repeating_digits_in_rows():
    for i in range(9):
        for j in range(1,10):
            if str(j) not in game_board[i]:
                return True

##take each column, turn it to horizontal list, iterate thru each column and
##confirm only digits 1 to 9 exist in each column and no repeating!
def repeating_digits_in_columns():
    columns_list = [[game_board[i][j] for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(1,10):
            if str(j) not in columns_list[i]:
                return True
##take each of the 9 3 by 3 grids, add to horizontal list, iterate thru each and
##confirm if digits 1 to 9 exist in each list without repeating!
            
##first_grid = 00,01,02,10,11,12,20,21,22
##second_grid = 03,04,05,13,14,15,23,24,25
##third_grid = 06,07,08,16,17,18,26,27,28
##fourth_grid = 30,31,32,40,41,42,50,51,52
##fifth_grid = 33,34,35,43,44,45,53,54,55
##sixth_grid = 36,37,38,46,47,48,56,57,58
##seventh_grid = 60,61,62,70,71,72,80,81,82
##eighth_grid = 63,64,65,73,74,75,83,84,85
##ninth_grid = 66,67,68,76,77,78,86,87,88
def repeating_digits_in_grids():
    total_grids = {'first_grid': [game_board[i][j] for i in range(3) for j in range(3)],
                   'second_grid': [game_board[i][j] for i in range(3) for j in range(3,6)],
                    'third_grid': [game_board[i][j] for i in range(3) for j in range(6,9)],
                   'fourth_grid': [game_board[i][j] for i in range(3,6) for j in range(3)],
                   'fifth_grid': [game_board[i][j] for i in range(3,6) for j in range(3,6)],
                   'sixth_grid': [game_board[i][j] for i in range(3,6) for j in range(6,9)],
                   'seventh_grid': [game_board[i][j] for i in range(6,9) for j in range(3)],
                   'eighth_grid': [game_board[i][j] for i in range(6,9) for j in range(3,6)],
                   'ninth_grid': [game_board[i][j] for i in range(6,9) for j in range(6,9)]}
    for grid in total_grids:
        for digit in range(1,10):
            if str(digit) not in total_grids[grid]:
                return True

fill_sudoku_board()
print_board(game_board)
##Sudoku is valid if no digits 1 to 9 exist in each row, column, and 3 by 3 grid
if not repeating_digits_in_rows() and not repeating_digits_in_columns() and not repeating_digits_in_grids():
    print ("Yes")
elif repeating_digits_in_rows() or repeating_digits_in_columns() or repeating_digits_in_grids():
    print ("No")
    

