class Piece:
    def __init__(self, input):
        self.val = "" + input
        self.row = -1
        self.col = -1

    def __repr__(self):
        return self.val

    def __eq__(self, other):
        return self.val == other

    def place_piece(self, r,c):
        self.row = r
        self.col = c

    def getVal(self):
        return self.val