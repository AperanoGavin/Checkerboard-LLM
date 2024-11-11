import pygame
from config import CASE_SIZE, CASES_NUMBER, WHITE, BLACK  , SCREEN_HEIGHT  , CYAN , BLUE , RED
current_style = 1

def draw_checkerboard(screen, style):
    screen.fill(WHITE)  # Remplir l'arrière-plan avec une couleur de fond

    # Dessiner le damier selon le style sélectionné
    for ligne in range(CASES_NUMBER):
        for colonne in range(CASES_NUMBER):
            if style == 1:  # Damier classique noir et blanc
                color = BLACK if (ligne + colonne) % 2 == 1 else WHITE
            elif style == 2:  # Damier avec couleurs rouge et bleu
                color = RED if (ligne + colonne) % 2 == 1 else BLUE
            elif style == 3:  # Damier avec dégradé de couleurs
                color = (ligne * 30 % 255, colonne * 30 % 255, (ligne + colonne) * 20 % 255)
            elif style == 4:  # Damier avec motif en cercle
                if (ligne + colonne) % 2 == 0:
                    pygame.draw.circle(screen, WHITE, (colonne * CASE_SIZE + CASE_SIZE // 2, ligne * CASE_SIZE + CASE_SIZE // 2), CASE_SIZE // 3)
                else:
                    color = BLACK
            pygame.draw.rect(screen, color, (colonne * CASE_SIZE, ligne * CASE_SIZE, CASE_SIZE, CASE_SIZE))

