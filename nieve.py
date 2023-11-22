import pygame, sys, random
pygame.init()

#Pantalla
size = (1000, 500)
screen = pygame.display.set_mode(size)
#FPS´s
clock = pygame.time.Clock()
#colores
white = (255,255,255)
grey = (50,50,50)
dark_blue = (0, 0, 15)

#Modulos
def nube():
    for i in range(100,900,59):
        pygame.draw.circle(screen, grey, (i,0), 40)
   

def SetCords():
    cord_list = []
    for i in range(50):
        cord_x = random.randint(80,900)
        cord_y = random.randint(40,500)
        cord_list.append( [cord_x, cord_y] )
    return cord_list

def nieve(cords):
    for cord in cords:
        pygame.draw.circle(screen, white, cord, 2)
        cord[1]+=1
        if cord[1] > 500:
            cord[1] = 35
            
        
#Bucle principal  
cords = SetCords()
done = False
while not done:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            done = True      
    screen.fill(dark_blue)
    nube()
    nieve(cords)
    
    
    
    pygame.display.flip()
    clock.tick(60)






















