import pygame
import random

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
        self.cloc = pygame.time.Clock()
        self.goinmg = True
        self.dudes = []
        self.Width = self.screen.get_width()
        self.Height = self.screen.get_height()
        self.PrevW = self.screen.get_width()
        self.PrevH = self.screen.get_height()

        self.VeloY = 0
        self.VeloX = 0
        self.elast= -0.75
        for i in range(0):
            self.MakeObj(random.randint(10, 150), random.randint(10, 150), random.randint(0, self.Width), random.randint(0, self.Height), i)

        self.MakeObj(150, 100, 0,0, 10)
        #self.MakeObj(100, 150, 300, 0, 20)
        self.MakeObj(300, 100, 0, 300, 10)


        self.ITGOES()
    def MakeObj(self, sizX, sizY, x, y, num):
        self.dudes.append(Object(self,sizX, sizY,x,y, num))
        
    def ITGOES(self):
        tick = 0
        while self.goinmg:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.goinmg = 0
            self.Width = self.screen.get_width()
            self.Height = self.screen.get_height()
            self.CheckCollide()
            for dud in self.dudes:
                dud.Update()

            self.screen.fill((40,40,40))
            for dud in self.dudes:
                dud.Draw()
            pygame.display.flip()

            tick+=1
            if tick >= 60: 
                tick = 0

            self.cloc.tick(60)

        else:
            pygame.quit()
    def Collision(self, a, b):
        return(a.x -a.RadiX < b.x + b.RadiX and 
               a.x + a.RadiX > b.x - b.RadiX and 
               a.y - a.RadiY < b.y + b.RadiY and 
               a.y + a.RadiY > b.y - b.RadiY)
    
    def CheckCollide(self):
        for i in range(len(self.dudes)):
            for j in range(i+1, len(self.dudes)):
                a= self.dudes[i]
                b = self.dudes[j]
                if self.Collision(a,b):
                    self.MakeBoing(a,b)
                    

    def MakeBoing(self, a, b):
        overlapX = min(a.x + a.RadiX, b.x+ b.RadiX) - max(a.x - a.RadiX, b.x - b.RadiX)
        overlapY = min(a.y + a.RadiY, b.y+ b.RadiY) - max(a.y - a.RadiY, b.y - b.RadiY)
        aX = a.x
        bX = b.x
        axR = a.RadiX
        bxR = b.RadiX
        axV = a.VeloX
        bxV = b.VeloX

        aY = a.y
        bY = b.y
        ayR = a.RadiY
        byR = b.RadiY
        ayV = a.VeloY
        byV = b.VeloY
        
        if overlapX < overlapY:
            a.CollidedX(bX, bxR, bxV)
            b.CollidedX(aX, axR, axV)
            
        else:
            a.CollidedY(bY, byR, byV)
            b.CollidedY(aY, ayR, ayV)
            
class Object:
    def __init__(self, pops, sizX, sizY, x, y, VeloX):
        self.parent = pops
        self.im = pygame.Surface((sizX, sizY), pygame.SRCALPHA)
        #self.im.fill((40,40,40))
        self.obj = self.im.get_rect()
        pygame.draw.rect(self.im, (255,255,255), self.obj, width=5)
        self.RadiX = sizX/2
        self.RadiY = sizY/2
        
        self.x = x + self.RadiX
        self.y = y + self.RadiY
        
        
        self.obj.center = (self.x, self.y)
        self.VeloX = VeloX
        self.VeloY = 0

        self.mass = 1

        self.Movable = True
        self.grounded= False
        self.elastic = True

        if self.y >= self.parent.Height - self.RadiY:
            self.grounded = True
        
    def Update(self):
        if self.Movable:
            if self.y >= self.parent.Height - self.RadiY:
                self.grounded = True
            else:
                self.grounded = False

        
            if self.x >= self.parent.Width - self.RadiX:
                self.VeloX *= self.parent.elast
                

            elif self.x <= self.RadiX:
                self.VeloX *= self.parent.elast
            if self.y <= self.RadiY:
                self.VeloY *= self.parent.elast
        
            if self.grounded:
                self.VeloY *= self.parent.elast
                
            else:
                self.accel(9.8)

            if self.x + self.RadiX >= self.parent.Width:
                self.x = self.parent.Width - self.RadiX
            elif self.x - self.RadiX < 0:
                self.x = self.RadiX

            if self.y < self.RadiY:
                self.y = self.RadiY
            elif self.y+ self.RadiY > self.parent.Height:
                self.y = self.parent.Height - self.RadiY

            self.x += self.VeloX
            self.y += self.VeloY


            self.obj.center = (self.x, self.y)

    def CollidedX(self, colliderX, colliderRad, ColliderVelo):
        if self.x > colliderX:
            self.x = colliderX + colliderRad + self.RadiX
        else:
            self.x = colliderX - colliderRad - self.RadiX
        self.VeloX = self.Bounce(self.VeloX, ColliderVelo, 1,1)
        self.VeloX *= -self.parent.elast

    def CollidedY(self, colliderY, colliderRad, ColliderVelo):
        if self.y > colliderY:
            self.y = colliderY + colliderRad + self.RadiY +1
        else:
            self.y = colliderY - colliderRad - self.RadiY -1
        self.VeloY = self.Bounce(self.VeloY, ColliderVelo, 1,1)
        self.VeloY *= -self.parent.elast

    def Bounce(self, Velo1, Velo2, mass, mass2):
            return  Velo2
    def accel(self, ac):
        self.VeloY = self.VeloY + ac*(1/60)

    def Draw(self):
        self.parent.screen.blit(self.im, self.obj)

main = Main()
