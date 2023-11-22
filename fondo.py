import pygame, sys, random

pygame.init()

#Pantalla
size = (500, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Meteoritos")
clock = pygame.time.Clock()

#Imagen
"""
background = pygame.image.load("background.png").convert()
meteor = pygame.image.load("meteor.png").convert()
meteor.set_colorkey((0,0,0) )
"""

class Meteor (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

#listas
meteor_list = pygame.sprite.Group() #? Proposito: Detectar colisiones
all_sprites_list = pygame.sprite.Group() #? Proposito: Dibujar los sprites

#generar meteoros
for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(500)
    meteor.rect.y = random.randrange(600)
    
    meteor_list.add(meteor)
    all_sprites_list.add(meteor)
    
#jugador
player = Player()    
all_sprites_list.add(player)

#data previa al bucle
score = 0
done = False
print(f"Meteors: {len(meteor_list)}")

#bucle
while not done:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            done = True      
    
    screen.fill((255,255,255))
    all_sprites_list.draw(screen)
    #mouse
    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    #movimiento de nave
    player.rect.x = x
    player.rect.y = y
    
    #colision
    meteor_hit_list =  pygame.sprite.spritecollide(player, meteor_list, True)
    
    for meteor in meteor_hit_list:
        score += 1
        print(score)
        
    if score == 50:
        score = 0
        for i in range(50):
            meteor = Meteor()
            meteor.rect.x = random.randrange(500)
            meteor.rect.y = random.randrange(600)
            meteor_list.add(meteor)
            all_sprites_list.add(meteor)
        
    
    
    """
    screen.blit(background, [0,0])
    screen.blit(meteor, [x,y] )
    """
    
        
    pygame.display.update()
    clock.tick(60)

