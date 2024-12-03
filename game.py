import pygame
from config import CASE_SIZE, CASES_NUMBER, WHITE, BLACK
from checkerboard import draw_checkerboard
from pieces import init_pieces, draw_pieces
from startmenu import draw_start_menu

VERTICAL_OFFSET = -60
current_player = 1


class Game:
    def __init__(self):
        self.pieces = init_pieces()  # Initialiser les pièces
        self.selected_piece = None  # Aucune pièce sélectionnée au départ

    def get_piece_at(self, x, y):
        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                return piece
        return None

    def is_valid_move(self, piece, new_x, new_y):
        # Vérifier si le mouvement est valide (par exemple, mouvement diagonal d'une case)
        dx = abs(piece.x // CASE_SIZE - new_x // CASE_SIZE)
        dy = abs(piece.y // CASE_SIZE - new_y // CASE_SIZE)
        return dx == dy == 1  # Déplacement diagonal d'une case

    def move_piece(self, piece, new_x, new_y):
        piece.x = new_x
        piece.y = new_y  


    def draw(self, screen):
        draw_checkerboard(screen)
        draw_pieces(screen, self.pieces)




