import pygame, time, random
pygame.init()
pygame.mixer.init()

#Constantes
full_black = (0,0,0)
black = (2,2,2)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
grey = (50,50,50)
dark_blue = (0, 0, 15)

SCREEN_LENGHT = 1000
SCREEN_HIGH = 500

MIDDLE = (SCREEN_LENGHT//3, SCREEN_HIGH//2)

#Pantalla
screen = pygame.display.set_mode((SCREEN_LENGHT, SCREEN_HIGH))
pygame.display.set_caption("AimLab")
pygame.mouse.set_visible(0)
clock = pygame.time.Clock()
font = pygame.font.SysFont("serif", 25)

#sonido
gunshot = pygame.mixer.Sound("sprites_sounds/gunshot.mp3")
clang = pygame.mixer.Sound("sprites_sounds/target_sound.mp3")

#Sprites
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites_sounds/target2.png").convert()
        #self.image.set_colorkey(full_black)
        self.rect = self.image.get_rect()

class Shot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites_sounds/45724.png").convert()
        self.image.set_colorkey(full_black)
        self.rect = self.image.get_rect()     
          



