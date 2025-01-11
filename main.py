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

    # Créer un agent
    agent = QAgent()

    # Paramètres d'entraînement
    num_episodes = 1000  # Nombre de parties
    reward_history = []  # Historique des récompenses cumulées
    pieces_captured_history = []  # Historique des captures

    running = True
    for episode in range(num_episodes):
        # Initialiser un nouveau jeu
        game = Game()
        game_over = False
        total_reward = 0  # Récompense cumulée pour l'épisode
        pieces_captured = 0  # Compteur de pièces capturées

        while not game_over and running:
            clock.tick(30)  # Limiter les FPS pour une visualisation fluide
            state = tuple((piece.x, piece.y, piece.color) for piece in game.pieces)  # État actuel
            all_actions = QAgent.generate_all_actions(game)  # Toutes les actions possibles
            
            # L'agent choisit une action
            action = agent.choose_action(state, all_actions)
            selected_piece_pos, new_pos = action
            selected_piece = game.get_piece_at(*selected_piece_pos)

            if selected_piece and selected_piece.color == game.current_player:
                # Effectuer le déplacement et obtenir une récompense
                reward = game.move_piece(selected_piece, *new_pos)
                total_reward += reward  # Ajouter à la récompense cumulée

                # Si une capture a eu lieu, l'incrémenter
                if reward == 10:
                    pieces_captured += 1

                next_state = tuple((piece.x, piece.y, piece.color) for piece in game.pieces)

                # Mettre à jour les valeurs Q de l'agent
                agent.update_q_value(state, action, reward, next_state, all_actions)

                # Passer au joueur suivant
                game.switch_player()

            # Vérifier si le jeu est terminé
            if game.is_game_over():
                game_over = True

            # Gérer les événements utilisateur (comme quitter le jeu)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

            # Afficher le jeu graphiquement
            draw_checkerboard(screen)
            game.draw(screen)
            pygame.display.flip()

        # Enregistrer les métriques pour cet épisode
        reward_history.append(total_reward)
        pieces_captured_history.append(pieces_captured)

        # Afficher la progression dans la console
        if episode % 100 == 0:
            print(f"Épisode {episode}/{num_episodes} - Récompense cumulée: {total_reward}, Pièces capturées: {pieces_captured}")

    # Tracer la courbe de progression après l'entraînement
    plot_training_progress(reward_history, pieces_captured_history)

    pygame.quit()

def plot_training_progress(reward_history, pieces_captured_history):
    """Tracer les courbes de récompenses et de captures au fil des épisodes."""
    plt.figure(figsize=(12, 6))

    # Récompenses cumulées
    plt.subplot(1, 2, 1)
    plt.plot(reward_history, label="Récompense cumulée", color="blue")
    plt.xlabel("Épisode")
    plt.ylabel("Récompense")
    plt.title("Évolution des récompenses")
    plt.legend()

    # Captures
    plt.subplot(1, 2, 2)
    plt.plot(pieces_captured_history, label="Pièces capturées", color="green")
    plt.xlabel("Épisode")
    plt.ylabel("Captures")
    plt.title("Évolution des captures")
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
