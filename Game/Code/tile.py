import pygame
from setting import *

class Tile(pygame.sprite.Sprite):
    def _init_(self,pos,Groups):
        super()._init_(Groups)
        self.image = pygame.image.load('../Images/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)