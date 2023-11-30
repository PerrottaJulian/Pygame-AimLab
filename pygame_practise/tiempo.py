import pygame

pygame.init()

#Pantalla
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("AimLab")
clock = pygame.time.Clock()
font = pygame.font.SysFont("serif", 25)

done = False

current_time = 0
buttonpress_time = 0
while not done:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #!Permite salir del juego
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttonpress_time = pygame.time.get_ticks()
            screen.fill((255,255,255))
            
    current_time = pygame.time.get_ticks()
    print(f"Current time: {current_time} Button time: {buttonpress_time}" )
    
    if current_time-buttonpress_time > 3000:
        screen.fill((0,0,0))
    
    pygame.display.flip()
    clock.tick(60)