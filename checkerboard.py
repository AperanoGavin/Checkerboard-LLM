import pygame
from config import CASE_SIZE, CASES_NUMBER, WHITE, BLACK 

def draw_checkerboard(screen):
    screen.fill(WHITE)
    for ligne in range(CASES_NUMBER):
        for colonne in range(CASES_NUMBER):
            if (ligne + colonne) % 2 == 1:
                pygame.draw.rect(
                    screen,
                    BLACK,
                    (colonne * CASE_SIZE, ligne * CASE_SIZE, CASE_SIZE, CASE_SIZE)
                )
