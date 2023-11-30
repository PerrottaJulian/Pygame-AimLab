import pygame, time, random
# = guia del codigo
#* = Codigo no usado por el momento/comentarios personales
#! = Notas/Separacion importantes
#? = Comentarios 

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
DOWN_MIDDLE = (SCREEN_LENGHT//3, SCREEN_HIGH//2 + 30)
TITLE_POS = (SCREEN_LENGHT//3, 40)
SUBTITLE_POS = (SCREEN_LENGHT//3+40, 90)
SCORE_POS = (50, SCREEN_HIGH-30)

#Iniciacion

pygame.font.init()
pygame.mixer.init()

#Pantalla
screen = pygame.display.set_mode((SCREEN_LENGHT, SCREEN_HIGH))
pygame.display.set_caption("AimLab")
pygame.mouse.set_visible(0)

background = pygame.image.load("sprites_and_sounds/wall2.png")

#sonido
gunshot = pygame.mixer.Sound("sprites_and_sounds/gunshot2.mp3")
clang = pygame.mixer.Sound("sprites_and_sounds/target-sound2.mp3")


title_font = pygame.font.SysFont("serif", 50, True)
subtitle_font = pygame.font.SysFont("arial", 20, False, True)
score_font = subtitle_font = pygame.font.SysFont("arial", 20, True)

#otros
clock = pygame.time.Clock()

#Sprites
class Target(pygame.sprite.Sprite):
    def __init__(self, type = 1):
        super().__init__()
        self.image = pygame.image.load("sprites_and_sounds/target2.png").convert()
        self.image.set_colorkey(full_black)
        self.rect = self.image.get_rect()
        
        self.speed = 5
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
        self.image.set_colorkey(full_black)
        self.rect = self.image.get_rect()     
              
#Funciones
def generateTargets(game, amount):
    for i in range(amount):
        type = random.randint(1,4)
        target = Target(type)
        target.rect.x = random.randint(10, SCREEN_LENGHT - 50)
        target.rect.y = random.randint(10, SCREEN_HIGH - 50)
    
        game.target_list.add(target)
        game.all_sprites_list.add(target)
        
def aim(center): #? Mirilla que sigue al mouse
    pygame.draw.circle(screen, red, center, 20, 5)
    pygame.draw.circle(screen, red, center, 5)

def startScreen():
    start_title = title_font.render("Pantalla de Inicio", True, full_black)
    screen.blit(start_title, TITLE_POS)
    start_text = subtitle_font.render("Presione cualquier tecla para iniciar", True, full_black)
    screen.blit(start_text, SUBTITLE_POS )
                 
#######! Clase 'Game'
class Game():
    def __init__(self):
        self.score = 0
        self.start = True
        self.setTime()
        
        #*extra de timepo global
        self.global_time = 0
        self.shot_time = 0
        
        #listas
        self.target_list = pygame.sprite.Group() #? Proposito: Detectar colisiones
        self.shot_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group() #? Proposito: Dibujar los sprites

    def setTime(self):
        self.time = 1000
        
    def passTime(self):
        self.time -= 1

    
    #!Funciones pricipales de juego        
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
                
                #*extra de tiempo cuando disparo
                self.shot_time = pygame.time.get_ticks()
                
                
            if event.type == pygame.KEYDOWN:
                if self.start:
                    self.start = False
                    self.shot_list.empty()
                    self.all_sprites_list.empty()
                    
                    generateTargets(self, 30) #? primera vez que genera los objetivos, luego de tocar cualquier tecla en la pantalla de inicio
                     
        return False
    
    def screenUpdate(self):
        self.mouse_pos = pygame.mouse.get_pos()
        
        #fondo de pantalla
        screen.blit(background, [0,0]) 
        
        if self.start:
            startScreen()
            self.shot_list.draw(screen)
            
        else:   
            self.all_sprites_list.draw(screen) #? Diferenciacion entre pantalla de inicio y de juego
            score_text = score_font.render(f"Score: {self.score}", True, full_black)
            screen.blit(score_text, SCORE_POS)
            
        aim(self.mouse_pos)
        
        pygame.display.update()

    def gameLogic(self):
        self.all_sprites_list.update()
        for shot in self.shot_list:
            if self.global_time - self.shot_time > 20:
                self.shot_list.remove(shot)
                self.all_sprites_list.remove(shot)  
                    
        if not self.start:
            self.passTime() #? Pasar el tiempo
            #print(self.time)
            for shot in self.shot_list:
                target_hitlist = pygame.sprite.spritecollide(shot, self.target_list, True)
                
                
                for hit in target_hitlist:
                    self.score += 1
                    clang.play()
                    
            if len(self.target_list) == 0:
                self.shot_list.empty()  #? Cuando destruyo todos los objetivos antes de que termine el tiempo,
                self.target_list.empty()  #? se vacian todas las carpetas de sprites, se reinicia el tiempo y se vuelven a generar 'targets', subiendo de nivel
                self.all_sprites_list.empty()
                
                self.setTime()
                generateTargets(self, 35)
            
            
            if self.time == 0:
                self.__init__()
                       
########################!
        
#Funcion principal
def main():
    pygame.init()
    
    done = False
    mygame = Game()
    while not done:
        done = mygame.events()
        
        #*extra de tiempo global
        timer = pygame.time.get_ticks()
        mygame.global_time = timer
        
        mygame.gameLogic() 
        mygame.screenUpdate()
        
        print(f"Time: {mygame.global_time} ShotTime: {mygame.shot_time}")
        
        clock.tick(60)
        

        
    pygame.quit()