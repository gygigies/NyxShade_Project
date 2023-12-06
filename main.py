import pygame
import math
import random
import os

pygame.init()

#color
white = (0,0,0)
black = (255,255,255)
red = (255, 0, 0)
green = (92, 145, 101)
colorr = (153, 51, 0)

#Screen and Display
screen = pygame.display.set_mode((800 , 800))

#Set captions && icon
pygame.display.set_caption("NyxShade")
icon_load = pygame.image.load("icon.png")
pygame.display.set_icon(icon_load)

#Font
font = pygame.font.Font('TF.TTF',30)
#Player Download
Player_Size = (80,80)
Player_Back_Load = pygame.image.load("FaceBack.png")
Player_Right_Load = pygame.image.load("FaceRight.png")
Player_Left_Load = pygame.image.load("FaceLeft.png")
Player_Front_Load = pygame.image.load("FaceFront.png")
Player_Back = pygame.transform.scale(Player_Back_Load , Player_Size)
Player_Right = pygame.transform.scale(Player_Right_Load , Player_Size)
Player_Left = pygame.transform.scale(Player_Left_Load , Player_Size)
Player_Front = pygame.transform.scale(Player_Front_Load , Player_Size)
HitBox = pygame.mask.from_surface(Player_Back)
HitBox2 = pygame.mask.from_surface(Player_Right)
HitBox3 = pygame.mask.from_surface(Player_Left)
Show_Hitbox_Back = HitBox.to_surface()
Show_Hitbox_Right = HitBox2.to_surface()
Show_Hitbox_Left = HitBox3.to_surface()

#cursur
show_cursur = True
cursur = pygame.image.load("cursor.png")
pygame.mouse.set_visible(False)

#Intro Button
start_button = pygame.image.load("Start.png")
start_button_size = pygame.transform.scale(start_button , (300,300))

#Bullet
bulletImg_load = pygame.image.load("bullet.png")
bulletImgSize = (30,30)
BulletImg = pygame.transform.scale(bulletImg_load , bulletImgSize)
Bullet_Hitbox = pygame.mask.from_surface(BulletImg)

#Enemy
enemyImg = pygame.image.load("EnemyImg.png")
enemyImgSize = (60,60)
Enemy_Img = pygame.transform.scale(enemyImg , enemyImgSize)
enemy_num = 5
EnemyImg_Show = []
Enemy_Hitbox = pygame.mask.from_surface(Enemy_Img)
Show_Enemy_Hitbox = Enemy_Hitbox.to_surface()

#Background
intro_bg = pygame.image.load('test.png')
intro_mBackground = pygame.transform.scale(intro_bg , (1200,1000))
bg = pygame.image.load('MAP1.png')
bg2 = pygame.image.load('MAP2.png')
bg3 = pygame.image.load('MAP3.png')
bg4 = pygame.image.load('MAP4.png')
mBackground = pygame.transform.scale(bg , (800,800))
sBackground1 = pygame.transform.scale(bg2 , (800,800))
sBackground2 = pygame.transform.scale(bg3 , (800,800))
sBackground3 = pygame.transform.scale(bg4 , (800,800))

#hp
hp_3_load = pygame.image.load('hp3.png')
hp_2_load = pygame.image.load('hp2.png')
hp_1_load = pygame.image.load('hp1.png')
hp3 = pygame.transform.scale(hp_3_load , (160,65))
hp2 = pygame.transform.scale(hp_2_load , (160,65))
hp1 = pygame.transform.scale(hp_1_load , (160,65))

def Enemy(x,y,i):
    for l in range(enemy_num):
        EnemyImg_Show.append(Enemy_Img)
    screen.blit(EnemyImg_Show[i],(x,y))


def text_text(text ,x,y,size):
    largeText = pygame.font.Font('TF.TTF',size)
    TextSurf, TextRect = text_object(text , largeText)
    TextRect.center = (x,y)
    return screen.blit(TextSurf , TextRect)


def text_object(text , font):
    textSurface = font.render(text , True , black)
    return textSurface, textSurface.get_rect()

def text_rim(text , font):
    textSurface = font.render(text , True , colorr)
    return textSurface, textSurface.get_rect()

def firebullet(x,y):
    global bullet_state
    bullet_state = True

def Collision(player_x, player_y, enemy_x, enemy_y, i):
    collision_status = False
    for j in range(enemy_num):
        offset = (enemy_x[j] - (player_x - 37), enemy_y[j] - (player_y - 45))
        if HitBox.overlap(Enemy_Hitbox, offset):
            collision_status = True
            enemy_x[j] = random.randint(0,800)
            enemy_y[j] = random.randint(0,800)

    if collision_status:
        return True
    else:
        return False

def Dead(bullet_x, bullet_y, enemy_x, enemy_y):
    dead_status = False
    for j in range(enemy_num):
        if Bullet_Hitbox.overlap(Enemy_Hitbox, (enemy_x[j] - (bullet_x), enemy_y[j] - (bullet_y))):
            dead_status = True
            # Respawn the dead enemy
            enemy_x[j] = random.randint(0, 800)
            enemy_y[j] = random.randint(0, 800)

    if dead_status:
        return False

