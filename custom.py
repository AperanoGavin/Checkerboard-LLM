import pygame
from config import SCREEN_HEIGHT, SCREEN_HEIGHT, CYAN, WHITE, BLUE, RED, YELLOW
from checkerboard import draw_checkerboard
from main   import font


def draw_custom_menu(screen):
    background = pygame.image.load("assets/background_R.jpeg") 
    background = pygame.transform.scale(background, (SCREEN_HEIGHT, SCREEN_HEIGHT))  
    screen.blit(background, (0, 0))  # Affiche l'image de fond

    # Titre
    custom_title = font.render("Choose Checkerboard Style", True, CYAN)
    screen.blit(custom_title, (SCREEN_HEIGHT // 2 - custom_title.get_width() // 2, SCREEN_HEIGHT // 6))

    # Styles de damier
    style_1_text = font.render("Style 1: Classic", True, WHITE)
    style_2_text = font.render("Style 2: Red/Blue", True, WHITE)
    style_3_text = font.render("Style 3: Gradient", True, WHITE)
    style_4_text = font.render("Style 4: Circles", True, WHITE)

    # Position des boutons
    screen.blit(style_1_text, (SCREEN_HEIGHT // 2 - style_1_text.get_width() // 2, SCREEN_HEIGHT // 3))
    screen.blit(style_2_text, (SCREEN_HEIGHT // 2 - style_2_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(style_3_text, (SCREEN_HEIGHT // 2 - style_3_text.get_width() // 2, SCREEN_HEIGHT // 1.5))
    screen.blit(style_4_text, (SCREEN_HEIGHT // 2 - style_4_text.get_width() // 2, SCREEN_HEIGHT // 1.3))

    # Ajouter un effet lumineux autour du texte
    pygame.draw.rect(screen, CYAN, (SCREEN_HEIGHT // 2 - style_1_text.get_width() // 2 - 10, SCREEN_HEIGHT // 3 - 10, style_1_text.get_width() + 20, style_1_text.get_height() + 20), 3)
    pygame.draw.rect(screen, BLUE, (SCREEN_HEIGHT // 2 - style_2_text.get_width() // 2 - 10, SCREEN_HEIGHT // 2 - 10, style_2_text.get_width() + 20, style_2_text.get_height() + 20), 3)
    pygame.draw.rect(screen, RED, (SCREEN_HEIGHT // 2 - style_3_text.get_width() // 2 - 10, SCREEN_HEIGHT // 1.5 - 10, style_3_text.get_width() + 20, style_3_text.get_height() + 20), 3)
    pygame.draw.rect(screen, YELLOW, (SCREEN_HEIGHT // 2 - style_4_text.get_width() // 2 - 10, SCREEN_HEIGHT // 1.3 - 10, style_4_text.get_width() + 20, style_4_text.get_height() + 20), 3)
