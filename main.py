import pygame
pygame.init()

from settings import WIDTH, HEIGHT, FPS
from settings import CELL_SIZE, ROWS, COLS, MINE_COUNT
from board import Board

window = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("assets/background.jpg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

from assets import cell_textures, numbers_textures, sign_texture, boom_texture, base_texture

clock = pygame.time.Clock()

board = Board(ROWS, COLS)

def get_board_offset():
    field_width = COLS * CELL_SIZE
    field_height = ROWS * CELL_SIZE
                           
    offset_x = (WIDTH - field_width) // 2
    offset_y = (HEIGHT - field_height) // 2
    return offset_x, offset_y

def handle_events():
    global play
    global game_state
    global loose_cell
    global first_left_click
    field_width = COLS * CELL_SIZE
    field_height = ROWS * CELL_SIZE
    offset_x, offset_y = get_board_offset()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if game_state == "menu":
                if start_button.collidepoint(mouse_x, mouse_y):
                    game_state = "playing"
                
            elif game_state == "playing" and (
                offset_x <= mouse_x < offset_x + field_width
                and
                offset_y <= mouse_y < offset_y + field_height
            ):
                col = (mouse_x - offset_x) // CELL_SIZE
                row = (mouse_y - offset_y) // CELL_SIZE

                if event.button == 1:
                    if first_left_click:
                        first_left_click = False
                        board.place_mines((row, col))
                    good_click = board.left_click(row, col)
                    if not good_click:
                        game_state = "game_over"
                        loose_cell = (row, col)
                    elif board.count_open == ROWS * COLS - MINE_COUNT:
                        game_state = "win"
                elif event.button == 3:
                    board.right_click(row, col)

def draw_boom():
    row, col = loose_cell
    offset_x, offset_y = get_board_offset()

    x = offset_x + col * CELL_SIZE
    y = offset_y + row * CELL_SIZE

    boom_rect = boom_texture.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
    window.blit(boom_texture, boom_rect)

def draw_game_over():
    window.blit(background, (0, 0))
    text = font.render("GAME OVER", True, (0, 33, 16))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(text, text_rect)

def draw_win():
    window.blit(background, (0, 0))
    text = font.render("WIN", True, (0, 33, 16))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(text, text_rect)

def draw_menu():
    text = font.render("Minesweeper", True, (0, 33, 16))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(text, text_rect)

    pygame.draw.rect(window, (100, 100, 100), start_button)

    text = button_font.render("PLAY", True, (255, 255, 255))
    text_rect = text.get_rect(center=start_button.center)

    window.blit(text, text_rect)

def draw_board():
    offset_x, offset_y = get_board_offset()

    base_rect = base_texture.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(base_texture, base_rect)

    for row in board.cells:
        for cell in row:
            x = offset_x + cell.col * CELL_SIZE
            y = offset_y + cell.row * CELL_SIZE

            if cell.is_open:
                texture = numbers_textures[cell.mine_count]
                window.blit(texture, (x, y))
            else:
                texture = cell_textures[cell.texture_id]
                window.blit(texture, (x, y))
                if cell.has_sign:
                    texture = sign_texture
                    window.blit(texture, (x, y))

    text = font.render(f"Mines: {board.remaining_mines}", True, (0, 33, 16))
    window.blit(text, (850, 10))

game_state = "menu"
start_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 150, 300, 70)
loose_cell = (0, 0)
play = True
first_left_click = True
font = pygame.font.Font("assets/fonts/Cinzel-Bold.ttf", 70)
button_font = pygame.font.Font("assets/fonts/Cinzel-Bold.ttf", 35)

while play:

    window.blit(background, (0, 0))
    
    handle_events()

    if game_state == "menu":
        draw_menu()

    elif game_state == "playing":
        draw_board()

    elif game_state == "game_over":
        draw_board()
        draw_boom()
        pygame.display.update()
        pygame.time.delay(1300)

        draw_game_over()
        pygame.display.update()
        pygame.time.delay(1000)

        play = False

    elif game_state == "win":
        draw_win()
        pygame.display.update()
        pygame.time.delay(1000)
        play = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()