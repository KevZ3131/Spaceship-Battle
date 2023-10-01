'''
Name: Kevin Tran
Date: June 26, 2022
File Name: KevinTran_Unit2Assignment2.py
Description: This is a modicaition of Tech With Tim's program. There will be two players for the two-player space battle. The keys "w," "a," "s," and "d" will be used by Player 1 to operate the spaceship on the left side of the screen. Using the "tab" key, Player 1 can shoot. Using the arrow keys, Player 2 will manoeuvre the spacecraft on the right side of the screen (up, down, left, right). The "enter" key is used to fire by Player 2. Players each have 100 health. When a player is struck by a bullet, their health is reduced by 10. The game ends and the losing player is the one whose health reaches zero. There are 5 ships to choose from, all, with different charateristics. In addition, there are 3 power ups, a heal, a speed boost and damage boost. 

This program has been modified from and with: 
https://www.youtube.com/watch?v=jO6qQDNa2UY&ab_channel=TechWithTim 
https://www.youtube.com/watch?v=GMBqjxcKogA&ab_channel=BaralTech

'''
#import pygame
import pygame
#import os
import os
#import random
import random
#import mixer
pygame.mixer.init()
#import fonts
pygame.font.init()

# X and Y values set to the width and the height
WIDTH, HEIGHT = 900,500

# The Window variable is taking control of the window, and setting it to the values of the width and height
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# pygame.display sets the title of the window to "First Game!"
pygame.display.set_caption("First Game!")

#Define white, black, red, yellow, blue
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)
BLUE=(0,0,255)

#Import bullet fire sound and bullet hit sound and background music
BULLET_FIRE_SOUND=pygame.mixer.Sound(os.path.join('Assets','bullet_fire_sound.wav'))
BULLET_HIT_SOUND=pygame.mixer.Sound(os.path.join('Assets','bullet_hit_sound.wav'))
pygame.mixer.music.load(os.path.join('Assets','background.wav'))

#Play background music while program is running
pygame.mixer.music.play(-1)

#Set the border
BORDER = pygame.Rect(WIDTH/2-5,0,10,HEIGHT)

#Define health and winner font
HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 100)

#Set frames per second to 60
FPS=60

#Set spaceship width to 55 pixels and spaceship height to 40 pixels
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

#Define player 1 hit userevent, and player 2 hit userevent
PLAYER1_HIT = pygame.USEREVENT+1
PLAYER2_HIT = pygame.USEREVENT+2

#Definer player 1 and player 2 ship
PLAYER1_SHIP=0
PLAYER2_SHIP=0

#Import yellow spaceship
YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
#Resize the yellow spaceship to 55 by 40 
YELLOW_SPACESHIP =pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

#Import red spaceship
RED_SPACESHIP_IMAGE=pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
#Resize the red spaceship to 55 by 40 
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

#Import scout ship 
SCOUT_SHIP_IMAGE=pygame.image.load(os.path.join('Assets', 'scout_ship.png'))
#Resize the red spaceship to 55 by 40 
SCOUT_SHIP = pygame.transform.scale(SCOUT_SHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

#Import tank ship 
TANK_SHIP_IMAGE=pygame.image.load(os.path.join('Assets', 'tank_ship.png'))
#Resize the tank to 55 by 40 and rotate by 180 degrees
TANK_SHIP = pygame.transform.rotate(pygame.transform.scale(TANK_SHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),180)

#Import medical ship 
MEDICAL_SHIP_IMAGE=pygame.image.load(os.path.join('Assets', 'medical_ship.png'))
#Resize the medical ship to 55 by 40 and rotate by 180 degrees
MEDICAL_SHIP = pygame.transform.rotate(pygame.transform.scale(MEDICAL_SHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),180)

#Import player 2 bullet
PLAYER2_BULLET_IMAGE=pygame.image.load(os.path.join('Assets', 'red_bullet.png'))
#Resize the player 2 bullet spaceship to 30 by 50
PLAYER2_BULLET = pygame.transform.scale(PLAYER2_BULLET_IMAGE, (30,50))

#Import player 1 bullet
PLAYER1_BULLET_IMAGE=pygame.image.load(os.path.join('Assets', 'player1_bullet.png'))
#Resize the player 1 bullet to 30 by 20 
PLAYER1_BULLET = pygame.transform.scale(PLAYER1_BULLET_IMAGE, (30,20))

#Import 5 space background
SPACE1=pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))
SPACE2=pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space2.jpg')), (WIDTH, HEIGHT))
SPACE3=pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space3.jpg')), (WIDTH, HEIGHT))
SPACE4=pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space4.jpg')), (WIDTH, HEIGHT))
SPACE5=pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space5.jpg')), (WIDTH, HEIGHT))


