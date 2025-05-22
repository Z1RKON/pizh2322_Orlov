import pygame
from game_objects import Snake, Apple
from utils import handle_keys
from constants import *

def main():
    """Основная функция игры."""
    # Настройка экрана
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Змейка')
    clock = pygame.time.Clock()

    # Создание объектов
    snake = Snake()
    apple = Apple()

    while True:
        # Обработка событий
        handle_keys(snake)

        # Обновление состояния игры
        snake.update_direction()
        snake.move()

        # Проверка съедания яблока
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()
            # Убедимся, что яблоко не появилось на змейке
            while apple.position in snake.positions:
                apple.randomize_position()

        # Отрисовка
        screen.fill(SCREEN_COLOR)
        snake.draw(screen)
        apple.draw(screen)
        pygame.display.update()

        # Контроль FPS
        clock.tick(FPS)

if __name__ == "__main__":
    main()