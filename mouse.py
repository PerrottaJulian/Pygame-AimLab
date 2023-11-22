import pygame, sys, random
pygame.init()

#Pantalla
size = (1000, 500)
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(0)
#FPS´s
clock = pygame.time.Clock()
#colores
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
grey = (50,50,50)
dark_blue = (0, 0, 15)

def Mira():
    borde = pygame.draw.circle(screen, red, mouse_pos, 20, 5)
    centro = pygame.draw.circle(screen, red, mouse_pos, 5)
    
#


#Bucle principal  
done = False
while not done:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            done = True   
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("PEW PEW")
            pygame.MOUSEBUTTONUP   
    screen.fill(white)
    
    #!animacion mouse
    mouse_pos = pygame.mouse.get_pos()
    
    #!dibujo cuadrado
    Mira()
    
        
    
    pygame.display.flip()
    clock.tick(60)