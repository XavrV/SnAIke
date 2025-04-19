import pygame
import random
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from game.snake_game import SnakeGame


def random_action():
    # Acción codificada como: [straight, right, left]
    actions = [
        [1, 0, 0],  # straight
        [0, 1, 0],  # right
        [0, 0, 1],  # left
    ]
    return random.choice(actions)


def test_play_loop(steps=20):
    game = SnakeGame(width=10, height=10)

    print("Iniciando juego de prueba con visualización...\n")
    for i in range(steps):
        action = random_action()
        reward, game_over, score = game.play_step(action)

        print(
            f"Step {i + 1}: Acción={action}, Reward={reward}, Score={score}, Game Over={game_over}"
        )
        game.render_pygame()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    test_play_loop()
