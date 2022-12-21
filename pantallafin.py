import pygame

class Pantalla_fin:
    def __init__(self):
        
        self.alto=500
        self.ancho=500        
        self.pantalla=pygame.display.set_mode((self.ancho,self.alto))
        self.clock=pygame.time.Clock()
        self.letra=pygame.font.SysFont("impact",100)
        self.anuncio=self.letra.render("JUEGO TERMINADO",True,(255,255,255))
        self.fps=60
        self.fin=True




    def fin(self):
        pygame.init()
        control=True
        while control:    
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
        
            self.pantalla.blit(self.anuncio,(0,250))
            self.clock()
            pygame.display.update()
            
            
fin=Pantalla_fin()
