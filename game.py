import pygame
import random
import math
#initialise pygame 
pygame.init()

#create a screen 
screen = pygame.display.set_mode((901,600))

#background 
background = pygame.image.load("bg.png")
#title and icon 
pygame.display.set_caption("Space invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#player 
playerimg = pygame.image.load("ufo1.png")
playerX = 370
playerY = 480
playerX_change = 0 

#enemy 
emnemyimg = pygame.image.load("enemy.png")
enemyX = random.randint(0,736) 
enemyY = random.randint(50,150)
enemyX_change = 0.3 
enemyY_change = 40

#bullet 
#ready - you can't see the bullet 
#fire - the bullet is moving 
bulletimg = pygame.image.load("bullet.png")
bulletX = 0 
bulletY = 480 
bulletX_change = 0 
bulletY_change = 0.5 
bullet_state = "ready"


def player(x,y):
  screen.blit(playerimg,(x,y))

def enemy(x,y):
  screen.blit(emnemyimg,(x,y))

def fire_bullet(x,y):
  global bullet_state
  bullet_state = "fire"
  screen.blit(bulletimg,(x+16,y+10))

def iscollision(eX,eY,bX,bY):
  distance=math.sqrt((math.pow(eX-bX,2))+(math.pow(eY-bY,2)))
  if distance < 27:
    return True
  else:
    return False

running = True 
while running:
  screen.fill((0,0,255)) # rgb 
  screen.blit(background,(0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT :
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        playerX_change = -0.3 
      if event.key == pygame.K_RIGHT:
        playerX_change = 0.3
      if event.key == pygame.K_SPACE:
        bulletX = playerX
        fire_bullet(playerX,bulletY)
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        playerX_change=0 
  
  #setting boundaries for player 
  playerX += playerX_change
  if playerX<=0: 
    playerX = 0
  elif playerX>=836:
    playerX = 836

  #setting boundaries for enemy
  if enemyX<=0:
    enemyX_change = 0.3 
    enemyY += enemyY_change
  elif enemyX>=836:
    enemyX_change= -0.3
    enemyY += enemyY_change
  enemyX += enemyX_change
  #collision 
  collision=iscollision(enemyX,enemyY,bulletX,bulletY)
  if collision :
    bulletY = 480
    bullet_state="ready"
    enemyX = random.randint(0,836)
    enemyY = random.randint(50,150)

  #bullet movement 
  if bulletY<=0:
    bulletY=480
    bullet_state="ready"
  if bullet_state == "fire":
    fire_bullet(bulletX,bulletY)
    bulletY -= bulletY_change
  #function call 
  enemy(enemyX,enemyY)
  player(playerX,playerY)
  pygame.display.update()
