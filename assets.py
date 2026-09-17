import pygame
from settings import CELL_SIZE, COLS, ROWS

spritesheet = pygame.image.load("assets/Sprites2.png").convert_alpha()

cell_textures = [
    spritesheet.subsurface((43 * 0, 43 * 0, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((43 * 1, 43 * 0, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((43 * 2, 43 * 0, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((43 * 3, 43 * 0, CELL_SIZE, CELL_SIZE)),
]

sign_texture = spritesheet.subsurface((43 * 0, 43 * 2, CELL_SIZE, CELL_SIZE)).convert_alpha()

numbers_textures = [
    spritesheet.subsurface((43 * 0, 43 * 1, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((43 * 1, 43 * 1, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((43 * 2, 43 * 1, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((43 * 3, 43 * 1, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((43 * 4, 43 * 1, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((43 * 5, 43 * 1, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((43 * 6, 43 * 1, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((43 * 7, 43 * 1, CELL_SIZE, CELL_SIZE)),
    spritesheet.subsurface((43 * 8, 43 * 1, CELL_SIZE, CELL_SIZE))
]

boom_texture = pygame.image.load("assets/boom.png").convert_alpha()

base_texture = pygame.image.load("assets/green.jpg")
base_texture = pygame.transform.scale(base_texture, (COLS * CELL_SIZE + 50, ROWS * CELL_SIZE + 50))