import pygame
pygame.init()
size = 600, 600
screen=pygame.display.set_mode(size)
pygame.display.set_caption('ping-pong')
def borders():
    pygame.draw.rect(screen, 0, 255, 0, (0, 0, 600, 25))
    pygame.draw.rect(screen, 0, 255, 0, (0, 600, 600, 25))
def objects():
    pygame.draw.rect(screen, 255, 255, 255, (15, 250, 10, 25))
    pygame.draw.rect(screen, 255, 255, 255, (585, 250, -10, 25))
    pygame.draw.rect(screen, 255, 255, 255, (300, 300, 0, 0))
clock = pygame.time.Clock()
running = True
sp = 5
sp1 = 2
p = 300
p1 = 250
c = 0, 0, 0
while running:
    clock.tick(15)
    screen.fill(c)
    borders()
    objects()
    pygame.display.flip()
    events = pygame.event.get()
    if p == 15+10:
        if p > p1:
            if p < p1+25:
                sp *= -1
    if p == 685-10:
        if p > p1:
            if p < p1+25:
                sp *= -1
    if p < 25 or p > 600-25:
        sp1 *= -1
    p += sp
    p += sp1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and  p1 > 25:
        p1 -= 6
    if keys[pygame.K_s] and  p1 < 575 - 25 -6 :
        p1 += 6
    if keys[pygame.K_UP] and p1> 25:
        p1 -= 6
    if keys[pygame.K_DOWN] and p1 < 550 - 25 - 6:
        p1 += 6
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
pygame.quit()