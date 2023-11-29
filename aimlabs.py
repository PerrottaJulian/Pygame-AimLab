import pygame, time, random
#=guia del codigo
#*Codigo no usado por el momento/comentarios personales
#!Notas importantes
#?Comentarios 

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

#Iniciacion
pygame.init()
pygame.mixer.init()

#Pantalla
screen = pygame.display.set_mode((SCREEN_LENGHT, SCREEN_HIGH))
pygame.display.set_caption("AimLab")
pygame.mouse.set_visible(0)

background = pygame.image.load("sprites_sounds/fondo.png")

#sonido
gunshot = pygame.mixer.Sound("sprites_sounds/gunshot2.mp3")
clang = pygame.mixer.Sound("sprites_sounds/target-sound2.mp3")

#otros
clock = pygame.time.Clock()
font = pygame.font.SysFont("serif", 25)

#Sprites
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
        self.image.set_colorkey(full_black)
        self.rect = self.image.get_rect()     
              
#Funciones
def generateTargets(game, amount):
    for i in range(amount):
        target = Target()
        target.rect.x = random.randint(10, SCREEN_LENGHT - 50)
        target.rect.y = random.randint(10, SCREEN_HIGH - 50)
    
        game.target_list.add(target)
        game.all_sprites_list.add(target)
        
def mira(center): #? Mirilla que sigue al mouse
    pygame.draw.circle(screen, red, center, 20, 5)
    pygame.draw.circle(screen, red, center, 5)
              
#######! Clase 'Game'
class Game():
    def __init__(self):
        self.score = 0
        #self.done = False
        self.start = True
        self.setTime()
        
        #listas
        self.target_list = pygame.sprite.Group() #? Proposito: Detectar colisiones
        self.shot_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group() #? Proposito: Dibujar los sprites

        #*Chequear si funciona bien
    def setTime(self):
        self.time = 1500
    def passTime(self):
        self.time -= 1
            
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #? Permite salir del juego
                #self.done = True
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                shot = Shot()
                shot.rect.center = self.mouse_pos
                
                self.shot_list.add(shot)
                self.all_sprites_list.add(shot)
                gunshot.play()
                
            if event.type == pygame.KEYDOWN:
                if self.start:
                    self.start = False
                    self.shot_list.empty()
                    self.all_sprites_list.empty()
                    
                    generateTargets(self, 50) #? primera vez que genera los objetivos, luego de tocar cualquier tecla en la pantalla de inicio
                     
        return False
    
    def screenUpdate(self):
        self.mouse_pos = pygame.mouse.get_pos()
        
        #fondo de pantalla
        screen.fill(blue)
        #*screen.blit(background, [0,0]) 
        
        if self.start:
            start_text = font.render("Pantalla de Inicio", True, full_black)
            screen.blit(start_text, MIDDLE)
            self.shot_list.draw(screen)
        else:
            
            self.all_sprites_list.draw(screen) #? Diferenciacion entre pantalla de inicio y de juego
            
        mira(self.mouse_pos)
        
        pygame.display.update()

    def gameLogic(self):
        #*self.all_sprites_list.update()
        if not self.start:
            self.passTime() #! Pasar el tiempo
            print(self.time)
            for shot in self.shot_list:
                target_hitlist = pygame.sprite.spritecollide(shot, self.target_list, True)
                for hit in target_hitlist:
                    self.score += 1
                    print(self.score)
                    clang.play()
                    
            if len(self.target_list) == 0:
                self.shot_list.empty()
                self.target_list.empty()
                self.all_sprites_list.empty()
                
                self.setTime()
                generateTargets(self, 50)
            
            if self.time == 0:
                self.__init__()
                
            
########################!
        
#Funcion principal
def main():
    done = False
    mygame = Game()
    while not done:
        done = mygame.events()
        
        mygame.gameLogic() 
        mygame.screenUpdate()
        
        
        clock.tick(60)
        

        
    pygame.quit()