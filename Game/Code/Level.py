import pygame
from setting import *
from tile import Tile
from player import Player

class Level:
    def _init_(self):
        
        #Display Surface
        self.display_surface = pygame.display.get_surface()
        self.vis_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        
        #Sprite
        self.create_map()
        
    
    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
          for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.vis_sprites])    
    
    def run(self):
        self.vis_sprites.draw(self.display_surface)
        
      
                