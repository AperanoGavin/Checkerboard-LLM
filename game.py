import pygame
from config import CASE_SIZE, CASES_NUMBER, WHITE, BLACK
from checkerboard import draw_checkerboard
from pieces import init_pieces, draw_pieces


class Game:
    def __init__(self):
        self.pieces = init_pieces()  # Initialiser les pièces
        self.selected_piece = None  # Aucune pièce sélectionnée au départ

    def get_piece_at(self, x, y):
        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                return piece
        return None

    ''' def move_piece(self, piece, new_x, new_y):
        piece.x = new_x
        piece.y = new_y '''  
        
    def move_piece(self, piece, new_x, new_y):
        if not (0 <= new_x < CASES_NUMBER * CASE_SIZE and 0 <= new_y < CASES_NUMBER * CASE_SIZE):
            return -1
        target_piece = self.get_piece_at(new_x, new_y)
        ''' if target_piece and target_piece.color != piece.color:
            # Capturer la pièce adverse
            self.pieces.remove(target_piece)
        
        # Déplacer la pièce sélectionnée
        piece.x = new_x
        piece.y = new_y '''
        
        # Empêcher l'empilement avec une pièce de la même couleur
        if target_piece and target_piece.color == piece.color:
            return -1  # Mouvement invalide : empilement

        # Vérifier que le mouvement est en diagonale
        dx = abs(new_x - piece.x)
        dy = abs(new_y - piece.y)
        if dx != dy or dx > CASE_SIZE:
            return -1  # Mouvement invalide : pas en diagonale

        # Capturer une pièce adverse si présente
        if target_piece and target_piece.color != piece.color:
            self.pieces.remove(target_piece)
            piece.x = new_x
            piece.y = new_y
            return 10  # Récompense pour capture

        # Déplacement simple
        piece.x = new_x
        piece.y = new_y
        return 1  # Récompense pour déplacement valide

        
        

    def draw(self, screen):
        draw_checkerboard(screen)
        draw_pieces(screen, self.pieces)
