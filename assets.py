import pygame
from settings import CELL_SIZE

spritesheet = pygame.image.load("assets/sprites.png").convert_alpha()

cell_textures = [
    spritesheet.subsurface((19 + 96 * 4, 21 + 96 * 2, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((19 + 96 * 5, 21 + 96 * 1, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((19 + 96 * 6, 21 + 96 * 1, CELL_SIZE, CELL_SIZE)),
]

sign_texture = spritesheet.subsurface((19 + 96 * 5, 21 + 96 * 2, CELL_SIZE, CELL_SIZE))

numbers_textures = [
    spritesheet.subsurface((19 + 96 * 5, 21 + 96 * 0, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((19 + 96 * 2, 21 + 96 * 6, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((19 + 96 * 3, 21 + 96 * 6, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((19 + 96 * 4, 21 + 96 * 6, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((19 + 96 * 3, 21 + 96 * 7, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((19 + 96 * 4, 21 + 96 * 7, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((19 + 96 * 2, 21 + 96 * 8, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((19 + 96 * 3, 21 + 96 * 8, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((19 + 96 * 4, 21 + 96 * 8, CELL_SIZE, CELL_SIZE))
]