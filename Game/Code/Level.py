import pygame
from setting import *
from tile import Tile
from player import Player
from debug import *

class Level:
    def __init__(self):
        
        #Display Surface
        self.display_surface = pygame.display.get_surface()
        self.vis_sprites = CameraGroupY()
        self.obs_sprites = pygame.sprite.Group()
        
        #Sprite
        self.create_map()
        
    
    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
          for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.vis_sprites,self.obs_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.vis_sprites],self.obs_sprites)
    
    def run(self):
        #updates and Draw the game
        self.vis_sprites.custom_draw(self.player)
        self.vis_sprites.update()
        debug(self.player.direction)
        
class CameraGroupY(pygame.sprite.Group):
   def __init__(self):
       
       super().__init__()
       self.display_surface = pygame.display.get_surface()
       self.half_width = self.display_surface.get_size()[0]//2
       self.half_height = self.display_surface.get_size()[1]//2
       
       self.offset = pygame.math.Vector2(100,200)
       
       #creating the floor
       self.floor_surf = pygame.transform.scale(pygame.image.load('../Images/Map/ground.png').convert(),self.display_surface)
       self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))
       
       
     
   def custom_draw(self,player):
       
       #Getting Offset
       self.offset.x = player.rect.centerx - self.half_width
       self.offset.y = player.rect.centery - self.half_height
       
       for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
           offset_pos = sprite.rect.topleft - self.offset
           self.display_surface.blit(sprite.image,offset_pos)
           
        #drawing the floor
       floor_offset_pos = self.floor_rect.topleft - self.offset
       self.display_surface.blit(self.floor_surf,floor_offset_pos)
        