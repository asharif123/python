##Create an alien invasion game!
##Use sys to exit the game!
##Respond to user_input, and load the ship image!

import sys
import pygame
from class_settings import Settings
def run_game():
##Initializes background settings that python needs to work!
    pygame.init()
##set the screen resolution and resolution of game window using a tuple!
##call the 'Settings' class to access the height, width of screen, and bcg color!
    screen_settings = Settings()
    screen = pygame.display.set_mode((screen_settings.height,screen_settings.width))
##set the name of the game you're playing!
    title = pygame.display.set_caption("Alien Invasion")

#use hexadecimals to set the background color
#use = amounts of red, green, and blue to make grey color!
#fill the entired screen created using pygame.display.set_mode!
    screen.fill(screen_settings.bcg_color)

####set all the events in a while True loop!
####an event is an action perfomed by a user (clicking mouse, etc.)
####write a while loop to listen to an event sent by the user in for loop!
####access events detected by pygame
##    while True:
###access all the events in pygame.event.get()
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT():
###exit the game!
##                sys.exit()

###command makes the most recently drawn screen visibile!
    pygame.display.flip()

run_game()


