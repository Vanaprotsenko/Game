import pygame

pygame.init()
win=pygame.display.set_mode((500, 500))

pygame.display.set_caption("New game")

walkRight=[pygame.image.load('D:\\Python\\1_right.png')],
pygame.image.load('D:\\Python\\2_right.png'),pygame.image.load('D:\\Python\\2_right.png')


walkLeft=[pygame.image.load('D:\\Python\\1_left.png')],
pygame.image.load('D:\\Python\\2_left.png'),pygame.image.load('D:\\Python\\3_left.png')

playerStand=pygame.image.load('D:\\Python\\1_right.png')
bg=pygame.image.load('D:\\Python\\bg2.png')

clock=pygame.time.Clock()

x=50
y=425
width=60
height=71
speed=5

isJump=False
jumpCount=10


left=False
right=False
animCount=0


def drawWindow():
    global animCount
    win.blit(bg,(0,0))

    if animCount +1>=30:
        animCount =0

    if left:
        win.blit(walkLeft[animCount//5],(x,y))
        animCount +=1
    elif right:
        win.blit(walkRight[animCount//5],(x,y))
        animCount +=1

    else:
        win.blit(playerStand(x,y))


    
    pygame.display.update()

run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>5:
        x-=speed
        left=True
        right=False
    elif keys[pygame.K_RIGHT] and x<500-width-5:
        x+=speed
        left=False
        right=True

    else:
        left= False
        right= False
        animCount=0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump=True
    else:
        if jumpCount>=-10:
            if jumpCount<0:
                 y+=(jumpCount**2)/2
            else:
                 y-=(jumpCount**2)/2
            jumpCount-=1

        else:
            isJump=False
            jumpCount=10

drawWindow()
    
    


pygame.quit()


