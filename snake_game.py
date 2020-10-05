#!/usr/bin/env python
# -*- coding: utf-8 -*-

# By Nikolas Petrou

# Importing the external libraries we need for this

from pygame.locals import *
from random import randint
import time
import pygame

# Function to check if the snake collides/hits something like apples or itself
# x1 and y1 represent the position of the first object
# x2 and y2 represent the position of the second object
# Returns true if the object 1 collides with object 2, in order for that to happen they objects must collide on both axes
def collision(x1,y1,x2,y2,size_snake,size_apple):
    if ((x1 + size_snake >= x2) or (x1 >= x2)) and x1 <= x2 + size_apple:
        if ((y1 >= y2) or (y1 + size_snake >= y2)) and y1 <= y2 + size_apple:
            return True
        return False

# Function to display the player's score during the game
def display_score(score):
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(score), True, (0, 0, 0))
    window.blit(text,(5,5))

playing = True # Is true while the game is not over
moveUp = moveDown = moveRight = moveLeft = move_init = False # Boolean which represent if the snake is going to that direction or not

# Other int variables
step = 23 # Variable used for random operations
score = 0 # The user's score
length = 2 # The snake's length
speed = 80 # The snake's speed

# Lists to store the coordinates of the snake
# Both are lists, which will keep at all time the positions of the snake and the different parts of it
x_snake_position = [0]
y_snake_position = [0]

# Increasing the size of the list to be able to have 1000 sections for the snake's body
for i in range(0,1000):
    x_snake_position.append(-100)
    y_snake_position.append(-100)

# Initialising pygame
pygame.init()

# Creating/Setting up the main window
window = pygame.display.set_mode((600, 600))
window_rect = window.get_rect() # Gets and stores the coordinates of a given object for later use.
pygame.display.set_caption("Snake Game") # Sets the caption of the main window

# Drows an image on the main window (Blitting a cover over it that we will colour in white with .fill)
cover = pygame.Surface(window.get_size())
cover = cover.convert()
cover.fill((250, 250, 250)) # Fills the entire board game with a chosen colour (white)
window.blit(cover, (0,0)) # Sticks the cover to the window (by using .flip so it appears on the screen)

# Since we used blit we now use display to refresh the screen to display everything
pygame.display.flip()

# Loading the main images on the game window
head = pygame.image.load("head.png").convert_alpha() # Loads the image for the head of the snake
head = pygame.transform.scale(head, (35,35)) # Scaling the image so it will fit the window

body_part = pygame.image.load("body.png").convert_alpha() # Loads the image for the body part of the snake
body_part = pygame.transform.scale(body_part, (25,25)) # Scaling the image so it will fit the window

apple = pygame.image.load("apple.png").convert_alpha() # Loads the image for the apples used
apple = pygame.transform.scale(apple, (35,35)) # Scaling the image so it will fit the window

# Storing the head and apple's coordinates in variables
position_head = head.get_rect()
position_apple = apple.get_rect()

# Storing the variables in the list variables that were created before (position 0 is used for the head)
x_snake_position[0] = position_head.x
y_snake_position[0] = position_head.y

# Giving random coordinates to the first apple of the game
position_apple.x = randint(2,10) * step
position_apple.y = randint(2,10) * step


