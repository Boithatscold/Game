import pygame
from setting import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,Groups):
        super().__init__(Groups)
        self.image = pygame.image.load('../Images/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)