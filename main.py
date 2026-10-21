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
        self.elast= -2
        for i in range(0):
            self.MakeObj(random.randint(10, 150), random.randint(10, 150), random.randint(0, self.Width), random.randint(0, self.Height), i)

        self.MakeObj(150, 100, 0,0, 1)
        #elf.MakeObj(100, 150, 0, 0, 2)

        self.ITGOES()
    def MakeObj(self, sizX, sizY, x, y, num):
        self.dudes.append(Object(self,sizX, sizY,x,y, num))
        

    def ITGOES(self):
        while self.goinmg:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.goinmg = 0
            self.Width = self.screen.get_width()
            self.Height = self.screen.get_height()
            for dud in self.dudes:
                dud.Update()


            self.screen.fill((40,40,40))
            for dud in self.dudes:
                dud.Draw()
            pygame.display.flip()

            self.cloc.tick(60)

        else:
            pygame.quit()
class Object:
    def __init__(self, pops, sizX, sizY, x, y, num):
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
        self.VeloX = 10
        self.VeloY = 0

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

            if self.y+ self.RadiY > self.parent.Height:
                self.y = self.parent.Height - self.RadiY

            if self.x >= self.parent.Width - self.RadiX or self.x <= self.RadiX:
                self.VeloX *= -1

            if self.x + self.RadiX >= self.parent.Width:
                self.x = self.parent.Width - self.RadiX

            elif self.x - self.RadiX < 0:
                self.x = self.RadiX

            if self.y <= self.RadiY:
                self.VeloY*= self.parent.elast
            if self.y < self.RadiY:
                self.y = self.RadiY

            if self.grounded:
                self.y = self.parent.Height - self.RadiY
                self.VeloY *= self.parent.elast

            else:
                self.accel(9.8)

            self.x += self.VeloX
            self.y += self.VeloY


            self.obj.center = (self.x, self.y)

    #def Collision(self):

    def accel(self, ac):
        self.VeloY = self.VeloY + ac*(1/60)

    def Draw(self):
        self.parent.screen.blit(self.im, self.obj)

main = Main()
