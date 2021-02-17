import pygame
import random
pygame.init()
W = 1000
H = 500
screen = pygame.display.set_mode((W,H))
#rgb coding - (red(0-255),green(0-255),blue(0-255))
red = 255,0,0
green = 0,255,0
blue = 0,0,255
white = 255,255,255
custom_color = (100,20,40)

x = 20
y = 20
width = 30
height = 30
move_x = 0
move_y = 0
f_x = random.randint(0,W-width)
f_y = random.randint(0,H-height)

frogImg = pygame.image.load("frog.png")

frogImg = pygame.transform.scale(frogImg,(frogImg.get_width()//7,frogImg.get_height()//7))

audio = pygame.mixer.Sound("point.wav")

while True:
    screen.fill(white)
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x = -1
                y += 0
            elif event.key == pygame.K_RIGHT:
                move_x = 1
                move_y = 0

            elif event.key == pygame.K_UP:
                move_x = 0
                move_y = -1
            elif event.key == pygame.K_DOWN:
                move_x = 0
                move_y = 1
        

    snake = pygame.draw.rect(screen,blue,[x,y,width,height])
    frog_rect = pygame.Rect(f_x,f_y,frogImg.get_width(),frogImg.get_height())
    screen.blit(frogImg,(f_x,f_y))
    
    if snake.colliderect(frog_rect):
        f_x = random.randint(0,W-width)
        f_y = random.randint(0,H-height)
        audio.play()
        
    
    x+=move_x
    y+=move_y
    
    pygame.display.flip()
    
    
    
    