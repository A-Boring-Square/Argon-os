import pygame
from sys import exit
import os

# initializes pygame
pygame.init()

# sets the screen size and opens the screen
screensize = pygame.display.set_mode((800,400))

# set up the clock
clock = pygame.time.Clock()

# will run the code repetedly intel the statment is ≠ to true
while True:
    
    # exits the window when X button is pressed
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # draw all are elements
    # update everyting
    pygame.display.update()
    
    # sets the max frame rate to 60fps
    clock.tick(60)