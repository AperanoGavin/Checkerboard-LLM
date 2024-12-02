# main.py
import pygame
from checkerboard import draw_checkerboard
from config import SCREEN_HEIGHT , CASE_SIZE
from startmenu import draw_start_menu
from pieces import  BLACK_PIECE, WHITE_PIECE , init_pieces , draw_pieces
from game import Game

# Init of  Pygame
pygame.init()
font = pygame.font.Font("AntonSC-Regular.ttf", 50)  

# creat screen
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))
pygame.display.set_caption('checkerboard')





def main():
    running = True
    in_menu = True  # Flag pour savoir si on est dans le menu ou pas
    game = Game()  # Instancier la classe Game pour gérer la logique de jeu

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if in_menu:  # Si on est dans le menu
                    if SCREEN_HEIGHT // 3 < mouse_y < SCREEN_HEIGHT // 3 + 50:  # Start Game Button
                        in_menu = False  # Passer à l'état du jeu
                    elif SCREEN_HEIGHT // 2 < mouse_y < SCREEN_HEIGHT // 2 + 50:  # Custom Button
                        print("Opening Customization Menu...")
                        # Ajouter ici la logique pour personnaliser le jeu
                    elif SCREEN_HEIGHT // 1.5 < mouse_y < SCREEN_HEIGHT // 1.5 + 50:  # Quit Button
                        running = False  # Quitter le jeu

                else:  # Si on est dans le jeu
                    # Gérer la sélection et les déplacements des pièces
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    selected_piece = game.get_piece_at(mouse_x // CASE_SIZE * CASE_SIZE, mouse_y // CASE_SIZE * CASE_SIZE)

                    if game.selected_piece:
                        if game.is_valid_move(game.selected_piece, mouse_x, mouse_y):
                            #centrer les pieces
                            #game.move_piece(game.selected_piece, mouse_x, mouse_y)
                            game.move_piece(game.selected_piece, mouse_x // CASE_SIZE * CASE_SIZE, mouse_y // CASE_SIZE * CASE_SIZE)
                        game.selected_piece = None
                    elif selected_piece:
                        game.selected_piece = selected_piece

        if in_menu:
            draw_start_menu(screen)  # Afficher le menu
        else:
            draw_checkerboard(screen)  # Afficher le damier
            game.draw(screen)  # Afficher les pièces sur le damier

        pygame.display.flip()  # Mettre à jour l'écran

    pygame.quit()
    pygame.quit()
if __name__ == "__main__":
    main()
