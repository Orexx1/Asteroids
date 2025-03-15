import pygame 
from constants import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    while True:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return
        screen.fill((0, 0, 0))
        pygame.display.flip()
    print ("Starting Asteroids!")
    print ("Screen width: 1280")
    print ("Screen height: 720")




if __name__ == "__main__":
    main()