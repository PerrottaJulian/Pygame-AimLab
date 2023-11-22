import pygame, time, random
pygame.init()

#Constantes
black = (0,0,0)
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
clock = pygame.time.Clock()
font = pygame.font.SysFont("serif", 25)

#Clases (Sprites)
class Meteoro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        
#Modulos
def displayFrames(start, game, gameover):
    screen.fill(white)
    if start:
        start_text = font.render("Pantalla de Inicio", True, black)
        screen.blit(start_text, middle)
    elif game:
        game_text = font.render("JUEGOOOOOOO", True, black)
        screen.blit(game_text, middle)
    elif gameover:
        end_text = font.render("GAME OVER", True, black)
        screen.blit(end_text, middle)
    pygame.display.update()


#Bucle Principal
done = False
start = True
game = False
gameover = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #!Permite salir del juego
            done = True
         
        #! Eventos de mouse y teclado segun la pantalla
        if game: #? Si estoy en el juego, hacer click dispara y con espacio paso al game over (temporal, va a haber condicion)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game = False
                    gameover = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("PEW PEW")
        if start and event.type == pygame.MOUSEBUTTONDOWN: #? Si estoy en el inicio, con un click voy al juego
            start = False
            game = True       
        if gameover and event.type == pygame.MOUSEBUTTONDOWN: #? Si esoty en GameOver, de un click vuelvo al inicio
            gameover = False
            start = True
            
        #####!
        
    if game:
        
        
                    
    displayFrames(start, game, gameover)

    clock.tick(60)





