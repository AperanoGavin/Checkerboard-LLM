import numpy as np
from config import SCREEN_HEIGHT, CASE_SIZE
from checkerboard import draw_checkerboard
from pieces import init_pieces, draw_pieces
from game import Game

class QAgent:
    def __init__(self, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0, exploration_decay=0.99):
        self.q_table = {}
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay

    def choose_action(self, state, valid_actions):
        """Choisir une action en fonction de l'exploration ou de l'exploitation."""
        import random

        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(valid_actions)  # Exploration

        # Exploitation : choisir l'action avec la plus haute valeur Q
        q_values = {action: self.q_table.get((state, action), 0) for action in valid_actions}
        return max(q_values, key=q_values.get)

    def update_q_value(self, state, action, reward, next_state, next_valid_actions):
        """Mettre à jour la Q-Table en fonction de l'algorithme Q-Learning."""
        max_future_q = max(
            [self.q_table.get((next_state, next_action), 0) for next_action in next_valid_actions],
            default=0
        )
        current_q = self.q_table.get((state, action), 0)

        # Calcul de la nouvelle valeur Q
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_future_q - current_q)
        self.q_table[(state, action)] = new_q

    def decay_exploration(self):
        """Réduire progressivement le taux d'exploration."""
        self.exploration_rate *= self.exploration_decay
        self.exploration_rate = max(self.exploration_rate, 0.1)


    def generate_valid_actions(game):
        """Génère toutes les actions valides (mouvements possibles) pour l'état actuel."""
        valid_actions = []
        for piece in game.pieces:
            for dx in [-CASE_SIZE, CASE_SIZE]:
                for dy in [-CASE_SIZE, CASE_SIZE]:
                    new_x = piece.x + dx
                    new_y = piece.y + dy

                    # Ajouter l'action uniquement si elle respecte les règles (aucune validation forcée ici)
                    valid_actions.append(((piece.x, piece.y), (new_x, new_y)))
        return valid_actions




