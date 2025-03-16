import pygame 
from constants import *
from player import Player
import circleshape
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
     
    print ("Starting Asteroids!")
    print ("Screen width: 1280")
    print ("Screen height: 720")

    while True:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return
        dt = clock.tick(60) / 1000  
        updatable.update(dt)
        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
    

if __name__ == "__main__":
    main()