#Import buff
BUFF_IMAGE=pygame.image.load(os.path.join('Assets', 'buff.png'))
#Resize buff to the same size as buff
BUFF=pygame.transform.scale(BUFF_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

#Import heal
HEAL_IMAGE=pygame.image.load(os.path.join('Assets', 'health.png'))
#Resize heal to the same size of a ship
HEAL = pygame.transform.scale(HEAL_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

#Import speed
SPEED_BUFF_IMAGE=pygame.image.load(os.path.join('Assets', 'speed.png'))
#Resize heal to the same size of a ship
SPEED_BUFF = pygame.transform.scale(SPEED_BUFF_IMAGE, (30,20))

#Define a backgrounds list
backgrounds=[]

#Add all the backgrounds into the backgrounds list
backgrounds.append(SPACE1)
backgrounds.append(SPACE2)
backgrounds.append(SPACE3)
backgrounds.append(SPACE4)
backgrounds.append(SPACE5)

#Draws all the main components of the game
def draw_window(player2, player1, PLAYER1_SHIP, PLAYER2_SHIP, player2_bullets, player1_bullets, PLAYER2_HEALTH_BAR, PLAYER1_HEALTH_BAR, speed_buff_x,speed_buff_y, buff_x,buff_y):
  # Fills the background of the window to be completely white
  WIN.blit(background,(0,0))
  # Makes a rectangular black border, so that the 2 spaceships are on each side
  pygame.draw.rect(WIN, BLACK, BORDER)
  #Draw player 2 health bar
  pygame.draw.rect(WIN, RED, PLAYER2_HEALTH_BAR)
  #Draw player 1 health bar
  pygame.draw.rect(WIN, BLUE, PLAYER1_HEALTH_BAR)
  #Display speed buff
  WIN.blit(SPEED_BUFF,(speed_buff_x,speed_buff_y))
  #Display heal
  WIN.blit(HEAL,(heal_x,heal_y))
  #Display buff
  WIN.blit(BUFF,(buff_x,buff_y))

  # Display player 1's ship depending on the ship they choose
  if PLAYER1_SHIP=='ship1':
    WIN.blit(PLAYER1_SPACESHIP,(player1.x,player1.y))
  elif PLAYER1_SHIP=='ship2':
    WIN.blit(PLAYER1_SPACESHIP,(player1.x,player1.y))
  elif PLAYER1_SHIP=='ship3':
    WIN.blit(PLAYER1_SPACESHIP,(player1.x,player1.y))
  elif PLAYER1_SHIP=='ship4':
    WIN.blit(PLAYER1_SPACESHIP,(player1.x,player1.y))
  elif PLAYER1_SHIP=='ship5':
    WIN.blit(PLAYER1_SPACESHIP,(player1.x,player1.y))
    
  #Display player 2's ship depending on the ship they choose
  if PLAYER2_SHIP=="ship3":
    WIN.blit(PLAYER2_SPACESHIP,(player2.x, player2.y))
  elif PLAYER2_SHIP=="ship2":
    WIN.blit(PLAYER2_SPACESHIP,(player2.x, player2.y))
  elif PLAYER2_SHIP=="ship1":
    WIN.blit(PLAYER2_SPACESHIP,(player2.x, player2.y))
  elif PLAYER2_SHIP=="ship4":
    WIN.blit(PLAYER2_SPACESHIP,(player2.x, player2.y))
  elif PLAYER2_SHIP=="ship5":
    WIN.blit(PLAYER2_SPACESHIP,(player2.x, player2.y))
    
  # For every bullet that is shot from the list player2_bullets, draw a bullet coming from that spaceship
  for bullet in player2_bullets:
    WIN.blit(PLAYER1_BULLET,(bullet.x,bullet.y))
  # For every bullet that is shot from the list player1_bullets, draw a bullet coming from that spaceship
  for bullet in player1_bullets:
    WIN.blit(PLAYER2_BULLET,(bullet.x,bullet.y))


  # This will, indefinitely, update the display after creating the rectangular border the spaceship png's
  pygame.display.update()

#Handle player 1 movement
def player1_handle_movement(keys_pressed,player1):
    if keys_pressed[pygame.K_a] and player1.x-player1_vel>0: #LEFT
      player1.x-=player1_vel
    if keys_pressed[pygame.K_w] and player1.y-player1_vel>0:#UP
      player1.y-=player1_vel
    if keys_pressed[pygame.K_s] and player1.y + player1_vel+player1.height < HEIGHT-15 :#DOWN
      player1.y+=player1_vel
    if keys_pressed[pygame.K_d] and player1.x+player1_vel+player1.width-15<BORDER.x:#RIGHT
      player1.x+=player1_vel

#Handle player 2 movement
def player2_handle_movement(keys_pressed, player2):
    if keys_pressed[pygame.K_LEFT] and player2.x-player2_vel>BORDER.x+12: #LEFT
      player2.x-=player2_vel
    if keys_pressed[pygame.K_UP] and player2.y-player2_vel>0:#UP
      player2.y-=player2_vel
    if keys_pressed[pygame.K_DOWN] and player2.y+player2.height+player2_vel<HEIGHT-15:#DOWN
      player2.y+=player2_vel
    if keys_pressed[pygame.K_RIGHT] and player2.x<900-45:#RIGHT
      player2.x+=player2_vel

#Hand bullets
def handle_bullets(player1_bullets, player2_bullets, player1, player2, player1_bullet_vel, player2_bullet_vel):
  #Move each bullet bullet in the list 
  for bullet in player1_bullets:
    bullet.x += player1_bullet_vel
    #If player 2 hits player 1 bullet, broadcast player 2 hit and remove the bullet
    if player2.colliderect(bullet):
      pygame.event.post(pygame.event.Event(PLAYER2_HIT))
      player1_bullets.remove(bullet)
    #If player 1 bullet goes off screen, remove the bullet
    elif bullet.x>WIDTH:
        player1_bullets.remove(bullet)
  #Move each bullet bullet in the list 
  for bullet in player2_bullets:
    bullet.x -= player2_bullet_vel
    #If player 1 hits player 2 bullet, broadcast player 1 hit and remove the bullet
    if player1.colliderect(bullet):
      pygame.event.post(pygame.event.Event(PLAYER1_HIT))
      player2_bullets.remove(bullet)
    #If player 2 bullet goes off screen, remove the bullet
    elif bullet.x<0:
        player2_bullets.remove(bullet)

#Display the winner
def draw_winner(text):
  #set the font
  draw_text=WINNER_FONT.render(text,1, WHITE)
  #Display the winner
  WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2 ))
  pygame.display.update()
  pygame.time.delay(5000)

