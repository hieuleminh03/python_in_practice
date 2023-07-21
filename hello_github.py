import pygame 

pygame.init()

screen = pygame.display.set_mode((500,500))

GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (19,22,34)
running = True

while running:
    screen.fill(GREY)

    pygame.draw.rect(screen, WHITE, (100,50,50,50))
    pygame.draw.rect(screen, WHITE, ( 200,50,50,50))
    pygame.draw.rect(screen, WHITE, (300,50,100,50))
    pygame.draw.rect(screen, WHITE, (100,150,50,50))
    pygame.draw.rect(screen, WHITE, (200,150,50,50))
    pygame.draw.rect(screen, WHITE, (300,150,100,50))

    pygame.draw.circle(screen, WHITE, (225,360), 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print('abc')

    pygame.display.flip()

pygame.quit()