import pygame
from config import CASE_SIZE, CASES_NUMBER, WHITE, BLACK
from checkerboard import draw_checkerboard
from pieces import init_pieces, draw_pieces

WHITE_PIECE = (102, 0, 0)
BLACK_PIECE = (160, 160, 160)

class Game:
    def __init__(self):
        self.pieces = init_pieces()
        print(f"Initial pieces: {len(self.pieces)}")  # Debug: afficher nombre initial
        self.selected_piece = None
        self.current_player = WHITE_PIECE
        
    def switch_player(self):
        self.current_player = BLACK_PIECE if self.current_player == WHITE_PIECE else WHITE_PIECE
    
    def get_piece_at(self, x, y):
        pieces_at_pos = [piece for piece in self.pieces if piece.x == x and piece.y == y]
        if len(pieces_at_pos) > 1:
            print(f"WARNING: Multiple pieces at {x},{y}: {pieces_at_pos}")  # Debug
        return pieces_at_pos[0] if pieces_at_pos else None
        
    def move_piece(self, piece, new_x, new_y):
        print(f"\nAttempting move from ({piece.x},{piece.y}) to ({new_x},{new_y})")  # Debug
        print(f"Current pieces count: {len(self.pieces)}")  # Debug
        
        # Vérifications minimales des limites du plateau
        if not (0 <= new_x < CASES_NUMBER * CASE_SIZE and 0 <= new_y < CASES_NUMBER * CASE_SIZE):
            print("Move invalid: out of bounds")  # Debug
            return -1

        # Vérifier si la destination est occupée
        target_piece = self.get_piece_at(new_x, new_y)
        if target_piece:
            print(f"Move invalid: destination occupied by {target_piece.color}")  # Debug
            return -1

        # Calculer le déplacement
        dx = abs(new_x - piece.x)
        dy = abs(new_y - piece.y)
        
        #print(f"Movement deltas: dx={dx}, dy={dy}")  # Debug

        # Vérifier mouvement diagonal
        if dx != dy:
            #print("Move invalid: not diagonal")  # Debug
            return -1

        # Copie de sauvegarde des coordonnées originales
        original_x, original_y = piece.x, piece.y

        print(f"dx: {dx}, CASE_SIZE: {CASE_SIZE}, dx == 2 * CASE_SIZE: {dx == 2 * CASE_SIZE}")  # Debug
        count = 10
        # Gestion de la capture
        if dx == 2 * CASE_SIZE:  # Saut potentiel
            mid_x = (piece.x + new_x) // 2
            mid_y = (piece.y + new_y) // 2
            captured_piece = self.get_piece_at(mid_x, mid_y)
            
            print(f"Checking capture at middle point ({mid_x},{mid_y})")  # Debug
            if captured_piece:
                print(f"Found piece to capture: color={captured_piece.color}")  # Debug
            
            if captured_piece and captured_piece.color != piece.color:
                print("Capturing piece!")  # Debug
                # Vérifier que la pièce à capturer existe bien dans la liste
                if captured_piece in self.pieces:
                    self.pieces.remove(captured_piece)
                    piece.x = new_x
                    piece.y = new_y
                    print(f"Pieces after capture: {len(self.pieces)}")  # Debug
                    return 10
                else:
                    print("WARNING: Piece to capture not found in pieces list")  # Debug
                    piece.x = original_x
                    piece.y = original_y
                    return -1
        
        # Déplacement simple
        elif dx == CASE_SIZE:
            piece.x = new_x
            piece.y = new_y
            print(f"Simple move successful to ({new_x},{new_y})")  # Debug
            return 1
            
        #print("Move invalid: unknown reason")  # Debug
        piece.x = original_x
        piece.y = original_y
        return -1
        
    def draw(self, screen):
        draw_checkerboard(screen)
        draw_pieces(screen, self.pieces)
        
    def is_game_over(self):
        white_pieces = [piece for piece in self.pieces if piece.color == WHITE_PIECE]
        black_pieces = [piece for piece in self.pieces if piece.color == BLACK_PIECE]
        
        print(f"Game state check - White pieces: {len(white_pieces)}, Black pieces: {len(black_pieces)}")  # Debug
        return not white_pieces or not black_pieces
    
    #toutes les captures possibles pour le joueur actuel
    def find_captures(self):
        """
            Retourne toutes les captures possibles pour le joueur actuel.
        """
        captures = []
        for piece in self.pieces:
            if piece.color == self.current_player:
                for dx, dy in [(2 * CASE_SIZE, 2 * CASE_SIZE), (2 * CASE_SIZE, -2 * CASE_SIZE),
                            (-2 * CASE_SIZE, 2 * CASE_SIZE), (-2 * CASE_SIZE, -2 * CASE_SIZE)]:
                    new_x = piece.x + dx
                    new_y = piece.y + dy
                    mid_x = (piece.x + new_x) // 2
                    mid_y = (piece.y + new_y) // 2
                    captured_piece = self.get_piece_at(mid_x, mid_y)
                    target_piece = self.get_piece_at(new_x, new_y)

                    if captured_piece and captured_piece.color != piece.color and target_piece is None:
                        captures.append(((piece.x, piece.y), (new_x, new_y)))
        return captures
    
