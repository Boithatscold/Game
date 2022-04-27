import pygame
from setting import *
from tile import Tile
from player import Player
from debug import *
from support import *
class Level:
    def __init__(self):
        
        #Display Surface
        self.display_surface = pygame.display.get_surface()
        self.vis_sprites = CameraGroupY()
        self.obs_sprites = pygame.sprite.Group()
        
        #Sprite
        self.create_map()
        
    
    def create_map(self):
        
        layouts = {
            'boundary': import_csv_layout('../Images/Map/Map_Border.csv')
            
            }
        for style,layout in layouts.items():
            for row_index,row in enumerate(WORLD_MAP):
                for col_index, col in enumerate(row):
                    x = col_index * TILESIZE
                    y = row_index * TILESIZE
                    if style == 'boundary':
                        Tile((x,y),self.obs_sprites,'Invis')
        
        
        
        self.player = Player((1000,1000),[self.vis_sprites],self.obs_sprites)
    
    def run(self):
        #updates and Draw the game
        self.vis_sprites.custom_draw(self.player)
        self.vis_sprites.update()
      
        
class CameraGroupY(pygame.sprite.Group):
   def __init__(self):
       
       super().__init__()
       self.display_surface = pygame.display.get_surface()
       self.half_width = self.display_surface.get_size()[0]//2
       self.half_height = self.display_surface.get_size()[1]//2
       
       self.offset = pygame.math.Vector2()
       
       #creating the floor
       
       # for row_index,row in enumerate(WORLD_MAP):
       #     for col_index, col in enumerate(row):
       #         x = col_index * (TILESIZE+2)
       #         y = row_index * (TILESIZE+2)
       #         self.size = (x,y)
       
       self.floor_surf = pygame.image.load('../Images/Map/Map.png').convert()
       self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
       
       
     
   def custom_draw(self,player):
       
       #Getting Offset
       self.offset.x = player.rect.centerx - self.half_width
       self.offset.y = player.rect.centery - self.half_height
       
       
        #drawing the floor
       floor_offset_pos = self.floor_rect.topleft - self.offset
       self.display_surface.blit(self.floor_surf,floor_offset_pos)
       
       for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
           offset_pos = sprite.rect.topleft - self.offset
           self.display_surface.blit(sprite.image,offset_pos)
           
        