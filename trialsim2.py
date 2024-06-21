import pygame

pygame.init()
screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption('Trial Simulation')
icon = pygame.image.load("drone (1).png")
pygame.display.set_icon(icon)
playerImg = pygame.image.load("player.png")
back = pygame.image.load("2381.jpg")
playerX = 360
playerY = 500
playerX_change = 0
playerY_change = 0

targetImg = pygame.image.load("target.png")
targetX = 300
targetY = 120
targetX_change = 0.3
targetY_change = 40


def target():
    screen.blit(targetImg, (targetX, targetY))


def player(x, y):
    screen.blit(playerImg, (x, y))


running = True
while running:
    screen.fill((86, 52, 45))
    screen.blit(back, (0, 0))
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                print("Left key is pressed.")
                playerX_change = -0.3
            elif events.key == pygame.K_RIGHT:
                print("Right key is pressed")
                playerX_change = +0.3

            else:
                print("Some random key has been pressed")
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
                print("Key has been released")
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 1436:
        playerX = 1436

    targetX += targetX_change
    if targetX <= 0:
        targetX_change = 0.3
        targetY += targetY_change
    if targetX >= 1436:
        targetX_change = -0.3
        targetY += targetY_change

    #if targetY >= 536:


    player(playerX, playerY)
    target()
    pygame.display.update()
