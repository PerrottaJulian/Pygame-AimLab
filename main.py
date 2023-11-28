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

middle = (SCREEN_LENGHT//3, SCREEN_HIGH//2)

#Pantalla
screen = pygame.display.set_mode((SCREEN_LENGHT, SCREEN_HIGH))
pygame.mouse.set_visible(0)
clock = pygame.time.Clock()
font = pygame.font.SysFont("serif", 25)

#sonido
sound = pygame.mixer.Sound("sprites_sounds/gunshot.mp3")

#Clases (Sprites)
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites_sounds/target2.png").convert()
        self.image.set_colorkey(full_black)
        self.rect = self.image.get_rect()

class Shot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites_sounds/disparo4.png").convert()
        #self.image.set_colorkey(white)
        self.rect = self.image.get_rect()     
          
#Modulos
def generateTargets():
    for i in range(25):
        target = Target()
        target.rect.x = random.randint(10, SCREEN_LENGHT - 50)
        target.rect.y = random.randint(10, SCREEN_HIGH - 50)
    
        target_list.add(target)
        all_sprites_list.add(target)


def displayFrames(start, game, gameover):
    screen.fill(white)
    if start:
        start_text = font.render("Pantalla de Inicio", True, full_black)
        screen.blit(start_text, middle)
    elif game:
        #game_text = font.render("JUEGOOOOOOO", True, black)
        #screen.blit(game_text, middle)
        all_sprites_list.draw(screen)
    elif gameover:
        end_text = font.render("GAME OVER", True, full_black)
        screen.blit(end_text, middle)
    mira(mouse_pos)
    pygame.display.update()

def mira(center): #!Mirilla que sigue al mouse
    pygame.draw.circle(screen, red, center, 20, 5)
    pygame.draw.circle(screen, red, center, 5)

#listas
target_list = pygame.sprite.Group() #? Proposito: Detectar colisiones
all_sprites_list = pygame.sprite.Group() #? Proposito: Dibujar los sprites

#Data previa
done = False
start = True
game = False
gameover = False
generateTargets()

#Bucle Principal
while not done:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #!Permite salir del juego
            done = True
         
        #! Eventos de mouse y teclado segun la pantalla
        if game: #? Si estoy en el juego, hacer click dispara y con espacio paso al game over (temporal, va a haber condicion)
            if event.type == pygame.KEYDOWN:
                game = False
                gameover = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                shot = Shot()
                shot.rect.x = mouse_pos[0] -10
                shot.rect.y = mouse_pos[1] -11
                all_sprites_list.add(shot)
                sound.play()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites_list.clear()
             
        elif start and event.type == pygame.MOUSEBUTTONDOWN: #? Si estoy en el inicio, con un click voy al juego
            start = False
            game = True       
        elif gameover and event.type == pygame.KEYDOWN: #? Si esoty en GameOver, de un click vuelvo al inicio
            gameover = False
            start = True
            
        #####!
    
                     
    displayFrames(start, game, gameover)

    clock.tick(60)

pygame.quit()



