import pygame
import matplotlib.pyplot as plt
from checkerboard import draw_checkerboard
from config import SCREEN_HEIGHT, CASE_SIZE
from pieces import init_pieces, draw_pieces
from game import Game, WHITE_PIECE, BLACK_PIECE
from agent.QAgent import QAgent 

# Init of Pygame
pygame.init()
font = pygame.font.Font("AntonSC-Regular.ttf", 50)

# Create screen
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))
pygame.display.set_caption('checkerboard')

clock = pygame.time.Clock()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))
    pygame.display.set_caption('checkerboard')
    running = True
    
    # Créer un agent et un jeu au début
    agent = QAgent()
    
    #attendre avant de commencer

    while running:
        # Réinitialiser le jeu à chaque match
        game = Game()
        game_over = False  # Flag pour détecter la fin du jeu
        
        while not game_over:
            clock.tick(10)
            state = tuple((piece.x, piece.y, piece.color) for piece in game.pieces)  # État actuel
            all_actions = QAgent.generate_all_actions(game)  # Toutes les actions possibles
            
             # L'agent choisit une action parmi toutes les actions
            action = agent.choose_action(state, all_actions)
            selected_piece_pos, new_pos = action
            selected_piece = game.get_piece_at(*selected_piece_pos)
            
            if selected_piece and selected_piece.color == game.current_player:
            # Effectuer le déplacement et obtenir une récompense
                reward = game.move_piece(selected_piece, *new_pos)
                next_state = tuple((piece.x, piece.y, piece.color) for piece in game.pieces)

                # Mettre à jour les valeurs Q de l'agent
                agent.update_q_value(state, action, reward, next_state, all_actions)


                # Passer au joueur suivant
            game.switch_player()

            # Vérifier si le jeu est terminé
            if game.is_game_over():
                game_over = True

            # Gérer les événements utilisateur (comme quitter le jeu)
            ''' for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False '''

            # Redessiner l'écran
            draw_checkerboard(screen)
            game.draw(screen)
            pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