#Main menu
def main_menu():
  #Set run True and click False
  run=True
  click=False

  #While run is true, keep running
  while run==True:
    #Display the background
    WIN.blit(background,(0, 0))
    #Set the font and display play game
    font = pygame.font.SysFont('ComicSans', 50)
    word = font.render('PLAY GAME', True, WHITE)
    WIN.blit(word, (WIDTH/2-word.get_width()/2, HEIGHT/2 - word.get_height()/2))

    #Track cursour coordinates
    mx, my= pygame.mouse.get_pos()

    #Rect play game
    play_game=pygame.Rect(WIDTH/2-125, HEIGHT/2-50, 300, 80)

    #Let the user exit the program if they choose or if the user clicks their left mouse button set click to true
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
      if event.type==pygame.MOUSEBUTTONDOWN:
        if event.button == 1: 
          click=True
      
    #If the cursor is hovering over play game and click is true, set run to false
    if play_game.collidepoint((mx, my)):
      if click:
        run=False
        
    #Set click to false
    click=False
    
    #Update the display
    pygame.display.update()

#Player 1 choose ship
def choose_ship1():
    #Set run to true and click to false
    run=True
    click=False

    #While run is true run
    while run==True:

        #Display the background
        WIN.blit(background,(0, 0))

        #Set the font and word
        font = pygame.font.SysFont('ComicSans', 50)
        word= font.render('CHOOSE YOUR SHIP PLAYER 1', True, WHITE)

        #Display the word
        WIN.blit(word, (WIDTH/2-word.get_width()/2, 0))

        #Track mouse coordinates
        mx, my= pygame.mouse.get_pos()

        #Display all 5 ships
        WIN.blit(RED_SPACESHIP,(200, HEIGHT/2 - word.get_height()/2))
        WIN.blit(YELLOW_SPACESHIP,(300, HEIGHT/2 - word.get_height()/2))
        WIN.blit(SCOUT_SHIP,(400, HEIGHT/2 - word.get_height()/2) )
        WIN.blit(TANK_SHIP,(500, HEIGHT/2 - word.get_height()/2) )
        WIN.blit(MEDICAL_SHIP,(600, HEIGHT/2 - word.get_height()/2) )

        #Rect all 5 ships
        ship1=pygame.Rect(200, HEIGHT/2 - word.get_height()/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        ship2=pygame.Rect(300, HEIGHT/2 - word.get_height()/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        ship3=pygame.Rect(400, HEIGHT/2 - word.get_height()/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        ship4=pygame.Rect(500, HEIGHT/2 - word.get_height()/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        ship5=pygame.Rect(600, HEIGHT/2 - word.get_height()/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

        #Let the user leave the game if they want, if they left click on their mouse, set click to true
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    click=True
                  
        #Check if mouse coordinates are on a ship and if user click is true, return the ship they chose
        if ship1. collidepoint((mx, my)):
            if click==True:
                return('ship1')
        elif ship2. collidepoint((mx, my)):
            if click==True:
                return('ship2')
        elif ship3. collidepoint((mx, my)):
            if click==True:
                ship3=True
                return('ship3')
        elif ship4. collidepoint((mx, my)):
            if click==True:
                ship4=True
                return('ship4')
        elif ship5. collidepoint((mx, my)):
            if click==True:
                ship4=True
                return('ship5')

        #Set click to false
        click=False

        #Update the display
        pygame.display.update()
      
def choose_ship2():
    #Set run and click to false 
    run=True
    click=False

    #While run is true keep looping
    while run==True:

        #Display the background
        WIN.blit(background,(0, 0))

        #Set the font and word
        font = pygame.font.SysFont('ComicSans', 50)
        word= font.render('CHOOSE YOUR SHIP PLAYER 2', True, WHITE)

        #Display the word
        WIN.blit(word, (WIDTH/2-word.get_width()/2, 0))

        #Track mouse coordinates
        mx, my= pygame.mouse.get_pos()

        #Display all 5 ships
        WIN.blit(RED_SPACESHIP,(200, HEIGHT/2 - word.get_height()/2))
        WIN.blit(YELLOW_SPACESHIP,(300, HEIGHT/2 - word.get_height()/2))
        WIN.blit(SCOUT_SHIP,(400, HEIGHT/2 - word.get_height()/2) )
        WIN.blit(TANK_SHIP,(500, HEIGHT/2 - word.get_height()/2) )
        WIN.blit(MEDICAL_SHIP,(600, HEIGHT/2 - word.get_height()/2) )

        #Rect all 5 ships
        ship1=pygame.Rect(200, HEIGHT/2 - word.get_height()/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        ship2=pygame.Rect(300, HEIGHT/2 - word.get_height()/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        ship3=pygame.Rect(400, HEIGHT/2 - word.get_height()/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        ship4=pygame.Rect(500, HEIGHT/2 - word.get_height()/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        ship5=pygame.Rect(600, HEIGHT/2 - word.get_height()/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
      
        #Let the user leave the game if they want, if they left click on their mouse, set click to true      
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    click=True
                  
        #Check if mouse coordinates are on a ship and if user click is true, return the ship they chose
        if ship1. collidepoint((mx, my)):
            if click==True:
                return('ship1')
        elif ship2. collidepoint((mx, my)):
            if click==True:
                return('ship2')
        elif ship3. collidepoint((mx, my)):
            if click==True:
                ship3=True
                return('ship3')
        elif ship4. collidepoint((mx, my)):
            if click==True:
                ship4=True
                return('ship4')
        elif ship5. collidepoint((mx, my)):
            if click==True:
                ship4=True
                return('ship5')

        #Set click to false
        click=False

        #Update the display
        pygame.display.update()


#Set player 1 ship and player 2 ship
def set_ships(player1, player2):
    #Global player 1 and player 2 spaceships
    global PLAYER2_SPACESHIP, PLAYER1_SPACESHIP

    #If player 2 chooses ship1, set player 2 ship to red ship. Set speed to 5, bullet speed to 10, bullet damage to 10, max bullets to 4, health to 100, and player 2 size to 790
    if player2=='ship1': 
        PLAYER2_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 90)
        player2_vel=5
        player2_bullet_vel=10
        player2_damage=10
        player2_max_bullets=4
        player2_health=100
        player2_health_bar_size=790
    #If player 2 chooses ship2, set player 2 ship to yellow ship. Set speed to 5, bullet speed to 10, bullet damage to 10, max bullets to 4, health to 100, and player 2 health size to 790
    if player2=='ship2':
        PLAYER2_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP,90)
        player2_vel=5
        player2_bullet_vel=10
        player2_damage=10
        player2_max_bullets=4
        player2_health=100
        player2_health_bar_size=790
    #If player 2 chooses ship3, set player 2 ship to scout ship. Set speed to 7, bullet speed to 15, bullet damage to 7, max bullets to 3, health to 100, and player 2 health size to 790
    if player2=='ship3':
        PLAYER2_SPACESHIP = pygame.transform.rotate(SCOUT_SHIP,90)
        player2_vel=7
        player2_bullet_vel=15
        player2_damage=7
        player2_max_bullets=3
        player2_health=100
        player2_health_bar_size=790
    #If player 2 chooses ship4, set player 2 ship to TANK ship. Set speed to 5, bullet speed to 5, bullet damage to 20, max bullets to 3, health to 100, and player 2 health size to 790
    if player2=='ship4':
        PLAYER2_SPACESHIP = pygame.transform.rotate(TANK_SHIP,90)
        player2_vel=5
        player2_bullet_vel=7
        player2_damage=20
        player2_max_bullets=3
        player2_health=100
        player2_health_bar_size=790
    #If player 2 chooses ship5, set player 2 ship to medical ship. Set speed to 5, bullet speed to 10, bullet damage to 7, max bullets to 5, health to 150, and player 2 health bar size to 740
    if player2=='ship5':
        PLAYER2_SPACESHIP = pygame.transform.rotate(MEDICAL_SHIP,90)
        player2_vel=5
        player2_bullet_vel=10
        player2_damage=7
        player2_max_bullets=5
        player2_health=150
        player2_health_bar_size=740
    #If player 1 chooses ship1, set player 1 ship to red ship. Set speed to 5, bullet speed to 10, bullet damage to 10, max bullets to 4, health to 100, and player 2 size to 790
    if player1=='ship1': 
        PLAYER1_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP,270)
        player1_vel=5
        player1_bullet_vel=10
        player1_damage=10
        player1_max_bullets=4
        player1_health=100
    #If player 1 chooses ship2, set player 1 ship to yellow ship. Set speed to 5, bullet speed to 10, bullet damage to 10, max bullets to 4, health to 100, and player 2 size to 790
    if player1=='ship2':
        PLAYER1_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP,270)
        player1_vel=5
        player1_bullet_vel=10
        player1_damage=10
        player1_max_bullets=4
        player1_health=100
    #If player 1 chooses ship3, set player 1 ship to scout ship. Set speed to 7, bullet speed to 15, bullet damage to 7, max bullets to 3, health to 100, and player 2 health size to 790
    if player1=='ship3':
        PLAYER1_SPACESHIP = pygame.transform.rotate(SCOUT_SHIP,270)
        player1_vel=7
        player1_bullet_vel=15
        player1_damage=7
        player1_max_bullets=3
        player1_health=100
    #If player 1 chooses ship 4, set player 1 ship to scout ship. Set speed to 7, bullet speed to 15, bullet damage to 7, max bullets to 3, health to 100, and player 2 health size to 790
    if player1=='ship4':
        PLAYER1_SPACESHIP = pygame.transform.rotate(TANK_SHIP,270)
        player1_vel=5
        player1_bullet_vel=7
        player1_damage=20
        player1_max_bullets=3
        player1_health=100
    #If player 1 chooses ship5, set player 1 ship to medical ship. Set speed to 5, bullet speed to 10, bullet damage to 7, max bullets to 5, health to 150, and player 2 health bar size to 740
    if player1=='ship5':
        PLAYER1_SPACESHIP = pygame.transform.rotate(MEDICAL_SHIP,270)
        player1_vel=5
        player1_bullet_vel=10
        player1_damage=7
        player1_max_bullets=5
        player1_health=150
    #return player 1 speed, bullet speed, bullet damage, max bullets, health and player 2 speed, bullet speed, bullet damage, max bullets, health, and bar size
    return(player1_health, player2_health,player1_bullet_vel, player2_bullet_vel,player1_vel, player2_vel, player2_health_bar_size, player1_damage, player2_damage, player1_max_bullets, player2_max_bullets)
    
#Check if a player got the speed boost
def speed_boost_check(speed, player1_pos, player2_pos, speed_buff_x,speed_buff_y):
  #If player 1 got speed boost
  if player1_pos.colliderect(speed):
        #Return player 1 speed boost check true and player 2 speed boost check false
        player1_speed_boost_check=True
        player2_speed_boost_check=False
        return(player1_speed_boost_check,player2_speed_boost_check)
  #If player 2 got speed
  if player2_pos.colliderect(speed):
        #Return player 1 speed boost check false and player 2 speed boost check True
        player1_speed_boost_check=False
        player2_speed_boost_check=True
        return(player1_speed_boost_check,player2_speed_boost_check)
  #Else return player 1 speed boost check and player 2 speed boost check as false
  else:
      player1_speed_boost_check=False
      player2_speed_boost_check=False
      return(player1_speed_boost_check, player2_speed_boost_check)

#Set speed
def set_speed(player1_check_boost,player2_check_boost,player1_vel,player2_vel,player1_bullet_vel,player2_bullet_vel):
      #if player 1 boost is true, set player 1 boost to true and player 2 boost to false and increase player 1 speed by 2, bullet speed by 20
      if player1_check_boost==True:
        player1_speed_boost=True
        player2_speed_boost=False
        player1_vel=player1_vel+2
        player1_bullet_vel+=10
        player2_vel+=0
        player2_bullet_vel+=0
      #if player 2 boost is true,set player 1 boost to false and player 2 boost to true and increase player 2 speed by 2 and bullet speed by 20
      elif player2_check_boost==True:
        player2_speed_boost=True
        player1_speed_boost=False
        player2_vel+=2
        player2_bullet_vel+=10
        player1_vel+=0
        player1_bullet_vel+=0
      #Return player 1 speed boost, player 2 speed boost, speed, bullet speed
      return(player1_speed_boost, player2_speed_boost,player1_vel, player2_vel, player1_bullet_vel, player2_bullet_vel)

#Check if a player got the buff
def set_buff_check(buff_rect, player1_pos, player2_pos, buff_x, buff_y):
  #If player 1 get buff, return player 1 buff true and player 2buff false
  if player1_pos.colliderect(buff_rect):
    player1_buff=True
    player2_buff=False
    return(player1_buff,player2_buff)
  #If player 1 get buff, return player 2 buff true and player 1 buff false
  elif player2_pos.colliderect(buff_rect):
    player1_buff=False
    player2_buff=True
    return(player1_buff,player2_buff)
  ##Else return false
  else:
    return(False,False)

#Set damage
def set_damage(player1_check_buff, player2_check_buff, player1_damage, player2_damage):
  #if player 1 check buff is true, set player 1 buff to true and player 2 buff to false and increase player 1 damage by 10
  if player1_check_buff==True:
    player1_buff=True
    player2_buff=False
    player1_damage+=10
    player2_damage+=0
  #if player 2 check buff is true, set player 2 buff to true and player 1 buff to false and increase player 2 damage by 10
  elif player2_check_buff==True:
    player1_buff=False
    player2_buff=True
    player1_damage+=0
    player2_damage+=10
  #return player 1 damage, player 2 damage, player 1 buff and player 2 buff
  return(player1_damage, player2_damage, player1_buff, player2_buff)
  

#Set heal
def heal(player1_pos, player2_pos,HEAL):
  #global healing, heal coordinates 
  global healing, heal_x, heal_y
  #If player 1 gets the heal, set heal coordinates off screen and healing to true. Return the amount player 1 will be healed by
  if player1_pos.colliderect(HEAL):
    heal_x=-100
    heal_y=-100
    player1_heal=10
    player2_heal=0
    healing=True
    return(player1_heal,player2_heal)
  #If player 2 gets the heal, set heal coordinates off screen and healing to true. Return the amount player 2 will be healed by
  elif player2_pos.colliderect(HEAL):
    heal_x=-100
    heal_y=-100
    player1_heal=0
    player2_heal=10
    healing=True
    return(player1_heal,player2_heal)
  #Else, set healing to false and return 0
  else:
    healing=False
    player1_heal=0
    player2_heal=0
    return(player1_heal,player2_heal)

def main():
  #Global background, bullet speed, speed, damage, heal coordinates, buff coordinates, speed available, buff available, player speed boost, and max bullets
  global background, player1_bullet_vel, player2_bullet_vel, player1_vel, player2_vel, player1_damage, player2_damage, heal_x, heal_y, buff_x, buff_y, speed_available, buff_available, player1_speed_boost, player2_speed_boost, player1_max_bullets,player2_max_bullets

  #Choose a random background
  background=random.choice(backgrounds)

  main_menu()

  #Set the player to the ship they choose
  PLAYER1=choose_ship1()
  PLAYER2=choose_ship2()

  #Get player healths, speed, bullet speed, health bar size, damage and max bullets
  player1_health, player2_health, player1_bullet_vel, player2_bullet_vel, player1_vel, player2_vel, player2_health_bar_size, player1_damage, player2_damage, player1_max_bullets,player2_max_bullets=set_ships(PLAYER1, PLAYER2)

  #Rect player 1 and player 2 postion
  player2_pos= pygame.Rect(700,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
  player1_pos= pygame.Rect(100,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

  #Set frame count to 0
  frame_count=0

  #Set all powerups all off the screen
  speed_buff_x=-100
  speed_buff_y=-100
  heal_x=-100
  heal_y=-100
  buff_x=-100
  buff_y=-100

  #Define player 1 and player 2 list
  player2_bullets=[]
  player1_bullets=[]

  #Set speed available and buff available to false
  speed_available=False
  buff_available=False

  #Set player 1 speed and player 2 speed to false
  player1_speed_boost=False
  player2_speed_boost=False

  #Set player 1 buff and player 2 buff to false
  player1_buff=False
  player2_buff=False

  #Keep track of time
  clock = pygame.time.Clock()

  #Set buff timer and speed_buff timer to 0
  buff_timer=0
  speed_buff_timer=0

  #Set run to true
  run = True       

  #While run is true, keep looping
  while run:
    #Set frame rate to 60
    clock.tick(FPS)

    #Count the frames
    frame_count+=1

    #Every 900 frames, give a random coordinate to the speed buff and set speed_available to true
    if frame_count%900==0:
      speed_buff_x=random.randint(30,870)
      speed_buff_y=random.randint(30,470)
      speed_available=True
    #Every 800 frames, give a random coordinate to the heal
    if frame_count%800==0:
      heal_x=random.randint(30,870)
      heal_y=random.randint(30,470)
    #Every 800 frames, give a random coordinate to buff and set buff_available to true
    if frame_count % 800==0:
      buff_x=random.randint(30,870)
      buff_y=random.randint(30,470)
      buff_available=True


    #Rect heal, buff, and speed
    heal_rect= pygame.Rect(heal_x,heal_y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    buff_rect=pygame.Rect(buff_x,buff_y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    speed= pygame.Rect(speed_buff_x,speed_buff_y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    #Heal player 1 and player 2by their heal amount 
    player1_heal_amount, player2_heal_amount=heal(player1_pos,player2_pos,heal_rect)
    player1_health+=player1_heal_amount
    player2_health+=player2_heal_amount
    player2_health_bar_size-=player2_heal_amount

    #Get event
    for event in pygame.event.get():
      #Allow the player to exit
      if event.type==pygame.QUIT:
        run=False
        pygame.quit()
        
      #If the player presses a button 
      if event.type == pygame.KEYDOWN:
        #If the player presses tab and did not run out of bullet, rect the bullet and add it to a list. Then, play the fire sound
        if event.key == pygame.K_TAB and len(player1_bullets) < player1_max_bullets:
          bullet=pygame.Rect( player1_pos.x,  player1_pos.y+ player1_pos.height//2 - 17, 10,5)
          player1_bullets.append(bullet)
          BULLET_FIRE_SOUND.play()
        #If the player presses tab and did not run out of bullet, rect the bullet and add it to a list. Then, play the fire sound
        if event.key == pygame.K_RETURN and len(player2_bullets) < player2_max_bullets:
          bullet=pygame.Rect( player2_pos.x,  player2_pos.y+ player2_pos.height//2 - 2, 10,5)
          player2_bullets.append(bullet)
          BULLET_FIRE_SOUND.play()
      #If player 2 is hit, decrease the health by player 1 damage and play bullet hit sound
      if event.type == PLAYER2_HIT:
          player2_health-=player1_damage
          player2_health_bar_size+=player1_damage
          BULLET_HIT_SOUND.play()
      #If player 1 is hit, decrease the health by player 2 damage and play bullet hit sound
      if event.type == PLAYER1_HIT:
          player1_health-=player2_damage
          BULLET_HIT_SOUND.play()

    #Rect player 1 and player 2 health bar  
    PLAYER1_HEALTH_BAR=pygame.Rect(10,10,player1_health,20)
    PLAYER2_HEALTH_BAR=pygame.Rect(player2_health_bar_size,10,player2_health,20)

    #Handle player movement
    keys_pressed=pygame.key.get_pressed()
    player1_handle_movement(keys_pressed,player1_pos)
    player2_handle_movement(keys_pressed, player2_pos)

    #If speed is available check if a player has gotten the speed boost
    if speed_available==True:
      player1_check_boost,player2_check_boost=speed_boost_check(speed, player1_pos, player2_pos, speed_buff_x, speed_buff_y)
      #If a player got the boost, set speed
      if player1_check_boost==True or player2_check_boost==True:
        player1_speed_boost, player2_speed_boost,player1_vel,player2_vel, player1_bullet_vel, player2_bullet_vel=set_speed(player1_check_boost,player2_check_boost,player1_vel,player2_vel, player1_bullet_vel, player2_bullet_vel)

    #If buff is available check if a player has gotten the buff   
    if buff_available==True:
      player1_check_buff, player2_check_buff=set_buff_check(buff_rect, player1_pos, player2_pos, buff_x, buff_y)
      #If a player got the buff, set damage
      if player1_check_buff==True or player2_check_buff==True:
        player1_damage, player2_damage, player1_buff, player2_buff=set_damage(player1_check_buff, player2_check_buff, player1_damage,player2_damage)  

    #If player 1 has the buff, hide the buff and turn on the timer. If 10 seconds has passed, turn off the buff and reset player damage and timer. Turn off buff_available
    if player1_buff==True:
      buff_timer+=1
      buff_x=-100
      buff_y=-100
      if buff_timer==600:
          buff_available=False
          player1_buff=False
          player1_damage-=10
          buff_timer=0
    #If player 2 has the buff, hide the buff and turn on the timer. If 10 seconds has passed, turn off the buff and reset player damage and timer. Set buff availabe to off.
    if player2_buff==True:
      buff_timer+=1
      buff_x=-100
      buff_y=-100
      if buff_timer==600:
          buff_available=False
          player2_buff=False
          player2_damage-=10
          buff_timer=0
        
      
    #If player 1 has the speed buff, hide the speed buff buff and turn on the timer. If 10 seconds has passed, turn off the buff and reset player speed and bullet vel and timer. Set speed available to false.    
    if player1_speed_boost==True:
        speed_buff_timer+=1
        speed_buff_x=-100
        speed_buff_y=-100
        if speed_buff_timer==600:
          speed_available=False
          player1_vel=player1_vel-2
          player1_bullet_vel=player1_bullet_vel-10
          player1_speed_boost=False
          speed_buff_timer=0
    #If player 1 has the speed buff, hide the speed buff buff and turn on the timer. If 10 seconds has passed, turn off the buff and reset player speed and bullet vel and timer. Set speed available to false. 
    if player2_speed_boost==True:
        speed_buff_timer+=1
        speed_buff_x=-100
        speed_buff_y=-100
        if speed_buff_timer==600:
          speed_available=False
          player2_vel=player2_vel-2
          player2_bullet_vel=player2_bullet_vel-10
          player2_speed_boost=False
          speed_buff_timer=0

    #Handle bullets
    handle_bullets(player1_bullets, player2_bullets, player1_pos, player2_pos, player1_bullet_vel, player2_bullet_vel)

    #Draw all the components to the screen
    draw_window(player2_pos,player1_pos, PLAYER1, PLAYER2,player2_bullets, player1_bullets, PLAYER2_HEALTH_BAR,PLAYER1_HEALTH_BAR, speed_buff_x,speed_buff_y, buff_x, buff_y)

    #Check who wins and display it
    winner_text = ''
    if player2_health<=0:
      winner_text="PLAYER 1 WINS!"  
    if player1_health<=0:
      winner_text="PLAYER 2 WINS" 
    if winner_text!='':
      draw_winner(winner_text)
      break
      
  #Reset
  main()


#Play game
if __name__ == "__main__":
  main()



