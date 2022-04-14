import pygame, sys, time 
from Level import Level
from setting import *


class Game:
    def __init__(self):
        
        # setup
        pygame.init()
        self.screen = pygame.display.set_mode((scr_wide,scr_high))
        pygame.display.set_caption('Project Snake')
        self.clock = pygame.time.Clock()
        self.Level = Level()
 
    def run(self):
        
        while True:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # game logic
            self.screen.fill('black')
            self.Level.run()
            pygame.display.update()
            self.clock.tick(fps)
 
if __name__ == '__main__':
    game = Game()
    game.run()