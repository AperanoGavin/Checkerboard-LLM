import pygame
import matplotlib.pyplot as plt
from checkerboard import draw_checkerboard
from config import SCREEN_HEIGHT, CASE_SIZE
from pieces import init_pieces, draw_pieces
from game import Game , WHITE_PIECE , BLACK_PIECE
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
    game = Game()
    agent = QAgent()

    running = True
    
    pygame.time.wait(900)
    

    while running:
        clock.tick(0.1)
        state = tuple((piece.x, piece.y, piece.color) for piece in game.pieces)  # État actuel du jeu
        
        valid_actions = QAgent.generate_valid_actions(game)  # Actions valides dynamiques

        # L'agent choisit une action
        if valid_actions:
            if game.current_player == WHITE_PIECE:
                # Tour de l'agent blanc
                action = agent.choose_action(state, valid_actions)
                selected_piece_pos, new_pos = action
                selected_piece = game.get_piece_at(*selected_piece_pos)

                if selected_piece and selected_piece.color == WHITE_PIECE:
                    reward = game.move_piece(selected_piece, *new_pos)
                    next_state = tuple((piece.x, piece.y, piece.color) for piece in game.pieces)
                    next_valid_actions = QAgent.generate_valid_actions(game)
                    agent.update_q_value(state, action, reward, next_state, next_valid_actions)

            elif game.current_player == BLACK_PIECE:
                # Tour de l'agent noir
                action = agent.choose_action(state, valid_actions)
                selected_piece_pos, new_pos = action
                selected_piece = game.get_piece_at(*selected_piece_pos)

                if selected_piece and selected_piece.color == BLACK_PIECE:
                    reward = game.move_piece(selected_piece, *new_pos)
                    next_state = tuple((piece.x, piece.y, piece.color) for piece in game.pieces)
                    next_valid_actions = QAgent.generate_valid_actions(game)
                    agent.update_q_value(state, action, reward, next_state, next_valid_actions)

            # Passer au joueur suivant après chaque tour
            game.switch_player()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Redessiner l'écran
        draw_checkerboard(screen)
        game.draw(screen)
        pygame.display.flip()
       

    pygame.quit()

if __name__ == "__main__":
    main()