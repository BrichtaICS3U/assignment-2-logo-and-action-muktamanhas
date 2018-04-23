# ICS3U
# Assignment 2: iTunes Logo
# Mukta

# adapted from http://www.101computing.net/getting-started-with-pygame/
# reference image https://www.sketchappsources.com/resources/source-image/apple_itune_store.png

#Import the pygame library and initialise the game engine
import pygame
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (227, 66, 229)

# Set the screen size (please don't change this)
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Logo")

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here
    # Clear the screen to white
    screen.fill(PURPLE)

    # Queue different shapes and lines to be drawn
    pygame.draw.ellipse(screen, WHITE, [25, 25, 350, 350], 13) #large circle
    pygame.draw.line(screen, WHITE, [154, 115], [154, 265], 10) #left line
    pygame.draw.line(screen, WHITE, [265, 120], [265, 250], 10) #right line
    pygame.draw.line(screen, WHITE, [150, 125], [270, 100], 55) #top line
    pygame.draw.ellipse(screen, WHITE, [96, 246, 65, 45], 0) #circle left
    pygame.draw.ellipse(screen, WHITE, [208, 225, 65, 45], 0) #circle right

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
