import pygame
from config import CASE_SIZE

WHITE_PIECE = (255, 255, 255)
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

    # Ajouter les pièces noires sur le plateau
    for row in range(2): 
        for col in range(8):
            if (row + col) % 2 == 1:  
                pieces.append(Dame(col * CASE_SIZE, row * CASE_SIZE, BLACK_PIECE))

    # Ajouter les pièces blanches sur le plateau
    for row in range(3, 5):  
        for col in range(8):
            if (row + col) % 2 == 1:
                pieces.append(Dame(col * CASE_SIZE, row * CASE_SIZE, WHITE_PIECE))

    return pieces

pieces = init_pieces()

def draw_pieces(screen, pieces):
    for piece in pieces:
        piece.draw(screen)