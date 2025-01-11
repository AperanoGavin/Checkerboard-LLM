import pygame
from config import CASE_SIZE

WHITE_PIECE = (102, 0, 0)
BLACK_PIECE = (160, 160, 160)



class Dame:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen):
        radius = CASE_SIZE // 2 - 10  # Taille de la pièce
        pygame.draw.circle(screen, self.color, (self.x + CASE_SIZE // 2, self.y + CASE_SIZE // 2), radius)



def init_pieces():
    pieces = []
    
    # Pour un damier 5x5 :
    # 5 pièces noires en haut sur les cases noires
    black_positions = [(1, 0), (3, 0), (0, 1), (2, 1), (4, 1)]
    

    
    # 3 pièces blanches en bas sur les cases noires
    white_positions = [(0, 3), (2, 3), (4, 3), (1, 4), (3, 4)]
    
    # Ajouter les pièces noires
    for col, row in black_positions:
        pieces.append(Dame(col * CASE_SIZE, row * CASE_SIZE, BLACK_PIECE))
    
    # Ajouter les pièces blanches
    for col, row in white_positions:
        pieces.append(Dame(col * CASE_SIZE, row * CASE_SIZE, WHITE_PIECE))
    
    return pieces

pieces = init_pieces()

def draw_pieces(screen, pieces):
    for piece in pieces:
        piece.draw(screen)