import pygame
import random
from src.game.snake_game import SnakeGame
from src.state.state_representation import get_state

def random_action():
    return random.choice([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

def visualizar_estado(num_pasos=30):
    game = SnakeGame()
    print("Visualización de vectores de estado:")

    for paso in range(num_pasos):
        action = random_action()
        reward, done, score = game.play_step(action)
        state = get_state(game)

        print(f"Paso {paso+1}")
        print("Estado:", state)
        print("Score:", score)
        print("Reward:", reward)
        print()

        game.render_pygame(speed=5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if done:
            print("Colisión: reiniciando...\n")
            game.reset()

if __name__ == "__main__":
    visualizar_estado()