# While loop for running the game
while (playing == True):

    # Collecting all the events
    for event in pygame.event.get():

        # Checks if the user quits the game
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            playing = False

        # Checks if the user presses a key
        # Getting the user’s interactions with the arrow keys (up, down, left and right). Depending on which one the user presses,
        # the values of the variables are changed accordingly (which will occur so that the snake will move in the right direction).
        # E.X., if the user presses the left key, the value of the other variables are changed to False and the value of moveLeft to True.
        # In case the user presses left when the snake is going right, there is an if statement which will leave the value of unchanged if this happens.
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:

                if moveUp == False and move_init == True:
                    if moveDown == True:
                        moveUp == False

                    else:

                        moveDown = moveRight = moveLeft = False
                        moveUp = move_init = True

            if event.key == pygame.K_DOWN:

                if moveDown == False:
                    if moveUp == True:
                        moveDown == False

                    else:

                        moveRight = moveLeft = moveUp = False
                        moveDown = move_init = True

            if event.key == pygame.K_RIGHT:

                if moveRight == False:
                    if moveLeft == True:
                        moveRight == False

                    else:

                        moveLeft = moveUp = moveDown = False
                        moveRight = move_init = True

            if event.key == pygame.K_LEFT:

                if moveLeft == False:
                    if moveRight == True:
                        moveLeft == False

                    else:

                        moveRight = moveDown = moveUp = False
                        moveLeft = move_init = True


  # Drawing the head and the first part of the body
    window.blit(body_part,(495,5))
    window.blit(head,(500,0)) # Top  corner of the window

  # Moving each part of the body by giving them new coordinates.
  # Each part of the snake will take the positions of the part before it.
  # By doing this on the entire list, we end up giving updated coordinates to the entire snake.
    for i in range(length-1,0,-1):
        x_snake_position[i] = x_snake_position[(i-1)]
        y_snake_position[i] = y_snake_position[(i-1)]

  # Filling the window with white color to erase the different parts of the snake (previus step)
    cover.fill((250, 250, 250))  # Color white (250,250,250) RGB

  # Blitting the updated(new) parts of the snake on the screen
    for i in range(1,length):
        cover.blit(body_part, (x_snake_position[i], y_snake_position[i]))

  # Moving the snake in a certain direction depending on which key the user has pressed
    if moveUp:
        y_snake_position[0] = y_snake_position[0] - step
        window.blit(cover, (0,0))
        window.blit(head, (x_snake_position[0], y_snake_position[0]))

    if moveDown:
        y_snake_position[0] = y_snake_position[0] + step
        window.blit(cover, (0,0))
        window.blit(head, (x_snake_position[0], y_snake_position[0]))

    if moveRight:
        x_snake_position[0] = x_snake_position[0] + step
        window.blit(cover, (0,0))
        window.blit(head, (x_snake_position[0], y_snake_position[0]))

    if moveLeft:
        x_snake_position[0] = x_snake_position[0] - step
        window.blit(cover, (0,0))
        window.blit(head, (x_snake_position[0], y_snake_position[0]))


    # Checking if the snake hits the edges of the window
    if x_snake_position[0] < window_rect.left:
        playing = False

    if x_snake_position[0] + 35 > window_rect.right:
        playing = False

    if y_snake_position[0] < window_rect.top:
        playing = False

    if y_snake_position[0] + 35 > window_rect.bottom:
        playing = False

    # Checking for every part of the snake to check if the snake hits itself
    if collision(x_snake_position[0], y_snake_position[0], x_snake_position[i], y_snake_position[i],0,0) and (move_init == True):
        playing = False


    # Drawing / Blitting the apple
    window.blit(apple, position_apple)

    # Checking if the snake hits the apple
    if collision(x_snake_position[0], y_snake_position[0], position_apple.x, position_apple.y,35,25):

        # Giving new coordinates to the apple when the snake eats it
        position_apple.x = randint(1,20) * step
        position_apple.y = randint(1,20) * step

        # Giving new coordinates to the apple if the ones given above are the same as the snake's ones
        # (Bad complecity for this part, could use something to save/avoid failed positions)
        for j in range(0,length):
            while collision(position_apple.x, position_apple.y, x_snake_position[j], y_snake_position[j],35,25):
                position_apple.x = randint(1,20) * step
                position_apple.y = randint(1,20) * step

        # Finally ,increasing the snake's and user's score
        length = length + 1
        score = score + 1


    # Displaying the user's score
    display_score(score)

    # Flipping to add everything on the board (refreshes the screen)
    pygame.display.flip()

    # Delaying the game to make snake move smoothly
    time.sleep (speed / 1000)

# Exits the game
pygame.quit()
exit()
