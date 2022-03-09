import pygame
from Board import *
class Piece:
    def __init__(self, square, Type, color,board):
        self.square = square
        self.Type = Type
        self.color = color
        self.board = board
        self.selected = False
        self.image = pygame.transform.scale(self.image,(100,100))
        self.hasMoved = False
    def draw(self):
        self.square.screen.blit(self.image, (self.square.x,self.square.y))
    def move(self,square):
        if square.piece:
            if square.piece.color == "white":
                self.board.white.remove(square.piece)
            elif square.piece.color == "black":
                self.board.black.remove(square.piece)
        self.square.piece = None
        self.square = square
        self.square.piece = self
        self.hasMoved = True

    def isValidMove(self, Square, check = False):
        if self.square == Square:
            return False
        elif self.color == "black" and not check:
            newBoard = self.board.predict(self, Square)
            #newBoard.doNotBlit()
            if newBoard.blackKing.Check():
                return False
        elif self.color == "white" and not check:
            newBoard = self.board.predict(self, Square)
            #newBoard.doNotBlit()
            if newBoard.whiteKing.Check():
                return False
        #
        # elif self.color == "black":
        #     for Pieces in self.board.white:
        #         if Pieces.Type == "bishop" or Pieces.Type == "rook" or Pieces.Type == "queen":
        #             otherX = int(Pieces.square.x / 100)
        #             otherY = int(Pieces.square.y / 100)
        #             x = int(self.board.blackKing.square.x / 100)
        #             y = int(self.board.blackKing.square.y / 100)
        #             valid = True
        #             if Pieces.Type == "bishop" or Pieces.Type == "queen":
        #                 if abs(x - otherX) != abs(y - otherY):
        #                     valid = False
        #                 elif abs(x - self.square.x) != abs(y - self.square.y):
        #                     valid = False
        #                 elif abs(otherX - self.square.x) != abs(otherY - self.square.y):
        #                     valid = False
        #                 elif min(otherX, x) > (self.square.x) or max(otherX, x) < (self.square.x):
        #                     valid = False
        #                 elif min(otherY, y) > (self.square.y) or max(otherY, y) < (self.square.y):
        #                     valid = False
        #             if Pieces.Type == "rook" or Pieces.Type == "queen":
        #                 if x != otherX or x != self.square.x or otherX != self.square.x:
        #                     if (y) != abs(otherY) or abs(y) != abs(self.square.y) or abs(otherY) != abs(self.square.Y):
        #                         valid = False
        #                 elif x == otherX and min(otherY, y) > (self.square.y) or max(otherY, y) < (self.square.y):
        #                     valid = False
        #                 elif y == otherY and min(otherX, x) > (self.square.x) or max(otherX, x) < (self.square.x):
        #                     valid = False
        #             if valid == False:
        #                 continue
        #             print("Potential Pin: " + self.color + self.Type + ", " + Pieces.color + Pieces.Type)
        #             foundPiece = 0
        #             while x != otherX or y != otherY:
        #                 if otherX > x:
        #                     x += 1
        #                 if otherX < x:
        #                     x -= 1
        #                 if otherY > y:
        #                     y += 1
        #                 if otherY < y:
        #                     y -= 1
        #                 if self.board.board[x][y].piece:
        #                     foundPiece += 1
        #             if foundPiece == 1:
        #                 print("pieces is pinned")
        #                 return False

        if not check and Square.piece and Square.piece.color == self.color:
            #print("allied piece occupies square")
            return False
        if not check:
            #print("move is okay")
            pass
        return True

    def getValidMoves(self):
        validMoves = []
        for i in range(8):
            for j in range(8):
                square = self.board.board[i][j]
                if self.isValidMove(square):
                    validMoves.append(square)
        return validMoves


