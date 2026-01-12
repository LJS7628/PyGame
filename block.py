""" blocks.py - Copyright 2016 Kenichiro Tanaka """
import sys,time
import math
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, Rect


class Block:
    """ 블록, 공, 패들 오브젝트 """
    def __init__(self, col, rect, speed=0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45, 45) + 270

    def move(self):
        """ 공을 움직인다 """
        self.rect.centerx += math.cos(math.radians(self.dir))\
             * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir))\
             * self.speed

    def draw(self):
        """ 블록, 공, 패들을 그린다 """
        if self.speed == 0:
            pygame.draw.rect(SURFACE, self.col, self.rect)
        else:
            pygame.draw.ellipse(SURFACE, self.col, self.rect)
            

def tick():
    """ 프레임별 처리 """
    global BLOCKS
    global SCORE
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT and PADDLE.rect.topleft[0] > 0:
                PADDLE.rect.centerx -= 10
            elif event.key == K_RIGHT and PADDLE.rect.topright[0] < 600:
                PADDLE.rect.centerx += 10

    if BALL.rect.centery < 1000:
        BALL.move()
    
    if BALL2.rect.centery < 1000:
        BALL2.move()

    # 블록과 충돌?
    prevlen = len(BLOCKS)
    BLOCKS = [x for x in BLOCKS
              if not x.rect.colliderect(BALL.rect)]
        
    if len(BLOCKS) != prevlen:

        if BALL.rect.centerx >=460 and BALL.rect.centerx < 600 :
            BALL2.speed = 5
        if BALL.rect.centerx >=360 and BALL.rect.centerx < 460 :
            BALL2.speed += 3
        if BALL.rect.centerx >=250 and BALL.rect.centerx < 350 \
            and BALL.rect.centery>=130 and BALL.rect.centery<=180:
            BLOCKS.clear()

        BALL.dir *= -1
        SCORE += 100
        mySound1.play()

        if SCORE % 500 == 0 and PADDLE.rect.w > 40:
            PADDLE.rect.w -= 30
        elif PADDLE.rect.w <= 40:
            PADDLE.rect.w = 40

    prevlen = len(BLOCKS)
    BLOCKS = [x for x in BLOCKS
              if not x.rect.colliderect(BALL2.rect)]
    
    if len(BLOCKS) != prevlen:

        if BALL2.rect.centerx >=160 and BALL.rect.centerx < 260 :
            BALL.speed = 5
        if BALL2.rect.centerx >=60 and BALL.rect.centerx < 160 :
            BALL.speed += 3 
        if BALL.rect.centerx >=260 and BALL.rect.centerx < 340 \
            and BALL.rect.centery>=130 and BALL.rect.centery<=180:
            BLOCKS.clear()
        
        BALL2.dir *= -1
        SCORE += 100
        mySound1.play()

        if SCORE % 500 == 0 and PADDLE.rect.w > 40:
            PADDLE.rect.w -= 30
        elif PADDLE.rect.w <= 40:
            PADDLE.rect.w = 40

    if SCORE % 700 == 0 and SCORE !=0:
        PADDLE.rect.w = 100
        

    # 패들과 충돌?
    if PADDLE.rect.colliderect(BALL.rect):
        BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) \
            / PADDLE.rect.width * 80

    if PADDLE.rect.colliderect(BALL2.rect):
        BALL2.dir = 90 + (PADDLE.rect.centerx - BALL2.rect.centerx) \
            / PADDLE.rect.width * 80
        
    # 벽과 충돌?
    if BALL.rect.centerx < 0 or BALL.rect.centerx > 600:
        BALL.dir = 180 - BALL.dir
    if BALL.rect.centery < 0:
        BALL.dir = -BALL.dir
        

    if BALL2.rect.centerx < 0 or BALL2.rect.centerx > 600:
        BALL2.dir = 180 - BALL2.dir
    if BALL2.rect.centery < 0:
        BALL2.dir = -BALL2.dir
        

