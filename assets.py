import pygame
from settings import CELL_SIZE

# текстуры клетки
cell_texture1 = pygame.image.load("assets/cell_texture1.png")
cell_texture1 = pygame.transform.scale(
    cell_texture1,
    (CELL_SIZE, CELL_SIZE)
)

cell_texture2 = pygame.image.load("assets/cell_texture2.png")
cell_texture2 = pygame.transform.scale(
    cell_texture2,
    (CELL_SIZE, CELL_SIZE)
)

cell_textures = [cell_texture1, cell_texture2]