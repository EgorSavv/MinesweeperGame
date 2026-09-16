class Cell:
    def __init__(self, row, col, texture_id):
        self.row = row
        self.col = col

        self.texture_id = texture_id

        self.is_open = False
        self.has_mine = False
        self.has_sign = False
        self.mine_count = 0

        self.bonus_type = None
        self.bonus_lifetime = 0

    def open(self):
        self.is_open = True

    def change_sign(self):
        self.has_sign = not self.has_sign