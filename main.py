import pygame
import random
import os
import math
from pygame import mixer
pygame.init()
WIDTH  = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PhaJAPPle!")
logo = pygame.image.load("assets\\gfx\\Logo.png")
pygame.display.set_icon(logo)
TitleGround = pygame.image.load("assets\\gfx\\Titlescreen.png")
mixer.music.load("assets\\sfx\\music.wav")
mixer.music.play(-1)
FPS = 60
clock = pygame.time.Clock()
Scorevalue = 0
font = pygame.font.Font("assets\\fonts\\AAA.otf", 30)
fontX = 10
fontY = 50
def Score(x,y):
    score = font.render("APPles : " + str(Scorevalue),True, (0,0,0))
    screen.blit(score, (x,y))
Hungervalue = 100
Dont = pygame.font.Font("assets\\fonts\\ABC.otf", 30)
DontX = 10
DontY = 10
def Hunger(x,y):
    hunger = Dont.render("HP : " + str(Hungervalue), True, (0,0,0))
    screen.blit(hunger, (x,y))
PlayerIMG = pygame.image.load("assets\\gfx\\Player.png")
playerX = random.randint(200,600)
playerY = random.randint(275,475)
playerXChange = 3
playerYChange = 3
playerXChangeNorm = 3
playerYChangeNorm = 3
def Player(x,y):
    screen.blit(PlayerIMG, (x,y))
AppleIMG = pygame.image.load("assets\\gfx\\Apple.png")
AppleImg = pygame.transform.scale(AppleIMG, (64,64))
AppleX = random.randint(0, WIDTH - 250)
AppleY = random.randint(0, HEIGHT- 125)
def Apple(AppleX,AppleY):
    screen.blit(AppleImg, (AppleX,AppleY))
def isEatApple(playerX,playerY,AppleX,AppleY):
    distance = math.sqrt(math.pow(playerX-AppleX,2) + (math.pow(playerY-AppleY,2)))
    if distance < 64:
        return True
    else:
        return False
DeadIMG = pygame.image.load("assets\\gfx\\DeadScreen.png")
dead = False
def Dead():
    if dead == True:
        global playerXChange
        playerXChange = 0
        global playerYChange
        playerYChange = 0
        global AppleX
        AppleX = 1024
        global AppleY
        AppleY = 900
        screen.blit(DeadIMG, (0,0))
def reset():
    global playerX
    playerX = random.randint(200,600)
    global playerY
    playerY = random.randint(275,475)
    global playerXChange
    playerXChange = 3
    global playerYChange
    playerYChange = 3
    global playerXChangeNorm
    playerXChangeNorm = 3
    global playerYChangeNorm
    playerYChangeNorm = 3
    global Hungervalue
    Hungervalue = 100
    global Scorevalue
    Scorevalue = 0
    global AppleX
    AppleX = random.randint(0, WIDTH - 250)
    global AppleY
    AppleY = random.randint(0, HEIGHT- 125)
