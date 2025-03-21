import pygame
from circleshape import CircleShape
import constants
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
     def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0 
        self.shoottimer = 0 
     def draw(self, screen):
         pygame.draw.polygon(screen, "white", self.triangle(), 2)
     def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 

     def move(self, dt):
         forward = pygame.Vector2(0, 1).rotate(self.rotation)
         self.position += forward * PLAYER_SPEED * dt

     def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoottimer -= dt  

        if keys[pygame.K_a]:
             self.rotate(-dt)
        if keys[pygame.K_d]:
             self.rotate(dt)
        if keys[pygame.K_w]:
             self.move(dt)
        if keys[pygame.K_s]:
             self.move(-dt)
        if keys[pygame.K_SPACE]:
         return self.shoot() 
        
        return None          

     # in the player class
     def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    

     def shoot(self): 
         if self.shoottimer <= 0:
          forward = pygame.Vector2(0, 1).rotate(self.rotation)
          shot_position = self.position + forward * self.radius  
          new_shot = Shot(shot_position.x, shot_position.y, SHOT_RADIUS)
          new_shot.velocity = forward * PLAYER_SHOOT_SPEED
          self.shoottimer += PLAYER_SHOOT_COOLDOWN
         
          return new_shot
         else:
          return None
     
