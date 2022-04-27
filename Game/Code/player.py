import pygame
from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,Groups,obs_sprites):
        super().__init__(Groups)
        self.image = pygame.image.load('../Images/Idle 1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-20)
        
        self.direction = pygame.math.Vector2()
        self.speed = 5
        
        self.obs_sprites = obs_sprites
        
    def input(self):
        # Movement
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        
    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
       
        
        
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        
    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obs_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x < 0: #moving right
                        self.hitbox.right = sprite.hitbox.left
                        print("Right")
                        print(self.direction.x)
                    
                    if self.direction.x > 0: #moving left
                        self.hitbox.left = sprite.hitbox.right
                        print("left")
                        print(self.direction.x)
        if direction == 'vertical':
            for sprite in self.obs_sprites:
                if sprite.rect.colliderect(self.hitbox):
                    if self.direction.y < 0: #moving down
                        self.hitbox.bottom = sprite.rect.top
                        print('top')
                    
                    if self.direction.y > 0: #moving up
                        self.hitbox.top = sprite.hitbox.bottom
                        print('bot')
        
    def update(self):
        self.input()
        self.move(self.speed)