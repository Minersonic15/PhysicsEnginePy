import pygame

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
        self.cloc = pygame.time.Clock()
        self.goinmg = True


        self.ITGOES()
    def ITGOES(self):
        while self.goinmg:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.goinmg = 0

            self.screen.fill((40,40,40))
            pygame.display.flip()
            self.cloc.tick(60)

        else:
            pygame.quit()
class Object:
    def __init__(self, pops, sizX, sizY, x, y):
        self.parent = pops
        self.im = pygame.Surface((sizX, sizY))
        self.im.fill((0,0,0))
        self.obj = self.im.get_rect()
        self.obj.center = (x,y)

main = Main()
