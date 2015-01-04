import pygame
import random

pygame.init()

window = pygame.display.set_mode((800,600))
pygame.display.set_caption('Chechi Game')

BLACK  = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
SKY = (80,0,250)

pygame.mixer.music.load('helicopter_loop.wav')
bulletSound = pygame.mixer.Sound('gunshot5.wav')
planeCollideSound = pygame.mixer.Sound('drip.wav')

bulletColor = GREEN

player = pygame.Rect(400,550,50,50)
wall = pygame.Rect(0,600,800,10)

moveleft = False
moveright = False
moveup = False
movedown = False

playerImage =  pygame.image.load('F11.bmp')
playerStretchedImage = pygame.transform.scale(playerImage,(40,40))
foodImage = pygame.image.load('food.bmp')
foodStretchedImage = pygame.transform.scale(foodImage,(30,30))
foodImage2 = pygame.image.load('food2.bmp')
foodStretchedImage2 = pygame.transform.scale(foodImage2,(30,30))

gameScore = 0
score = 0
FOODSPEED = 70
foodCounter = 0
foods = []
bullets = []
movespeed = 4
movespeed2 = 4
movespeed3 = 5

clock = pygame.time.Clock()
gameLoop = True

while gameLoop:
    window.fill(WHITE)

    pygame.mixer.music.play(-1,0.0)
    
    if (score > 800):
        pygame.mixer.music.stop()
        pygame.quit()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveleft = True
            if event.key == pygame.K_RIGHT:
                moveright = True
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.left + 20,player.top,3,10))
           

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveleft = False
            if event.key == pygame.K_RIGHT:
                moveright = False

        if event.type == pygame.MOUSEBUTTONUP:
            bullets.append(pygame.Rect(player.left + 20,player.top,3,10))

    if moveleft == True and player.left > 0 :
        player.left -= movespeed
    if moveright == True and player.right < 800:
        player.left += movespeed

    foodCounter += 1
    if foodCounter >= FOODSPEED:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(50,550),0,30,30))
    
    for food in foods:
        if player.colliderect(food):
            planeCollideSound.play()
            gameScore -= .03846
        if wall.colliderect(food):
            score += 1
        for bullet in bullets:
            if bullet.colliderect(food):
                foods.remove(food)
                bullets.remove(bullet)
                gameScore += 1
                bulletSound.play()
            
           
    window.blit(playerStretchedImage,player)
        
    for i in range(len(foods)):
        window.blit(foodStretchedImage,foods[i])
        foods[i].top += movespeed2
        
    for bullet in bullets:
        pygame.draw.rect(window,bulletColor,bullet)
        bullet.top -= movespeed3
    
    if (gameScore > 15):
        foodStretchedImage = foodStretchedImage2
        movespeed = 7
        movespeed2 = 5
        bulletColor = RED
    clock.tick(70)
    pygame.display.update()
    
pygame.quit()


