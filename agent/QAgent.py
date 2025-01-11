import numpy as np
import random
from config import SCREEN_HEIGHT, CASE_SIZE , CASES_NUMBER
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

    def choose_action(self, state, all_possible_actions):
        """Choisir une action en fonction de l'exploration ou de l'exploitation."""
        import random

        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(all_possible_actions)  # Exploration

        # Exploitation : choisir l'action avec la plus haute valeur Q
        q_values = {action: self.q_table.get((state, action), 0) for action in all_possible_actions}
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

 

    ''' def generate_all_actions(game):
        all_actions = []
        for piece in game.pieces:
            for dx in [-CASE_SIZE, CASE_SIZE]:
                for dy in [-CASE_SIZE, CASE_SIZE]:
                    new_x = piece.x + dx
                    new_y = piece.y + dy
                    all_actions.append(((piece.x, piece.y), (new_x, new_y)))
        return all_actions '''
    
    
    ''' def generate_all_actions(game):
        all_actions = []
        for piece in game.pieces:
            # Pour chaque pièce, ajouter des déplacements simples et des captures potentielles
            for dx in [-CASE_SIZE, CASE_SIZE]:
                for dy in [-CASE_SIZE, CASE_SIZE]:
                    new_x = piece.x + dx
                    new_y = piece.y + dy

                    # Vérifier si c'est un saut (capture)
                    if abs(new_x - piece.x) == 2 * CASE_SIZE and abs(new_y - piece.y) == 2 * CASE_SIZE:
                        mid_x = (piece.x + new_x) // 2
                        mid_y = (piece.y + new_y) // 2
                        captured_piece = game.get_piece_at(mid_x, mid_y)

                        # Vérifier qu'il y a bien une pièce capturée et que la case de destination est libre
                        if captured_piece and captured_piece.color != piece.color and not game.get_piece_at(new_x, new_y):
                            all_actions.append(((piece.x, piece.y), (new_x, new_y)))  # Ajouter l'action de capture
                    else:
                        # Sinon, ajouter les mouvements simples
                        all_actions.append(((piece.x, piece.y), (new_x, new_y)))
        return all_actions '''


        
    def generate_all_actions(game):
        all_actions = []
    # Ajouter d'abord les captures possibles
        captures = game.find_captures()
        for capture in captures:
            start_pos, end_pos = capture
            new_x, new_y = end_pos
            # Vérifications minimales des limites du plateau
            if 0 <= new_x < CASES_NUMBER * CASE_SIZE and 0 <= new_y < CASES_NUMBER * CASE_SIZE:
                all_actions.append(capture)
            else:
                print("Capture invalid: out of bounds")  # Debug

        # Si aucune capture n'est possible, ajouter des déplacements simples
        if not all_actions:
            for piece in game.pieces:
                if piece.color == game.current_player:
                    for dx in [-CASE_SIZE, CASE_SIZE]:
                        for dy in [-CASE_SIZE, CASE_SIZE]:
                            next_x = piece.x + dx
                            next_y = piece.y + dy
                            if 0 <= next_x < CASES_NUMBER * CASE_SIZE and 0 <= next_y < CASES_NUMBER * CASE_SIZE and not game.get_piece_at(next_x, next_y):
                                action = ((piece.x, piece.y), (next_x, next_y))
                                all_actions.append(action)
        return all_actions




