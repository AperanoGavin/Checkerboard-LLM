import pygame
from config import CASE_SIZE, CASES_NUMBER, WHITE, BLACK
from checkerboard import draw_checkerboard
from pieces import init_pieces, draw_pieces

WHITE_PIECE = (102, 0, 0)
BLACK_PIECE = (160, 160, 160)

class Game:
    def __init__(self):
        self.pieces = init_pieces()  # Initialiser les pièces
        self.selected_piece = None  # Aucune pièce sélectionnée au départ
        self.current_player = WHITE_PIECE
        
    def switch_player(self):
        #Changer le joueur actuel
        self.current_player = BLACK_PIECE if self.current_player == WHITE_PIECE else WHITE_PIECE

    def get_piece_at(self, x, y):
        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                return piece
        return None
        
    def move_piece(self, piece, new_x, new_y):

        if not (0 <= new_x < CASES_NUMBER * CASE_SIZE and 0 <= new_y < CASES_NUMBER * CASE_SIZE):
            return -1
        target_piece = self.get_piece_at(new_x, new_y)

        
        # Empêcher l'empilement avec une pièce de la même couleur
        if target_piece and target_piece.color == piece.color:
            return -1  # Mouvement invalide : empilement

        # Vérifier que le mouvement est en diagonale
        dx = abs(new_x - piece.x)
        dy = abs(new_y - piece.y)
        print(f"Attempting move: {piece.x, piece.y} -> {new_x, new_y} | dx: {dx}, dy: {dy}")

        if dx != dy or dx > CASE_SIZE:
            return -1  # Mouvement invalide : pas en diagonale

        # Gestion de la capture
        if dx == 2 * CASE_SIZE:  # Vérifier si c'est un saut
            mid_x = (piece.x + new_x) // 2
            mid_y = (piece.y + new_y) // 2
            captured_piece = self.get_piece_at(mid_x, mid_y)
            

            if captured_piece and captured_piece.color != piece.color:
                # Vérifier que la case derrière est libre
                if target_piece is None:
                    print(f"Captured piece found at {mid_x, mid_y}, removing it.")

                    self.pieces.remove(captured_piece)  # Retirer la pièce capturée
                    print(f"Piece at {mid_x, mid_y} has been captured")
                    piece.x = new_x
                    piece.y = new_y
                    return 10  # Récompense pour capture
                else:
                    return -1  # Mouvement invalide : case derrière occupée

        # Déplacement simple
        piece.x = new_x
        piece.y = new_y
        return 1  # Récompense pour déplacement valide

        
        

    def draw(self, screen):
        draw_checkerboard(screen)
        draw_pieces(screen, self.pieces)
        
    def is_game_over(self):
        white_pieces = [piece for piece in self.pieces if piece.color == WHITE_PIECE]
        black_pieces = [piece for piece in self.pieces if piece.color == BLACK_PIECE]
        return not white_pieces or not black_pieces
