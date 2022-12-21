class Movimiento:
    
     def __init__ (self):
        self.direction="quieto"
        self.xjug=0
        self.yjug=20
        
        
     def move(self):
        
        if self.direction=="derecha":
            self.xjug=self.xjug+2
            
        if self.direction=="izquierda":
            self.xjug=self.xjug-2
            
        if self.direction=="arriba":
            self.yjug=self.yjug-2
            
        if self.direction=="abajo":
            self.yjug=self.yjug+2
        
        if self.direction=="quieto":
            self.xjug=self.xjug 
            self.yjug=self.yjug
            
        return(self.xjug,self.yjug)