titlescreen = True
run = False
while titlescreen:
    clock = pygame.time.Clock()
    clock.tick(FPS)
    screen.fill((0,0,0))
    screen.blit(TitleGround, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            titlescreen = False     
        if event.type == pygame.MOUSEBUTTONDOWN:
            run = True
            titlescreen = False
            start = mixer.Sound("assets\\sfx\\start.wav")
            mixer.Sound.play(start)     
    pygame.display.update()
while run:
    screen.fill((255,255,255))
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not isEatApple(playerX,playerY,AppleX,AppleY) and not Dead():
                Hungervalue -= 1
                ouch = mixer.Sound("assets\\sfx\\ouch.wav")
                mixer.Sound.play(ouch)
            elif event.key ==pygame.K_SPACE and isEatApple(playerX,playerY,AppleX,AppleY) and not Dead():
                AppleX = random.randint(0, WIDTH  - 250)
                AppleY = random.randint(0, HEIGHT - 125)
                Scorevalue += 1
                Hungervalue += 5
                if Scorevalue <18:
                    playerXChange += playerXChange / 10
                    playerYChange += playerYChange / 10
                    playerXChangeNorm += playerXChangeNorm / 10
                    playerYChangeNorm += playerYChangeNorm / 10
                elif Scorevalue >=18 and Scorevalue <=25:
                    playerXChange += playerXChange / 15
                    playerYChange += playerYChange / 15
                    playerXChangeNorm += playerXChangeNorm / 15
                    playerYChangeNorm += playerYChangeNorm / 15
                elif Scorevalue > 25 and Scorevalue <=30:
                    playerXChange += playerXChange / 20
                    playerYChange += playerYChange / 20
                elif Scorevalue > 30 and Scorevalue <= 35:
                    playerXChange += playerXChange / 25
                    playerYChange += playerYChange / 25
                elif Scorevalue > 35 and Scorevalue <= 40:
                    playerXChange += playerXChange / 30
                    playerYChange += playerYChange / 30
                elif Scorevalue > 40 and Scorevalue <=45:
                    playerXChange += playerXChange / 35
                    playerYChange += playerYChange / 35
                elif Scorevalue > 45 and Scorevalue <= 50:
                    playerXChange += playerXChange / 40
                    playerYChange += playerYChange / 40
                elif Scorevalue > 50:
                    playerXChange += playerXChange / 50
                    playerYChange += playerYChange / 50
                    playerXChangeNorm += playerXChangeNorm / 20
                    playerYChangeNorm += playerYChangeNorm / 20
                congrats = mixer.Sound("assets\\sfx\\point.wav")
                mixer.Sound.play(congrats)
            if event.key == pygame.K_RETURN:
                playerX = random.randint(200,600)
                playerY = random.randint(275,475)
            if event.key == pygame.K_BACKSPACE:
                Hungervalue += 20
                Scorevalue += 20
        if Hungervalue <= 0:
            dead = True
            Dead()
        if event.type == pygame.MOUSEBUTTONDOWN and dead == True:
            dead = False
            ok = pygame.image.load("assets\\gfx\\backscreen.png")
            screen.blit(ok, (0,0))
            revive = mixer.Sound("assets\\sfx\\revive.wav")
            mixer.Sound.play(revive)
            reset()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                playerXChange = playerXChangeNorm
                playerYChange = playerYChangeNorm
    playerX += playerXChange
    playerY += playerYChange
    if playerX >= 725 and playerX < 800:
        playerXChange = playerXChange - playerXChange * 2
        playerXChangeNorm = playerXChangeNorm - playerXChangeNorm * 2
    if playerX >= 850:
        playerX = random.randint(200,600)
        playerY = random.randint(275,475)
    if playerX <= 0 and playerX > -30:
        playerXChange = playerXChange - playerXChange * 2
        playerXChangeNorm = playerXChangeNorm - playerXChangeNorm * 2
    if playerX <= -50:
        playerX = random.randint(200,600)
        playerY = random.randint(275,475)
    if playerY >= 550 and playerY < 600:
        playerYChange = playerYChange - playerYChange * 2
        playerYChangeNorm = playerYChangeNorm - playerYChangeNorm * 2
    if playerY >=650:
        playerX = random.randint(200,600)
        playerY = random.randint(275,475)
    if playerY <= 0 and playerY > -30:
        playerYChange = playerYChange - playerYChange * 2
        playerYChangeNorm = playerYChangeNorm - playerYChangeNorm * 2
    if playerY <= -50:
        playerX = random.randint(200,600)
        playerY = random.randint(275,475)
    if Hungervalue > 100:
        Hungervalue = 100
    Apple(AppleX, AppleY)
    Player(playerX, playerY)
    Hunger(DontX, DontY)
    Score(fontX,fontY)
    Dead()
    pygame.display.update()