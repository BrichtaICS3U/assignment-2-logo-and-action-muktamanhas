# ICS3U
# Assignment 2: Action
# Mukta

# adapted from http://www.101computing.net/getting-started-with-pygame/
# background image from https://www.nikonusa.com/en/learn-and-explore/a/tips-and-techniques/moose-peterson-how-to-photograph-winter-landscapes.html
# background music (get you - daniel caesar) https://www.youtube.com/watch?v=sweE862aOGc
# used tutorials from http://www.101computing.net/pygame-how-tos/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame, random
from snow import Snowflake
pygame.init()

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('soundtrack.mp3')
pygame.mixer.music.play(-1) 

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

background = pygame.image.load("background.png")
speed = 10

# Set the screen size
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Animation")

all_sprites_list = pygame.sprite.Group()

playerSnowflake = Snowflake(WHITE, 20, 20, 10)
playerSnowflake.rect.x = 200
playerSnowflake.rect.y = 100

all_sprites_list.add(playerSnowflake)

for i in range (75):
    obj = Snowflake(WHITE, 20, 20, 10)
    obj.rect.x= random.randint(0,400)
    obj.rect.y= random.randint(-500 ,0)
    all_sprites_list.add(obj)

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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            carryOn = False
        

    # --- Game logic goes here
    # There should be none for a static image
    for snow in all_sprites_list:
        snow.moveForward(speed)
        if snow.rect.y > SCREENHEIGHT:
            snow.rect.y = -200

    # --- Draw code goes here
    all_sprites_list.update()
    
    # Clear the screen to white
    screen.blit(background, (0, 0))
    
    # Queue different shapes and lines to be drawn
    # pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    all_sprites_list.draw(screen)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
