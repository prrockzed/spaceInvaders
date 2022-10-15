# noinspection DuplicatedCode
import pygame
import random
import math

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((850, 700))

# Background Screen
background = pygame.image.load('galaxy.jpeg')

# Adding title to the gaming window
pygame.display.set_caption("Space Invaders")

# Adding icon to the gaming window
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('arcade-game.png')
playerX = 405
playerY = 620
playerX_change = 0
playerY_change = 40

# Enemy
enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(5, 790)
enemyY = random.randint(50, 150)
enemyX_change = 0.8
enemyY_change = 40

# Bullet
# ready state - you can't see the bullet on the screen
# fire state - the bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 0
bulletX_change = 0
bulletY_change = 6
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 12, y + 10))


def isCollision(en_x, en_y, bul_x, bul_y):
    distance = math.sqrt(math.pow(en_x - bul_x, 2) + math.pow(en_y - bul_y, 2))
    if distance < 27:
        return True
    else:
        return False


score = 0

# game loop
running = True
while running:

    # The display is in RGB(Red, Green, Blue) Format
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(background, (-170, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed then check whether it is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_UP:
                playerY_change = -1.5
            if event.key == pygame.K_DOWN:
                playerY_change = 1.5
            if event.key == pygame.K_SPACE:
                # gets the current x and y coordinate of the player
                bulletX = playerX
                bulletY = playerY
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    # Updating the coordinates of the player
    playerX += playerX_change
    playerY += playerY_change

    # Restricting the movement of the player
    if playerX <= 5:
        playerX = 5
    elif playerX >= 790:
        playerX = 790
    if playerY >= 620:
        playerY = 620
    elif playerY <= 520:
        playerY = 520

    # Updating the movement of enemy
    enemyX += enemyX_change

    # Restricting the movement of enemy
    if enemyX <= 5:
        enemyX_change = 0.8
        enemyY += enemyY_change
    elif enemyX >= 790:
        enemyX_change = -0.8
        enemyY += enemyY_change

    # Bullet Restructuring
    if bulletY <= 0:
        bulletY = 620
        bullet_state = "ready"

    # Bullet Movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision, Restarting the bullet and Generating the Enemy again
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 620
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(5, 790)
        enemyY = random.randint(50, 150)

    # Calling the player and enemy icon
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    # Updating the pygame window
    pygame.display.update()
