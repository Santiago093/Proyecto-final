import pygame
from movimiento import Movimiento

class Juego:
    
    def __init__(self):
        
        self.alto=500
        self.ancho=500
        self.movilalto=10
        self.movilancho=10
        self.screen=pygame.display.set_mode((self.ancho,self.alto))
        self.clock=pygame.time.Clock()
        self.fps=60
        self.movimiento=Movimiento()

    def teclas(self):
    
        keys=pygame.key.get_pressed()
            
        if keys [pygame.K_RIGHT]:
            self.movimiento.direction="derecha"
            if self.movimiento.xjug>(self.ancho-self.movilancho):
                    self.movimiento.xjug=self.ancho-self.movilancho
   
        elif keys[pygame.K_LEFT]:
            self.movimiento.direction="izquierda"
            if self.movimiento.xjug<0:
                   self.movimiento.xjug=20

        elif keys[pygame.K_UP]:
            self.movimiento.direction="arriba"
            if self.movimiento.yjug<0:
                self.movimiento.yjug=20
            
        elif keys[pygame.K_DOWN]:
            self.movimiento.direction="abajo"
            if self.movimiento.yjug>(self.alto-self.movilalto):
                self.movimiento.yjug=self.alto-self.movilalto
         
        else:
            self.movimiento.direction="quieto"
            
            
    def run (self):
        pygame.init()
        control=True
        while control:
            self.screen.fill((0,0,0))

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()



                      
            mapa = [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",            
            "                               XXX  XX  X  X  X  X",            
            "                                       X X XX X XX",            
            "XXX  XXXXXXX  XXX       X X X   XX X   X X X  X XX",            
            "XXXXXXX  X X               X X XXXXXX       XX   X",            
            "XXX x XXX X  X X   X XXX X X XX X XXX  X  XXXXXXXX",            
            "XXX X      X X  X X   XX X X            X XXXXXXXX",            
            "XXX  XXX XXXX X         X  X  X XXX  X X  X  XXXXX",            
            "XXX  XXXXX X        XXXX X          X  X X  X  X X",           
            "X X X XXXX X X       X  X X X X  XXX  XX      XXXX",           
            "XXX       XX X X X     X X X X  X    XXX       XXX",            
            "XXX x XXX               XX X X X       XX  XX     ",            
            "X X x X    X XXX   XX  X X  X   XXX  X   X  X XXXX",             
            "XXX X XXXX        XXXXX  XX      XX X   X XX X XXX",            
            "XXX x XX  XXXXX    XXXX             X  X  X  XXXXX",           
            "X X x XXXXX        XXXXX X X X  X X  X  X X  X  XX",           
            "XXX X       XXXX XX XXX X  XX XX           XXXX XX",            
            "XXX  XXXXX x x x          X  X X X XXXX  X  XXXXXX",           
            "XXX  XXX         X X X XX  X  X  XX X X  XX X  XXX",            
            "XXXX XXX XX    X X X X X    X   XXXXX X        XXX",            
            "XXX X X     XX   X XX XX      XX    XXXX       XXX",            
            "XXX  XX   XXX            X X X X X    XXXXXX   XXX",
            "XXX  XX  XXX XXXX     XX XX  XX XX XX      X XX  X",
            "XXX      XXX     XXX     XX    X  X X X XXXX    XX",
            "XX XXX     X X     XXX  XX X  X   X XX X  XXXX   X",
            "XXXXX     X X X X   X X         X XX X XX     XX X",
            "XX   XXXX X  XXX    XXX     XX XXXX   XX   X XX XX",
            "XXX X X X X X          XX X X X        XX XXX  XXX",
            "XX   XXX      XXXX        XX   XXX  XX    XXXX  XX",
            "XXXX   XXXXXX    XX   XXX   XXX       XXX   XXXX X",
            "XXXXX     XX  XXXX          XXXXXX   XX   XX  XXXX",
            "X  XXX  XXXX    XXXX   XXXXX       XXXXX   X  XXXX",
            "XXX    XXXX      XXX  XX    X  XX    XX  XX    X X",
            "   XXXXXX    X XX       XXX     XX        XX  X  X",
            "XXX      XXX     XXX   XXX   XXXX     XXX  X  X   ",
            "XX     XX    XXXX    XXXXX      XX   XXXX     X  X",
            "XX  XXX     X  XXX      XXXX XXXX       XX XXXX   ",
            "XX   XXXX  XXXX    XXXX   XX  XXX       XXX  XXX  ",
            "XXXX    XXXXX   X         XXX   XXXX     XX   XXXX",
            "XXX        XXX XXXX    XX      XX    XXXXX    XXXX",
            "XX   XXXX     XX    X X   XX     XX    XXXXX    XX",
            "XX XX      XX XXX     XX   XXX   XX    XXX   XX  X",
            "   XX  XX    XXXX     XX     XX XXXX   XXX  X XX  ",
            "XX   XXXXX        X  XXXXX      XXXX         XXXXX",
            "XXX      XXXX   XXXX     XXXXX   XX   XXX     XXXX",
            "XXX  XX    XXX   XX       XXXXX  XXXX   X    XX   ",
            "XX    XXXXX    XXX  XXXX      XXX       XXX    XXX",
            "XXX    XXXXX     XXX    XXXX   XX      XX   XXX   ",
            "XXX   XX       XX   XXX      XX  XXX    XXX    XX ",
            "  XXXX     XXX XXX  XX           XXX   XXXXXX  XXX",
            ]
            movil=pygame.draw.rect(self.screen,(0,255,0),[self.movimiento.xjug,self.movimiento.yjug,self.movilancho,self.movilalto])
            
            for fila in range(len(mapa)):
                for columna in range(len(mapa[fila])):
                    letrax=mapa[fila][columna]   
                    screenx= (columna)*20
                    screeny= (fila)*10
                        
                    if letrax=="X":
                        estatico=pygame.draw.rect(self.screen,(255,255,255),[screenx,screeny,20,10])
                        
                    if movil.colliderect(estatico):
                        self.movimiento.xjug=0
                        self.movimiento.yjug=20 

                         
                
            self.clock.tick(self.fps)
            self.teclas()
            self.movimiento.move()
            
            pygame.display.flip()


myGame=Juego()
myGame.run()
            
            
            