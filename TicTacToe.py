from Player import Player
from Board import Board

class TicTacToe:
    def __init__(self):
        print("Welcome to Tic Tac Toe!")
        self.players = [None, None]
        self.current = 0
        self.board = Board(3,3)
        self.generatePlayers()
        self.isOver = False

    def __repr__(self):
        print("Tic Tac Toe")
        print("Player X:")
        repr(self.players[0])
        print("Player Y: ")
        repr(self.players[1])
        repr(self.board)

    def generatePlayers(self):
        name = input("Player X, enter your name: ")
        playerX = Player(name, 'X')
        self.players[0] = playerX
        name = input("Player Y, enter your name: ")
        playerY = Player(name, 'Y')
        self.players[1] = playerY

    def restart(self):
        self.board = Board(3,3)
        self.isOver = False
        self.playGame()

    def playGame(self):
        while not self.isOver:
            print(self.board)
            if self.board.isFull():
                print("Tie game!")
                self.isOver = True
            else:
                print(self.players[self.current].getName() + ", your turn.")
                self.players[self.current].move(self.board)
                if self.players[self.current].isWinner(self.board):
                    print("Congratulations " + self.players[self.current].getName())
                    self.players[self.current].addWin()
                    self.isOver = True
                else:
                    if self.current == 0:
                        self.current = 1
                    else:
                        self.current = 0

        #When round is over, prompt user to keep playing
        for player in self.players:
            print(player)
        inp = input("Would you like to play another round? [Y/N]")
        while inp != "Y" and inp != "y" and inp != "N" and inp != "n":
            inp = input("Would you like to play another round? [Y/N]")
        if inp == "Y" or inp == "y":
            self.restart()
        else:
            for player in self.players:
                print(player)
            print("Goodbye")
            exit()






