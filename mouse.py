import pygame, sys, random




#* Datos previos
size = (1000, 500)
#colores
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
grey = (50,50,50)
dark_blue = (0, 0, 15)

#*Pygame
pygame.init()

screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(0)
clock = pygame.time.Clock()

#Sprites
class Meteoro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        
# Mira
def Mira(center):
    borde = pygame.draw.circle(screen, red, center, 20, 5)
    centro = pygame.draw.circle(screen, red, center, 5)
    
#meteoritos
lista_meteoros = pygame.sprite.Group()
lista_sprites = pygame.sprite.Group()

def generarMeteoros():
    for i in range(25):
        meteoro = Meteoro()
        meteoro.rect.x = random.randint(10,990)
        meteoro.rect.y = random.randint(10,490)
        lista_meteoros.add(meteoro)
        lista_sprites.add(meteoro)
        
      
#Bucle principal  
done = False
generarMeteoros()
while not done:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            done = True   
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("PEW PEW")
            
    #!Dibujos de pantalla  
    screen.fill(white)
    lista_meteoros.draw(screen)
    #!Mouse
    mouse_pos = pygame.mouse.get_pos()
    
    #!dibujo mirilla
    Mira(mouse_pos)
    
        
    
    pygame.display.flip()
    clock.tick(60)