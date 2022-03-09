import pygame
from Board import *
from Pieces import Piece
class Knight(Piece):
    def __init__(self, square,Type, color,board):
        if color == "black" :
            self.image = pygame.image.load("chess/b_knight_1x_ns.png")
        else :
            self.image = pygame.image.load("chess/w_knight_1x_ns.png")
        Piece.__init__(self,square,Type,color,board)
    def isValidMove(self ,Square,check = False):
        if not Piece.isValidMove(self,Square,check= check):
            return False
        x = self.square.x
        y = self.square.y
        if (abs(x-Square.x ) == 200 and  abs(y - Square.y) == 100)or(abs(x-Square.x ) == 100 and  abs(y - Square.y)== 200) :
            otherPiece = self.board.board[int(x/100)][int(y/100)].piece 
            if otherPiece and otherPiece != self:
                return False
            return True
        return False

    def checkMove(self, xmod, ymod):
        x = int(self.square.x / 100) + xmod
        y = int(self.square.y / 100) + ymod
        return x >= 0 and y <= 7  and x <= 7 and y >= 0 and self.isValidMove(self.board.board[x][y])

    def getValidMoves(self):
        validMoves = []
        x = int(self.square.x / 100)
        y = int(self.square.y / 100)
        if self.checkMove(-1, 2):
            validMoves.append(self.board.board[x - 1][y + 2])
        if self.checkMove(-1, -2):
            validMoves.append(self.board.board[x - 1][y - 2])
        if self.checkMove(1, 2):
            validMoves.append(self.board.board[x + 1][y + 2])
        if self.checkMove(1, -2):
            validMoves.append(self.board.board[x + 1][y - 2])
        if self.checkMove(2, 1):
            validMoves.append(self.board.board[x + 2][y + 1])
        if self.checkMove(2, -1):
            validMoves.append(self.board.board[x + 2][y - 1])
        if self.checkMove(-2, 1):
            validMoves.append(self.board.board[x - 2][y + 1])
        if self.checkMove(-2, -1):
            validMoves.append(self.board.board[x - 2][y - 1])
        return validMoves
