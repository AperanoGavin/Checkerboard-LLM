import pygame
from config import CASE_SIZE, CASES_NUMBER, WHITE, BLACK
from checkerboard import draw_checkerboard
from pieces import init_pieces, draw_pieces

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

    def move_piece(self, piece, new_x, new_y):
        piece.x = new_x
        piece.y = new_y  

    def draw(self, screen):
        draw_checkerboard(screen)
        draw_pieces(screen, self.pieces)