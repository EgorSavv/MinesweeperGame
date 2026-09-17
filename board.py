import random
from cell import Cell
from settings import MINE_COUNT
from collections import deque

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.remaining_mines = MINE_COUNT
        self.cells = []
        self.unopened_cells = self.get_all_cells()
        self.mine_positions = []

        self.create_cells()

    def get_all_cells(self):
        all_positions = set()
                
        for row in range(self.rows):
            for col in range(self.cols):
                all_positions.add((row, col))

        return all_positions
    
    def get_available_cells(self, bad_cell):
        good_positions = []
        bad_row, bad_col = bad_cell
                
        for row in range(self.rows):
            for col in range(self.cols):
                if abs(bad_row - row) <= 1 and abs(bad_col - col) <= 1:
                    continue
                good_positions.append((row, col))

        return good_positions

    def create_cells(self):
        for row in range(self.rows):
            current_row = []

            for col in range(self.cols):
                texture_id = random.randrange(3)
                cell = Cell(row, col, texture_id)

                current_row.append(cell)

            self.cells.append(current_row)

    def place_mines(self, bad_cell):

        self.mine_positions = random.sample(self.get_available_cells(bad_cell), MINE_COUNT)

        for row, col in self.mine_positions:
            cell = self.cells[row][col]
            cell.has_mine = True

    def calc_mine_count(self, row, col):
        count = 0

        for cur_row, cur_col in self.mine_positions:
            if abs(cur_row - row) <= 1 and abs(cur_col - col) <= 1:
                count += 1

        return count

    def open_area(self, row, col):
        queue = deque()
        self.unopened_cells.remove((row, col))
        queue.append((row, col))

        while queue:
            cur_row, cur_col = queue.popleft()

            cell = self.cells[cur_row][cur_col]
            cell.mine_count = self.calc_mine_count(cur_row, cur_col)
            cell.open()

            if cell.mine_count == 0:
                needs_to_be_removed = []

                for next_row, next_col in self.unopened_cells:
                    if abs(next_row - cur_row) <= 1 and abs(next_col - cur_col) <= 1:
                        needs_to_be_removed.append((next_row, next_col))
                        queue.append((next_row, next_col))

                for rem_row, rem_col in needs_to_be_removed:
                    self.unopened_cells.remove((rem_row, rem_col))


    def left_click(self, row, col):
        cell = self.cells[row][col]

        if cell.is_open:
            return True

        if cell.has_sign:
            return True

        if cell.has_mine:
            return False

        self.open_area(row, col)

        return True

    def right_click(self, row, col):
        cell = self.cells[row][col]

        if cell.has_sign:
            self.remaining_mines += 1
        else:
            self.remaining_mines -= 1

        cell.change_sign();
    