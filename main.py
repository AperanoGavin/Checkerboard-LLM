# main.py
import pygame
from checkerboard import draw_checkerboard
from config import SCREEN_HEIGHT, CASE_SIZE
from pieces import BLACK_PIECE, WHITE_PIECE, init_pieces, draw_pieces
from game import Game

# Init of Pygame
pygame.init()
font = pygame.font.Font("AntonSC-Regular.ttf", 50)

# Create screen
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))
pygame.display.set_caption('checkerboard')

current_player = 1

def main():
    running = True
    game = Game()  # Instancier la classe Game pour gérer la logique de jeu

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Gérer la sélection et les déplacements des pièces
                selected_piece = game.get_piece_at(mouse_x // CASE_SIZE * CASE_SIZE, mouse_y // CASE_SIZE * CASE_SIZE)

                if game.selected_piece:
                    if game.is_valid_move(game.selected_piece, mouse_x, mouse_y):
                        # Centrer les pièces
                        game.move_piece(game.selected_piece, mouse_x // CASE_SIZE * CASE_SIZE, mouse_y // CASE_SIZE * CASE_SIZE)
                    game.selected_piece = None
                elif selected_piece:
                    game.selected_piece = selected_piece

        draw_checkerboard(screen)  # Afficher le damier
        game.draw(screen)  # Afficher les pièces sur le damier

        pygame.display.flip()  # Mettre à jour l'écran

    pygame.quit()

if __name__ == "__main__":
    main()