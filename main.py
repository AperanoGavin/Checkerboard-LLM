# main.py
import pygame
from checkerboard import draw_checkerboard
from config import SCREEN_HEIGHT

# Init of  Pygame
pygame.init()

# creat screen
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))
pygame.display.set_caption('checkerboard')

# main loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_checkerboard(screen)
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