def next_stage():
    global STAGE, PADDLE, BALL, BALL2
    mySound2.stop()
    STAGE += 1
    colors = [(255, 0, 0), (255, 165, 0), (242, 242, 0),
              (0, 128, 0), (128, 0, 128), (0, 0, 250),(64,64,64),(128,255,128)]
    if STAGE == 2 :    
        for ypos, color in enumerate(colors, start=0):
            for xpos in range(0, 5):
                BLOCKS.append(Block(color,Rect(xpos * 100 + 60, ypos * 50 + 40, 50, 30) ))

    elif STAGE == 3 :
        for ypos, color in enumerate(colors, start=0):
            for xpos in range(0, 5):
                BLOCKS.append(Block(color,
                                Rect(xpos * 100 + 60, ypos * 50 + 100, 
                                     30, 50)))
    elif STAGE%3 == 1:
        STAGE = 1
        colors = [(255, 0, 0), (255, 165, 0), (242, 242, 0),
                  (0, 128, 0), (128, 0, 128), (0, 0, 250)]
        for ypos, color in enumerate(colors, start=0):
            for xpos in range(0, 5):
                BLOCKS.append(Block(color,
                                Rect(xpos * 100 + 60, ypos * 50 + 40, 80, 30)))


    PADDLE = Block((242, 242, 0), Rect(230, 700, 160, 30))
    BALL = Block((242, 242, 0), Rect(300, 400, 20, 20), 10) # 공속도=10
    BALL2 = Block((255, 0, 0), Rect(500, 400, 20, 20), 7) # 공속도=10                


           

pygame.init()
pygame.key.set_repeat(15, 15)
SURFACE = pygame.display.set_mode((900, 800))
FPSCLOCK = pygame.time.Clock()
BLOCKS = []
SCORE = 0
PADDLE = Block((242, 242, 0), Rect(230, 700, 160, 30))
BALL = Block((242, 242, 0), Rect(300, 600, 20, 20), 10) 
BALL2 = Block((255, 0, 0), Rect(250, 600, 20, 20), 10)
background = pygame.image.load("background.png")
lens = 1
BALL2.dir = BALL.dir
STAGE = 1


mySound1 = pygame.mixer.Sound("ping.mp3")
mySound2 = pygame.mixer.Sound("pass.mp3")
mySound3 = pygame.mixer.Sound("fail.mp3")

def main():
    """ 메인 루틴 """
    myfont = pygame.font.Font("gamefont.ttf", 80)
    myfont2 = pygame.font.Font("gamefont.ttf",40)
    
    start_ticks = pygame.time.get_ticks()
    



    mess_clear = myfont.render("Cleared!", True, (255, 255, 0))
    mess_over = myfont.render("Game Over!", True, (255, 255, 0))
    fps = 30
    colors = [(255, 0, 0), (255, 165, 0), (242, 242, 0),
              (0, 128, 0), (128, 0, 128), (0, 0, 250)]

    for ypos, color in enumerate(colors, start=0):
        for xpos in range(0, 5):
            BLOCKS.append(Block(color,Rect(xpos * 100 + 60, ypos * 50 + 40, 80, 30)))
         
           
    while True:
        tick()
        SURFACE.fill((0, 0, 0))
        timer = (pygame.time.get_ticks() - start_ticks) / 1000
        elapsed_time = myfont2.render(f'Timer : {timer}',True,(64,64,128))
        score = myfont2.render(f'SCORE : {SCORE}',True,(128,255,0))
        stage = myfont2.render(f'Stage : {STAGE}',True,(0,0,255))
        speed = myfont2.render(f'BALL : {BALL.speed}',True,(255,255,0))
        speed2 = myfont2.render(f'BALL2 : {BALL2.speed}',True,(255,255,0))
        pad = myfont2.render(f'pad : {PADDLE.rect.w}',True,(255,0,0))
        SURFACE.blit(background,(600,0))
        SURFACE.blit(score,(620,100))
        SURFACE.blit(stage,(620,200))
        SURFACE.blit(speed,(620,300))
        SURFACE.blit(speed2,(620,400))
        SURFACE.blit(pad,(620,500))
        SURFACE.blit(elapsed_time,(620,600))
        
        BALL.draw()
        BALL2.draw()
        PADDLE.draw()
        
        for block in BLOCKS:
            block.draw()

        if len(BLOCKS) == 0:
            SURFACE.blit(mess_clear, (200, 400))
            mySound2.play()
            pygame.display.update()
            time.sleep(3)
            next_stage()
        if BALL.rect.centery > 800 and len(BLOCKS) > 0:
            SURFACE.blit(mess_over, (150, 400))
            mySound3.play()
            

        if timer >= 30.0 :
            BALL.speed = 15    

        pygame.display.update()
        FPSCLOCK.tick(fps)

if __name__ == '__main__':
    main()
