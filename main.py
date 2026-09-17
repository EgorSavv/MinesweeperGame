import pygame
pygame.init()

from settings import WIDTH, HEIGHT, FPS
from settings import CELL_SIZE, ROWS, COLS
from board import Board

window = pygame.display.set_mode((WIDTH, HEIGHT))
from assets import cell_textures, numbers_textures, sign_texture, boom_texture

clock = pygame.time.Clock()

board = Board(ROWS, COLS)

def loose_game():
    global play
    global loose_pos
    x, y = loose_pos
    play = False
    window.blit(boom_texture, (x - 300, y - 300))
    print("Game Over!")

def win_game():
    global play
    play = False
    print("Win!")

def handle_events():
    global play
    global is_loose
    global loose_pos
    global first_left_click

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            col = mouse_x // (CELL_SIZE + 1)
            row = mouse_y // (CELL_SIZE + 1)

            if event.button == 1:
                if first_left_click:
                    first_left_click = False
                    board.place_mines((row, col))
                good_click = board.left_click(row, col)
                if not good_click:
                    is_loose = True
                    loose_pos = (mouse_x, mouse_y)
            elif event.button == 3:
                board.right_click(row, col)

def draw_board():
    global font

    for row in board.cells:
        for cell in row:
            x = cell.col * (CELL_SIZE + 1)
            y = cell.row * (CELL_SIZE + 1)

            if cell.is_open:
                texture = numbers_textures[cell.mine_count]
            elif cell.has_sign:
                texture = sign_texture
            else:
                texture = cell_textures[cell.texture_id]

            window.blit(texture, (x, y))

    text = font.render(f"Мины: {board.remaining_mines}", True, (255, 255, 255))
    window.blit(text, (850, 10))

is_loose = False
loose_pos = (0, 0)
play = True
first_left_click = True
font = pygame.font.Font(None, 50)

while play:

    window.fill((0, 0, 0))
    
    handle_events()

    draw_board()

    if len(board.unused_cells) == board.remaining_mines:
        win_game()
    if is_loose:
        loose_game()

    pygame.display.update()
    clock.tick(FPS)

    if not play:
        pygame.time.delay(1000)

pygame.quit()