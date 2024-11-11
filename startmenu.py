import pygame
from config import CASE_SIZE, CASES_NUMBER, WHITE, BLACK  , SCREEN_HEIGHT  , CYAN , BLUE , RED


def draw_start_menu(screen):
    font = pygame.font.Font("AntonSC-Regular.ttf", 50) 
    # Charger l'image de fond depuis le dossier "assets"
    background = pygame.image.load("assets/background_R.jpeg") 
    background = pygame.transform.scale(background, (SCREEN_HEIGHT, SCREEN_HEIGHT))  


    #screen.fill(BLACK)
    screen.blit(background, (10, 0)) 

    # Boutons
    start_text = font.render("Start Game", True, CYAN)
    custom_text = font.render("Custom", True, BLUE)
    quit_text = font.render("Quit", True, RED)

    # Position des boutons
    screen.blit(start_text, (SCREEN_HEIGHT // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 3))
    screen.blit(custom_text, (SCREEN_HEIGHT // 2 - custom_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(quit_text, (SCREEN_HEIGHT // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 1.5))

    # Ajouter un effet lumineux autour du texte
    pygame.draw.rect(screen, CYAN, (SCREEN_HEIGHT // 2 - start_text.get_width() // 2 - 10, SCREEN_HEIGHT // 3 - 10, start_text.get_width() + 20, start_text.get_height() + 20), 3)
    pygame.draw.rect(screen, BLUE, (SCREEN_HEIGHT // 2 - custom_text.get_width() // 2 - 10, SCREEN_HEIGHT // 2 - 10, custom_text.get_width() + 20, custom_text.get_height() + 20), 3)
    pygame.draw.rect(screen, RED, (SCREEN_HEIGHT // 2 - quit_text.get_width() // 2 - 10, SCREEN_HEIGHT // 1.5 - 10, quit_text.get_width() + 20, quit_text.get_height() + 20), 3)
