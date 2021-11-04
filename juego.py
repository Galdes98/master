import pygame
pygame.init()

screenWidth = 500
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("First Game")

x = 50
y = 400
width = 64
height = 64
vel = 10
delayTime = 10
bckr = 0
bckg = 0
bckb = 0

isJump = False
jumpCount = 10

#mainloop
run = True
while run:
    pygame.time.delay(delayTime)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth - width:
        x += vel
    if not(isJump):
        """if keys[pygame.K_UP] and y >= vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screenHeight - height:
            y += vel"""
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:            
            isJump = False
            jumpCount = 10
        

    win.fill((bckr,bckg,bckb))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()            
