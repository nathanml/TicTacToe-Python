class Cell:
    def __init__(self,r,c):
        self.row = r
        self.col = c
        self.piece = None

    def __repr__(self):
        ret = ""
        if self.piece is not None:
            ret += " | " + repr(self.piece) + " |"
        else:
            ret += " |   |"
        return ret

    def __eq__(self, other):
        if other.isEmpty():
            return False
        else:
            return self.piece == other.piece

    def isEmpty(self):
        return self.piece is None

    def placepiece(self, p):
        self.piece = p
        p.place_piece(self.row, self.col)

    def getPiece(self):
        return self.piece
