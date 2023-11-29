import pygame, sys, random
pygame.init()

#Colores
"""colores = {
"BLACK" : (0, 0, 0),
"WHITE" : (255, 255, 255),
"GREEN" : (0, 255, 0),
"RED" : (255, 0, 0),
"BLUE" : (0, 0, 255),
}"""
colores = [(0, 0, 0), (0, 255, 0), (255, 0, 0), (0, 0, 255)]

#FPS´s
clock = pygame.time.Clock()

#Pantalla
size = (1000, 500)
screen = pygame.display.set_mode(size)

#animacion
cord_x = 500
cord_y = 250

speed_x = 4
speed_y = 4
n_random = random.randint(0,3)
n_color = n_random

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()        
    screen.fill((255, 255, 255))
    
    #* Logica
    #pygame.draw.line(screen, RED, [100, 100],[100,500], 5)
    
    cord_x += speed_x
    cord_y += speed_y
    if cord_x > 1000-40 or cord_x < 0:
        speed_x *= -1
        while n_color == n_random:
            n_random = random.randint(0,3)
        n_color = n_random
            
    if cord_y > 500-40 or cord_y < 0:
        speed_y *= -1
        while n_color == n_random:
            n_random = random.randint(0,3)
        n_color = n_random
    """if center_x > 1050:
        center_x = 0"""
        
    #! <---- zona de dibujo
    pygame.draw.rect(screen, colores[n_color], [cord_x, cord_y, 40,40])
    #! <---- zona de dibujo
    
    #actualizar pantalla
    pygame.display.flip()
    clock.tick(60)