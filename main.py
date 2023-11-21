import pygame, sys
pygame.init()

#Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)



#Pantalla
size = (1000, 500)
screen = pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()        
    screen.fill(WHITE)
    
    #! <---- zona de dibujo
    #pygame.draw.line(screen, RED, [100, 100],[100,500], 5)
    for i in range(10,1000,40):
        pygame.draw.circle(screen, BLACK, (i,100), 20 )
    #! <---- zona de dibujo
    
    #actualizar pantalla
    pygame.display.flip()