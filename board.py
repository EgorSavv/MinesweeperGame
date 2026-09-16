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
        self.mine_positions = []

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
                texture_id = random.randrange(3)
                cell = Cell(row, col, texture_id)

                current_row.append(cell)

            self.cells.append(current_row)

    def place_mines(self):
        self.mine_positions = random.sample(self.get_all_cells(), MINE_COUNT)

        for row, col in self.mine_positions:
            cell = self.cells[row][col]
            cell.has_mine = True

    def calc_mine_count(self, row, col):
        count = 0

        for cur_row, cur_col in self.mine_positions:
            if abs(cur_row - row) <= 1 and abs(cur_col - col) <= 1:
                count += 1

        return count

    def left_click(self, row, col):
        cell = self.cells[row][col]

        if cell.is_open:
            return True

        if cell.has_sign:
            return True

        if cell.has_mine:
            return False

        cell.mine_count = self.calc_mine_count(row, col)
        cell.open()

        return True

    def right_click(self, row, col):
        cell = self.cells[row][col]

        if cell.has_sign:
            self.remaining_mines += 1
        else:
            self.remaining_mines -= 1

        cell.change_sign();
    