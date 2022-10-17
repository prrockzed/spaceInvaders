# Importing Required Modules
import pygame

# Initialising pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode()

# Background
background = pygame.image.load('galaxy.jpeg')

running = True
while running:
    screen.fill()
    screen.blit(background, (0, 0))
