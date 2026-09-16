import random
from cell import Cell

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.cells = []
        for row in range(rows):
            current_row = []

            for col in range(cols):
                texture_id = random.randrange(2)
                cell = Cell(row, col, texture_id)
                current_row.append(cell)

            self.cells.append(current_row)