def gameover():
    over = True

    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    game_intro()

        text_text("GAME OVER" , 400,350,100 )
        text_text("Press R to restart or M to menu" , 400,420,40 )
        pygame.display.update()
            
def button(msg , x, y, w, h ,ac ,ic ,action=None) :
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()
    
    smallText = pygame.font.Font( 'TF.TTF', 80)
    textSurf , textRect = text_object(msg , smallText)
    textRect.center = (x + (w/2), (y+ (h/2)))
    screen.blit(textSurf , textRect ) 

def paused():

    pygame.mixer.music.pause()
    text_text("Paused" , 400,350,100 )
    text_text("Press P to continue or M to menu" , 400,420,40 )

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause_check = False
                    unpause()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    pause_check = False
                    game_intro()

        pygame.display.update()
        
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    
#test bullet


def game_intro():
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(intro_mBackground , (-100,-200))
        screen.blit(start_button_size , (248,325))
        screen.blit(start_button_size , (248,468))
        button("START", 300,408,200,100 , white , red , main )
        button("EXIT", 300,548,200,100 , white , red , quit_game )
        text_text("NYX", 315,205,125 )
        text_text("SHADE" , 450,280,125 )
        cur_pos = pygame.mouse.get_pos()
        screen.blit(cursur, cur_pos)
        pygame.display.update()

def quit_game():
    pygame.quit()
    quit()

