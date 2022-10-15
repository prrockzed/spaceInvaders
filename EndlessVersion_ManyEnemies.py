import pygame
import random
import math
from pygame import mixer

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

# Player
playerImg = pygame.image.load('arcade-game.png')
playerX = 405
playerY = 620
playerX_change = 0
playerY_change = 40

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

# Finding the number of enemies the user wants
number_of_enemies = int(input("How many do you want to tackle? "))

for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(5, 790))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1.75)
    enemyY_change.append(50)

# Background Music
mixer.music.load('background.wav')
mixer.music.play(-1)

# Bullet
# ready state - you can't see the bullet on the screen
# fire state - the bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 0
bulletX_change = 0
bulletY_change = 3
bullet_state = "ready"

# Fonts
score_value = 0
font = pygame.font.Font('WhiteMonkey-Regular.ttf', 40)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score is " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 300))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, t):
    screen.blit(enemyImg[t], (x, y))


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
                playerX_change = -2.6
            if event.key == pygame.K_RIGHT:
                playerX_change = 2.6
            if event.key == pygame.K_UP:
                playerY_change = -1.75
            if event.key == pygame.K_DOWN:
                playerY_change = 1.75
            if event.key == pygame.K_SPACE:
                # for bullet sound
                bullet_sound = mixer.Sound('laser.wav')
                bullet_sound.play()
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

    for i in range(number_of_enemies):

        # Game Over
        if enemyY[i] > 500:
            for j in range(number_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        # Updating the movement of enemy
        enemyX[i] += enemyX_change[i]

        # Restricting the movement of enemy
        if enemyX[i] <= 5:
            enemyX_change[i] = 1.75
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 790:
            enemyX_change[i] = -1.75
            enemyY[i] += enemyY_change[i]

        # Collision, Restarting the bullet and Generating the Enemy again
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            # for bullet sound
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 620
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(5, 790)
            enemyY[i] = random.randint(50, 150)

        # Calling the enemy icon
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Restructuring
    if bulletY <= 0:
        bulletY = 620
        bullet_state = "ready"

    # Bullet Movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Calling the player icon
    player(playerX, playerY)

    # Calling the score function
    show_score(textX, textY)

    # Updating the pygame window
    pygame.display.update()
