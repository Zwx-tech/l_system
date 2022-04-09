from lsystem import *
import pygame

if __name__ == "__main__":
    # set up pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # set up lsystem object
    #l_sys = load_lsystem_from_file("blueprints/tris.txt")
    #l_sys = load_lsystem_from_file("blueprints/binary.txt")
    l_sys = load_lsystem_from_file("blueprints/plant.txt")
    #l_sys = load_lsystem_from_file("blueprints/sierpinski.txt")
    #l_sys = load_lsystem_from_file("blueprints/sierpinski_curve.txt")
    #l_sys = load_lsystem_from_file("blueprints/dragon.txt")
    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN: # on mouse click generate next recursion(generation)
                screen.fill((0, 0, 0))
                l_sys.draw()
                l_sys.generate()
        pygame.display.flip()