def main():

    global pause,hp
    global score

    #Player
    player_x = 400
    player_y = 400
    player_x_change = 0
    player_y_change = 0
    player_left = 0
    player_right = 0
    player_up = 0
    player_down = 0
    up = False
    down = True
    left = False
    right = False

    #Bullet
    bullet_x = 0
    bullet_y = 0
    bullet_x_change = 0
    bullet_y_change = 0
    bullet_state = False
    bullet_x2 = 0
    bullet_y2 = 0
    bullet_x_change2 = 0
    bullet_y_change2 = 0
    bullet_state2 = False
    bullet_x3 = 0
    bullet_y3 = 0
    bullet_x_change3 = 0
    bullet_y_change3 = 0
    bullet_state3 = False
    bulletshoot = False
    bulletshoot2 = False
    
    #Enemy
    enemy_x = []
    enemy_y = []
    enemy_x_change = []
    enemy_y_change = []
    enemy_speed = 0.75
    for i in range(enemy_num):
        for i in range(enemy_num):
            if i % 4 == 0:  # Top side
                enemy_x.append(random.randint(0,800))
                enemy_y.append(random.randint(0,100))
            elif i % 4 == 1:  # Bottom side
                enemy_x.append(random.randint(0,800))
                enemy_y.append(random.randint(700,800))
            elif i % 4 == 2:  # Left side
                enemy_x.append(random.randint(0,100))
                enemy_y.append(random.randint(0,800))
            elif i % 4 == 3:  # Right side
                enemy_x.append(random.randint(700,800))
                enemy_y.append(random.randint(0,800))
        enemy_x_change.append(0)
        enemy_y_change.append(0)

    #Pause
    pause_check = False
    
    score = 0
    hp = 3

    #Loop
    while True:
        
        #score
        if score < 20:
            screen.blit(mBackground , (0,0) )
            enemy_speed = 0.50
        elif 20 <= score < 30:
            screen.blit(sBackground1 , (0,0) )
            enemy_speed = 1
        elif 30 <= score < 40:
            screen.blit(sBackground2 , (0,0) )
            enemy_speed = 1.5
        elif 40 <= score:
            screen.blit(sBackground3 , (0,0) )
            enemy_speed = 2

        #hp
        if hp == 3 :
            screen.blit(hp3 , (600,5) )
        if hp == 2:
            screen.blit(hp2 , (600,5) )
        if hp == 1 :
            screen.blit(hp1 , (600,5) )
        if hp <= 0:
            gameover()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
            if event.type == pygame.KEYDOWN:
                #Player Movement
                if event.key == pygame.K_d:
                    player_right = 3
                    player_up = 0
                    player_down = 0
                    right = True
                    left = False
                    down = False
                    up = False
                if event.key == pygame.K_a:
                    player_left = 3
                    player_up = 0
                    player_down = 0
                    right = False
                    left = True
                    down = False
                    up = False
                if event.key == pygame.K_w:
                    player_up = 3
                    player_right = 0
                    player_left = 0
                    right = False
                    left = False
                    down = False
                    up = True
                if event.key == pygame.K_s:
                    player_down = 3
                    player_right = 0
                    player_left = 0
                    right = False
                    left = False
                    down = True
                    up = False

        
                #Bullet
                    #Shoot
                if event.key == pygame.K_j:
                    bullet_state = True
                if event.key == pygame.K_j and bulletshoot:
                    bullet_state2 = True
                if event.key == pygame.K_j and bulletshoot2:
                    bullet_state3 = True
                    

                #Pause
                if event.key == pygame.K_p and pause_check == False:
                    pause = True
                    paused()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player_right = 0
                if event.key == pygame.K_a:
                    player_left = 0
                if event.key == pygame.K_w:
                    player_up = 0
                if event.key == pygame.K_s:
                    player_down = 0
                if event.key == pygame.K_j and bullet_state:
                    bulletshoot = True
                if event.key == pygame.K_j and bullet_state2:
                    bulletshoot2 = True
        
            

        #MOVEMENT
        player_x_change = player_right-player_left
        player_y_change = player_down-player_up
        player_x += player_x_change
        player_y += player_y_change
        if player_x >= 720:
            player_x = 720
        if player_x <= 60:
            player_x = 60
        if player_y >= 705:
            player_y = 705
        if player_y <= 60:
            player_y = 60
        player_place = (player_x-30,player_y-40)

        if(right):
            screen.blit(Player_Right , player_place )
        elif(left):
            screen.blit(Player_Left , player_place )
        elif(up):
            screen.blit(Player_Back , player_place )
        elif(down):
            screen.blit(Player_Front , player_place )

        
        #Bullet
        if(bullet_state == False):
            bullet_x = player_x
            bullet_y = player_y
            if(up):
                bullet_y_change = -2
                bullet_x_change = 0
            elif(down):
                bullet_y_change = 2
                bullet_x_change = 0
            elif(left):
                bullet_x_change = -2
                bullet_y_change = 0
            elif(right):
                bullet_x_change = 2
                bullet_y_change = 0
        if(bullet_state2 == False):
            bullet_x2 = player_x
            bullet_y2 = player_y
            if(up):
                bullet_y_change2 = -2
                bullet_x_change2 = 0
            elif(down):
                bullet_y_change2 = 2
                bullet_x_change2 = 0
            elif(left):
                bullet_x_change2 = -2
                bullet_y_change2 = 0
            elif(right):
                bullet_x_change2 = 2
                bullet_y_change2 = 0
        if(bullet_state3 == False):
            bullet_x3 = player_x
            bullet_y3 = player_y
            if(up):
                bullet_y_change3 = -2
                bullet_x_change3 = 0
            elif(down):
                bullet_y_change3 = 2
                bullet_x_change3 = 0
            elif(left):
                bullet_x_change3 = -2
                bullet_y_change3 = 0
            elif(right):
                bullet_x_change3 = 2
                bullet_y_change3 = 0
        if(bullet_state):
            bullet_x += bullet_x_change
            bullet_y += bullet_y_change
            screen.blit(BulletImg,(bullet_x,bullet_y))
        if(bullet_state2):
            bullet_x2 += bullet_x_change2
            bullet_y2 += bullet_y_change2
            screen.blit(BulletImg,(bullet_x2,bullet_y2))
        if(bullet_state3):
            bullet_x3 += bullet_x_change3
            bullet_y3 += bullet_y_change3
            screen.blit(BulletImg,(bullet_x3,bullet_y3))
        
        if((bullet_x < 30 or bullet_x > 720 or bullet_y < 0 or bullet_y > 720) ):
            bullet_state = False
            bulletshoot = False
        elif bullet_state:
                if Dead(bullet_x, bullet_y, enemy_x, enemy_y) == False:
                    bullet_state = False
                    bulletshoot = False
                    score += 1
        if(bullet_x2 < 30 or bullet_x2 > 720 or bullet_y2 < 0 or bullet_y2 > 720 ):
            bullet_state2 = False
            bulletshoot2 = False
        elif bullet_state2:
                if Dead(bullet_x2, bullet_y2, enemy_x, enemy_y) == False:
                    bullet_state2 = False
                    bulletshoot2 = False
                    score += 1
        if(bullet_x3 < 30 or bullet_x3 > 720 or bullet_y3 < 0 or bullet_y3 > 720 ):
            bullet_state3 = False
        elif bullet_state3:
                if Dead(bullet_x3, bullet_y3, enemy_x, enemy_y) == False:
                    bullet_state3 = False
                    score += 1
        
        
        #Enemy

        for i in range(enemy_num):
            enemy_change_x = (player_x - 30 - enemy_x[i])
            enemy_change_y = (player_y - 40 - enemy_y[i])
            distance = math.sqrt(enemy_change_x ** 2 + enemy_change_y ** 2)
            enemy_x_change[i] = enemy_change_x/distance*enemy_speed
            enemy_y_change[i] = enemy_change_y/distance*enemy_speed
            enemy_x[i] += enemy_x_change[i]
            enemy_y[i] += enemy_y_change[i]
            Enemy(enemy_x[i], enemy_y[i], i)
        
            col = Collision(player_x, player_y, enemy_x, enemy_y, i)
            if(col):
                hp -= 1

        score_show = font.render('SCORE' + str(score),True,black)
        screen.blit(score_show ,(10,10))
        pygame.display.update()
        

game_intro()
main()

        




        
   
    
    


