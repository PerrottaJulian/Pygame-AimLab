import pygame, random
# = guia del codigo // Usar la extension 'Better Comments' para ver los comentarios especiales
#* = Codigo no usado por el momento/comentarios personales
#! = Notas/Separacion importantes
#? = Comentarios 

#Constantes
FULL_BLACK = (0,0,0)
BLACK = (2,2,2)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
GREY = (50,50,50)
DARK_BLUE = (0, 0, 15)
SKYBLUE = (24, 125, 184)

SCREEN_LENGHT = 1000 #1300
SCREEN_HIGH = 500 #650

MIDDLE = (SCREEN_LENGHT//3, SCREEN_HIGH//2)
DOWN_MIDDLE = (SCREEN_LENGHT//3, SCREEN_HIGH//2 + 30)
TITLE_POS = (SCREEN_LENGHT//3, 40)
SUBTITLE_POS = (SCREEN_LENGHT//3+40, 90)
SCORE_POS = (40, SCREEN_HIGH-30)
TIME_POS = (SCREEN_LENGHT-100, SCREEN_HIGH-30)
LEVEL_POS = (10, 10)
SIGN_POS = (SCREEN_LENGHT-290, SCREEN_HIGH-40)

#Iniciacion
pygame.font.init()
pygame.mixer.init()

#Pantalla
screen = pygame.display.set_mode((SCREEN_LENGHT, SCREEN_HIGH))
pygame.display.set_caption("AimLab")
pygame.mouse.set_visible(0)

background = pygame.image.load("sprites_and_sounds/wall.png")

#sonido
gunshot = pygame.mixer.Sound("sprites_and_sounds/gunshot2.mp3")
clang = pygame.mixer.Sound("sprites_and_sounds/target-sound2.mp3")

#fuentes de texto
title_font = pygame.font.SysFont("serif", 50, True)
subtitle_font = pygame.font.SysFont("arial", 20, False, True)
score_font  = pygame.font.SysFont("arial", 20, True)
sign_font  = pygame.font.SysFont("comicsans", 15, True)

#otros
clock = pygame.time.Clock()

#Sprites
targets = ["sprites_and_sounds/target_big.png", "sprites_and_sounds/target_small.png", "sprites_and_sounds/target.png"]
class Target(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        r = random.randint(0,10)
        if r > 1:
            r = 2
            
        self.image = pygame.image.load(targets[r]).convert()
        self.image.set_colorkey(FULL_BLACK)
        self.rect = self.image.get_rect()
        
        self.speed = random.randint(3,7)
        self.type = type
        
    def update(self):
        if self.type == 1:
            self.rect.x += self.speed
            
            if self.rect.x >= SCREEN_LENGHT-10 or self.rect.x < 0:
                self.speed *= -1
                   
class Shot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites_and_sounds/disparo4.png").convert()
        self.image.set_colorkey(FULL_BLACK)
        self.rect = self.image.get_rect()  

class BulletHole(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites_and_sounds/disparo4.png").convert()
        self.image.set_colorkey(FULL_BLACK)
        self.rect = self.image.get_rect()     
              
#Funciones
def aim(center): #? Mirilla que sigue al mouse
    pygame.draw.circle(screen, RED, center, 20, 5)
    pygame.draw.circle(screen, RED, center, 5)

def startScreen():
    start_title = title_font.render("Pantalla de Inicio", True, FULL_BLACK) 
    start_text = subtitle_font.render("Presione cualquier tecla para iniciar", True, FULL_BLACK)
    sign = sign_font.render(f"Hecho por: Julian Perrotta - UMET", True, SKYBLUE)
    
    screen.blit(start_title, TITLE_POS)
    screen.blit(start_text, SUBTITLE_POS )
    screen.blit(sign, SIGN_POS)
    
def inGameScreen(score, level, t):
    score_text = score_font.render(f"Score: {score}", True, RED)
    level_text = title_font.render(f"Level {level}", True, RED)
    time_text = score_font.render(f"Time: {t}", True, FULL_BLACK)
    
    screen.blit(score_text, SCORE_POS)
    screen.blit(level_text, LEVEL_POS) 
    screen.blit(time_text, TIME_POS) 
        
        
#######!!! Clase 'Game'
class Game():
    def __init__(self):
        self.score = 0
        self.level = 0
        self.start = True
        self.setTime()
        
        #*extra de timepo global
        self.global_time = 0
        self.shot_time = 0
        
        #listas
        self.target_list = pygame.sprite.Group() #? Proposito: Detectar colisiones
        self.shot_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group() #? Proposito: Dibujar los sprites
        self.all_sprites_list = pygame.sprite.Group() 
    
    def setTime(self):
        self.time = 1000
        
    def passTime(self):
        self.time -= 1
    
    def generateTargets(self):
        for i in range(10 + 2*self.level):
            type = random.randint(1,4)
            target = Target(type)
            target.rect.x = random.randint(10, SCREEN_LENGHT - 50)
            target.rect.y = random.randint(10, SCREEN_HIGH - 50)

            self.target_list.add(target)
            self.all_sprites_list.add(target)
        self.level += 1
    
    #!Funciones pricipales de juego        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #? Permite salir del juego
                #self.done = True
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                shot = Shot()
                bullet_hole = BulletHole()
                shot.rect.center = self.mouse_pos
                bullet_hole.rect.center = self.mouse_pos
                
                self.shot_list.add(shot)
                self.bullet_list.add(bullet_hole)
                self.all_sprites_list.add(shot)
                self.all_sprites_list.add(bullet_hole)
        
                gunshot.play()
                
                #*extra de tiempo cuando disparo
                self.shot_time = pygame.time.get_ticks()
         
            if event.type == pygame.KEYDOWN:
                if self.start:
                    self.start = False
                    
                    self.bullet_list.empty()
                    self.all_sprites_list.empty()
                    
                    self.generateTargets() #? primera vez que genera los objetivos, luego de tocar cualquier tecla en la pantalla de inicio
                     
        return False
    
    def screenUpdate(self):
        self.mouse_pos = pygame.mouse.get_pos()
        
        #fondo de pantalla
        screen.blit(background, [0,0]) 
        
        if self.start:
            startScreen()
            self.shot_list.draw(screen)
            self.bullet_list.draw(screen)
            
        else:   
            inGameScreen(self.score, self.level, self.time)
            self.all_sprites_list.draw(screen) #? Diferenciacion entre pantalla de inicio y de juego
            
            
            
        aim(self.mouse_pos)
        
        pygame.display.update()

    def gameLogic(self):
        self.all_sprites_list.update()
        
        #? Eliminar los disparos apenas se generan, para evitar que se queden estaticos y colisionen con los objetivos que se mueven,
        #? Pero aun asi se generan una fraccion de segundo, por lo que al momento del disparo si hay colision
        for shot in self.shot_list:
            if self.global_time - self.shot_time > 20: #? Esto significa que el disparo con colision se genera por solo 20 milesimas de segundo y luego se elimina
                self.shot_list.remove(shot)
                self.all_sprites_list.remove(shot)  
                    
        if not self.start:
            self.passTime() #? Pasar el tiempo del nivel
            #print(self.time)
            for shot in self.shot_list:
                target_hitlist = pygame.sprite.spritecollide(shot, self.target_list, True) #? Colisiones Detectar los disparos cuando aciertan a un objetivo
                
                for hit in target_hitlist:
                    self.score += 1 #? Aumenta el puntaje cuando se produce la colision 
                    clang.play()
                    
            if len(self.target_list) == 0:
                self.shot_list.empty()  #? Cuando destruyo todos los objetivos antes de que termine el tiempo:
                self.target_list.empty()  #? se vacian todas las carpetas de sprites, se reinicia el tiempo y se vuelven a generar 'targets', subiendo de nivel
                self.all_sprites_list.empty()
                
                self.setTime()
                self.generateTargets()
            
            
            if self.time == 0:  
                self.__init__()
            
            #? La idea del juego es acumular la mayor cantidad de puntos, disparandole a los objetivos.
            #?Cuando le disparaste a todos los objetivos, se reinica el timpo y aparecen nuevos (se avanza de nivel)
            #?Se pierde cuando te quedas sin tiempo
            #?La cantidad de tiempo es simpre la misma, pero en cada nuevo nivel hay mas objetivos.
            
########################!
        
#Funcion principal
def main():
    pygame.init()
    
    done = False
    mygame = Game()
    while not done:
        done = mygame.events()
        
        #*tiempo global
        timer = pygame.time.get_ticks()
        mygame.global_time = timer
        #*
        
        mygame.gameLogic() 
        mygame.screenUpdate()
        
        #print(f"Time: {mygame.global_time} ShotTime: {mygame.shot_time}")
        
        clock.tick(60)
        

        
    pygame.quit()
    
    
main()