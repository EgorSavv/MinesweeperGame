import pygame
pygame.init()

from settings import WIDTH, HEIGHT, FPS
from settings import CELL_SIZE, ROWS, COLS
from board import Board
from assets import cell_textures


window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

board = Board(ROWS, COLS)

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    for row in board.cells:
        for cell in row:
            x = cell.col * (CELL_SIZE + 1)
            y = cell.row * (CELL_SIZE + 1)
            texture = cell_textures[cell.texture_id]
            window.blit(texture, (x, y))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()