import pygame

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((850, 700))

# Background Screen
background = pygame.image.load('background_image.png')

# Adding title to the gaming window
pygame.display.set_caption("Space Invaders")

# Adding icon to the gaming window
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Game Starting
starting_font = pygame.font.Font('freesansbold.ttf', 64)


def game_starting_text():
    starting_text = starting_font.render('SPACE INVADERS', True, (255, 255, 255))
    screen.blit(starting_text, (200, 300))


running = True
while running:
    # The display is in RGB(Red, Green, Blue) Format
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(background, (150, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # If keystroke is pressed then check whether it is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                # import EndlessVersion_OneEnemy_1
                pass
