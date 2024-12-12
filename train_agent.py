import numpy as np
import random
from game import Game
from agent.QAgent import QAgent
def train_agent(episodes=1000):
    game = Game()
    agent = QAgent()

    for episode in range(episodes):
        game.__init__()  # Réinitialiser le jeu
        while not game.is_game_over():
            state = game.get_state()
            valid_actions = game.get_valid_moves(agent.current_player)
            
            if valid_actions:
                action = agent.choose_action(state, valid_actions)
                reward = game.apply_move(agent.current_player, action)
                next_state = game.get_state()
                next_valid_actions = game.get_valid_moves(-agent.current_player)
                
                # Mettre à jour la Q-Table
                agent.update_q_value(state, action, reward, next_state, next_valid_actions)
            
            # Passer à l'autre joueur
            agent.current_player *= -1
