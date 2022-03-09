import pygame
from Board import *
from Pieces import Piece
class Rook(Piece):
    def __init__(self, square,Type, color,board):
        if color == "black" :
            self.image = pygame.image.load("chess/b_rook_1x_ns.png")
        else :
            self.image = pygame.image.load("chess/w_rook_1x_ns.png")
        Piece.__init__(self,square,Type,color,board)
    def isValidMove(self ,Square,check = False):
        if not Piece.isValidMove(self, Square, check = check):
            return False
        x = self.square.x
        y = self.square.y
        if abs(x-Square.x) != 0 and abs(y - Square.y) != 0:
            return False
        foundFirst = False
        while x != Square.x or y != Square.y:
            otherPiece = self.board.board[int(x/100)][int(y/100)].piece 
            if otherPiece and otherPiece != self:
                return False
            if x < Square.x:
                x += 100
            elif x > Square.x:
                x -= 100
            if y< Square.y:
                y += 100
            elif y > Square.y:
                y -=100
        return True
    
    def Castle(self):
        if self.square.x == 0:
            moveHere = self.board.board[3][int(self.square.y/100)]
        elif self.square.x == 700:
            moveHere = self.board.board[5][int(self.square.y/100)]
        self.move(moveHere)

    def getValidMoves(self):
        validMoves = []
        for i in range(8):
            rookSquare = self.board.board[i][int(self.square.y/100)]
            if self.isValidMove(rookSquare):
                validMoves.append(rookSquare)
            rookSquare = self.board.board[int(self.square.x/100)][i]
            if self.isValidMove(rookSquare):
                validMoves.append(rookSquare)
        return validMoves

