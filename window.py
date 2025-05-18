import pygame
import numpy as np

class SudokuVisualizer:
    def __init__(self, width=540, height=540) -> None:
        pygame.init()
        self.rows, self.cols = 9, 9
        self.width = width
        self.height = height
        self.cell_size = width // self.cols
        self.line_width = 2

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sudoku Grid")

        self.font = pygame.font.SysFont('Arial', 40)
        self.colors = {
            'white': (255, 255, 255),
            'black': (0, 0, 0),
            'gray': (200, 200, 200),
            'blue': (0, 0, 255)
        }

        self.clock = pygame.time.Clock()

    def draw_grid(self) -> None:

        for i in range(1, self.rows + 1):
            pygame.draw.line(
                self.screen, self.colors['gray'],
                (0, i * self.cell_size), (self.width, i * self.cell_size), 1
            )
            pygame.draw.line(
                self.screen, self.colors['gray'],
                (i * self.cell_size, 0), (i * self.cell_size, self.height), 1
            )

        for i in range(1, self.rows + 1):
            if i % 3 == 0:
                pygame.draw.line(
                    self.screen, self.colors['black'],
                    (0, i * self.cell_size), (self.width, i * self.cell_size), 4
                )
                pygame.draw.line(
                    self.screen, self.colors['black'],
                    (i * self.cell_size, 0), (i * self.cell_size, self.height), 4
                )

    def draw_numbers(self, current, original) -> None:

        # Draw current
        for i in range(self.rows):
            for j in range(self.cols):
                num = current[i][j]
                if num != 0:
                    text = self.font.render(str(num), True, self.colors['black'])
                    self.screen.blit(
                        text,
                        (j * self.cell_size + 20, i * self.cell_size + 10)
                    )
        
        # Draw originals
        for i in range(self.rows):
            for j in range(self.cols):
                num = original[i][j]
                if num != 0:
                    text = self.font.render(str(num), True, self.colors['blue'])
                    self.screen.blit(
                        text,
                        (j * self.cell_size + 20, i * self.cell_size + 10)
                    )

    def draw_rect(self, index) -> None:
        pygame.draw.rect(self.screen, self.colors['gray'], (index[1] * self.cell_size, index[0] * self.cell_size, self.cell_size, self.cell_size))

    def flip(self) -> None:
        pygame.display.flip()

    def quit(self) -> None:
        pygame.quit()
