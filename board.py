import random
from cell import Cell
from settings import MINE_COUNT

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.remaining_mines = MINE_COUNT
        self.cells = []
        self.unopened_cells = self.get_all_cells()

        self.create_cells()

        self.place_mines()

    def get_all_cells(self):
        all_positions = []
                
        for row in range(self.rows):
            for col in range(self.cols):
                all_positions.append((row, col))

        return all_positions

    def create_cells(self):
        for row in range(self.rows):
            current_row = []

            for col in range(self.cols):
                texture_id = random.randrange(2)
                cell = Cell(row, col, texture_id)

                current_row.append(cell)

            self.cells.append(current_row)

    def place_mines(self):
        mine_positions = random.sample(self.get_all_cells(), MINE_COUNT)

        for row, col in mine_positions:
            cell = self.cells[row][col]
            cell.has_mine = True

    def left_click(self, row, col):
        cell = self.cells[row][col]

        if cell.is_open:
            return

        if self.has_sign:
            return

        if self.has_mine:
            return False
        else:
            cell.open()

    def right_click(self, row, col):
        cell = self.cells[row][col]

        if self.has_sign:
            self.remaining_mines += 1
        else:
            self.remaining_mines -= 1

        cell.change_sign();
    