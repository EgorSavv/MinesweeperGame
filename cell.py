class Cell:
    def __init__(self, row, col, texture_id):
        self.row = row
        self.col = col

        self.texture_id = texture_id

        self.is_open = False
        self.has_mine = False
        self.mine_count = 0

        self.bonus_type = None
        self.bonus_lifetime = 0