from Cell import Cell


class Board:
    def __init__(self,r,c):
        self.rows = r
        self.cols = c
        self.cells = [[Cell(row,col) for row in range(self.rows)] for col in range(self.cols)]

    def __repr__(self):
        ret = "------------------\n"
        for row in range(self.rows):
            for col in range(self.cols):
                ret += repr(self.tileAt(row,col))
            ret += "\n"
        ret += "------------------"
        return ret

    def tileAt(self,row,col):
        return self.cells[row][col]

    def isFull(self):
        ret = True
        for row in range(self.rows):
            for col in range(self.cols):
                if self.cells[row][col].isEmpty():
                    ret = False
        return ret

    def place_piece(self, piece, r,c):
        tile = self.tileAt(r,c)
        if tile.isEmpty():
            tile.placepiece(piece)
        else:
            print("There is already a piece there")

    #def printBoard(self):
    def isValid(self, r,c):
        if (r < 0 or r > 2 or c < 0 or c > 2):
            return False
        if self.tileAt(r,c).isEmpty():
            return True
        else:
            return False
