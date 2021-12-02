import pygame
pygame.init()
size = 600, 600
screen=pygame.display.set_mode(size)
pygame.display.set_caption('ping-pong')
c = 0, 0, 0
green = 0, 255, 0
white = 255, 255, 255
y_movement1 = 267.5
y_movement2 = 267.5
x_velocity = 300
y_velocity = 300
gy = 25
sp2 = 585
sp1 = 15
def borders():
    pygame.draw.rect(screen, green, (0, 0, 600, gy) )
    pygame.draw.rect(screen, green, (0, 600, 600, -gy))
def objects():
    pygame.draw.rect(screen, white, (sp1, y_movement1, 10, 25))
    pygame.draw.rect(screen, white, (sp2, y_movement2, -10, 25))
    pygame.draw.rect(screen, white, (x_pos, y_pos, 7.5, 7.5))
clock = pygame.time.Clock()
running = True
x_pos = 300
y_pos = 300
x_velocity = 5
y_velocity = 2
while running:
    clock.tick(30)
    screen.fill(c)
    borders()
    objects()
    pygame.display.flip()
    events = pygame.event.get()
    if x_pos == sp1+10:
        if y_pos > y_movement1:
            if y_pos < y_movement1+25:
                x_velocity *= -1
    if x_pos == sp2-10:
        if y_pos > y_movement2:
            if y_pos < y_movement2+25:
                x_velocity *= -1
    if y_pos < gy or y_pos > 600-gy:
        y_velocity *= -1
    x_pos += x_velocity
    y_pos += y_velocity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and  y_movement1 > 25:
        y_movement1 -= 6
    if keys[pygame.K_s] and  y_movement1 < 575 - 25 -6 :
        y_movement1 += 6
    if keys[pygame.K_UP] and y_movement2 > 25:
        y_movement2 -= 6
    if keys[pygame.K_DOWN] and y_movement2 < 550 - 25 - 6:
        y_movement2 += 6
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
pygame.quit()