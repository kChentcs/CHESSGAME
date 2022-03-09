import pygame
from Board import *
from Pieces import Piece
class Bishop(Piece):
    def __init__(self, square,Type, color,board):
        if color == "black" :
            self.image = pygame.image.load("chess/b_bishop_1x_ns.png")
        else :
            self.image = pygame.image.load("chess/w_bishop_1x_ns.png")
        Piece.__init__(self,square,Type,color,board)
    def isValidMove(self ,Square,check = False):
        if not Piece.isValidMove(self,Square,check= check):
            return False
        x = self.square.x
        y = self.square.y
        if abs(x-Square.x) != abs(y - Square.y):
            return False
        while x != Square.x and y != Square.y:
            otherPiece = self.board.board[int(x/100)][int(y/100)].piece 
            if otherPiece and otherPiece != self:
                return False
            if x < Square.x:
                x += 100
            else:
                x -= 100
            if y < Square.y:
                y += 100
            else:
                y -=100
        return True

    def getValidMoves(self):
        validMoves = []
        x = int(self.square.x/100)
        y = int(self.square.y/100)
        n = min(x, y)
        for i in range(1, n + 1):
            targetSquare = self.board.board[x - n][y - n]
            if self.isValidMove(targetSquare):
                validMoves.append(targetSquare)
        n = min(x, 7 - y)
        for i in range(1, n + 1):
            targetSquare = self.board.board[x - n][y + n]
            if self.isValidMove(targetSquare):
                validMoves.append(targetSquare)
        n = min(7-x, y)
        for i in range(1, n + 1):
            targetSquare = self.board.board[x + n][y - n]
            if self.isValidMove(targetSquare):
                validMoves.append(targetSquare)

        n = min(7 - x, 7- y)
        for i in range(1, n + 1):
            targetSquare = self.board.board[x + n][y + n]
            if self.isValidMove(targetSquare):
                validMoves.append(targetSquare)

        return validMoves


    
