import pygame
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

circle_x = 20
circle_y = 20
move_x = 1
while True:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #pygame.draw.rect(screen,blue,[W//2-25,H//2-25,50,50])
    pygame.draw.circle(screen,red,[circle_x,circle_y],20)
    circle_x+=move_x
    pygame.display.flip()
