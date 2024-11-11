# main.py
import pygame
from checkerboard import draw_checkerboard
from config import SCREEN_HEIGHT
from startmenu import draw_start_menu

# Init of  Pygame
pygame.init()
font = pygame.font.Font("AntonSC-Regular.ttf", 50)  

# creat screen
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))
pygame.display.set_caption('checkerboard')

# main loop
''' def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_checkerboard(screen)
        pygame.display.flip()

    # Quit Pygame
    pygame.quit() '''


def main():
    running = True
    in_menu = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if SCREEN_HEIGHT // 3 < mouse_y < SCREEN_HEIGHT // 3 + 50:  # Start Game
                    in_menu = False
                elif SCREEN_HEIGHT // 2 < mouse_y < SCREEN_HEIGHT // 2 + 50:  # Custom Button
                    print("Opening Customization Menu...")
                    # Ajouter ici la logique pour personnaliser le jeu
                elif SCREEN_HEIGHT // 1.5 < mouse_y < SCREEN_HEIGHT // 1.5 + 50:  # Quit Button
                    running = False

        if in_menu:
            draw_start_menu(screen)
        else:
            draw_checkerboard(screen)  # Fonction à définir pour afficher le damier futuriste
        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main()
