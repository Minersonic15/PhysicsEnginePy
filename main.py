import pygame

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
        self.cloc = pygame.time.Clock()
        self.goinmg = True
        self.dudes = []
        self.Width = self.screen.get_width()
        self.Height = self.screen.get_height()
        print(self.screen.get_width())
        self.MakeObj()

        self.ITGOES()
    def MakeObj(self):
        self.dudes.append(Object(self,100,50,100,0))

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
            self.dudes[0].Draw()
            pygame.display.flip()

            self.cloc.tick(60)

        else:
            pygame.quit()
class Object:
    def __init__(self, pops, sizX, sizY, x, y):
        self.parent = pops
        self.im = pygame.Surface((sizX, sizY))
        self.im.fill((255,255,255))
        self.obj = self.im.get_rect()
        self.RadiX = sizX/2
        self.RadiY = sizY/2
        
        self.x = x + self.RadiX
        self.y = y + self.RadiY
        
        
        self.obj.center = (self.x, self.y)
        self.VeloX = 0
        self.VeloY = 0
        self.Movable = 1
        self.grounded=0
        if self.y >= self.parent.Height - self.RadiY:
            self.grounded = True
        
        
    def Update(self):
        if self.Movable:
            if self.y >= self.parent.Height - self.RadiY:
                self.grounded = True
            else:
                self.grounded = False
            if self.y+ self.RadiY >= self.parent.Height:
                self.y = self.parent.Height - self.RadiY

            if self.grounded:
                self.VeloY = 0
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
