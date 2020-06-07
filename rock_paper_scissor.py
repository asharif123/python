###Create a Rock, Paper, and Scissors game
##User selects R, P or S and computer also selects R, P or S
##Rock beats scissor, scissor beats paper, and paper beats rock
from random import randint
from time import sleep

#User selects rock, paper or scissor
options = ["R", "P", "S"]
print (options.index(options))

loser_message = "You lost!"
winner_message = "You win!"
