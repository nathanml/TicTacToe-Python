from Piece import Piece


class Player:
    def __init__(self, n, v):
        self.name = n
        self.piece = Piece(v)
        self.numWins = 0

    def __repr__(self):
        ret = self.name + ": \n"
        ret += "Piece: " + str(self.piece.getVal()) + "\n"
        ret += "Wins: " + str(self.numWins)
        return ret

    def getName(self):
        return self.name

    def addWin(self):
        self.numWins+=1

    def isWinner(self, board):
        ret = True
        for i in range(3):
            if (board.tileAt(i, 0) == board.tileAt(i, 1) == board.tileAt(i, 2) or
                    board.tileAt(0, i) == board.tileAt(1, i) == board.tileAt(2, i)):
                return True
            elif board.tileAt(i, i) != board.tileAt(1, 1):
                ret = False
            elif board.tileAt(i, 2 - i) != board.tileAt(1, 1):
                ret = False
        return ret

    def move(self, board):
        r = int(input("Enter your row [0,1,2]: "))
        c = int(input("Enter your column [0,1,2]: "))
        while not board.isValid(r,c):
            print("Not a valid tile")
            r = int(input("Enter your row: "))
            c = int(input("Enter your column: "))
        board.place_piece(self.piece, r,c)
