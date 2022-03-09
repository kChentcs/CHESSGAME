import pygame
from Board import *
from Pieces import Piece
from Queen import Queen
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
class Pawn(Piece):
    def __init__(self, square,Type, color,board):
        if color == "black" :
            self.image = pygame.image.load("chess/b_pawn_1x_ns.png")
        else :
            self.image = pygame.image.load("chess/w_pawn_1x_ns.png")
        Piece.__init__(self,square,Type,color,board)
    def isValidMove(self ,Square,check = False):
        if not Piece.isValidMove(self,Square,check= check):
            return False
        if (Square.y - self.square.y == 100 and self.color == "white") or (Square.y - self.square.y== -100 and self.color == "black"):
            if abs(Square.x - self.square.x) == 0 and not Square.piece and not check:
                return True
            elif abs(Square.x - self.square.x) == 100 and (Square.piece or check):
                return True
            else:
                return False
        elif not check and not self.hasMoved and abs(Square.y - self.square.y) == 200 and (Square.x - self.square.x) == 0 and not Square.piece:
            middleSquare = self.board.board [int(self.square.x/100)][int((self.square.y + Square.y)/200)]
            return middleSquare.piece == None
        else:
            return False
    def promote(self, type):
        if type == "queen":
            piece = Queen(self.square, type,self.color,self.board)
        if type == "rook":
            piece = Rook(self.square, type,self.color,self.board)
        if type == "bishop":
            piece = Bishop(self.square, type,self.color,self.board)
        if type == "knight":
            piece = Knight(self.square, type,self.color,self.board)
        if self.color == "white":
            self.board.white.remove(self)
            self.board.white.append(piece)
            self.square.piece = piece
        elif self.color == "black":
            self.board.black.remove(self)
            self.board.black.append(piece)
            self.square.piece = piece
    def move(self,square):
        Piece.move(self,square)
        if (self.color == "white" and self.square.y == 700) or (self.color == "black" and self.square.y == 0):
            self.board.promotingPiece = self

    def getValidMoves(self):
        validMoves = []
        if self.color == "black":
            ymod = -1
        else:
            ymod = 1
        possibleMoves = []
        if int(self.square.y/100) + ymod >= 0 and int(self.square.y/100) + ymod <= 7:
            possibleMoves.append(self.board.board[int(self.square.x / 100)][int(self.square.y / 100) + ymod])
        if int(self.square.y / 100) + ymod *2 >= 0 and int(self.square.y / 100) + ymod *2 <= 7:
            possibleMoves.append(self.board.board[int(self.square.x / 100)][int(self.square.y / 100) + ymod *2])
        if self.square.x > 0:
            possibleMoves.append(self.board.board[int(self.square.x / 100) - 1][int(self.square.y / 100) + ymod])
        if self.square.x < 700:
            possibleMoves.append(self.board.board[int(self.square.x / 100) + 1][int(self.square.y / 100) + ymod])
        for goodMove in possibleMoves:
            if self.isValidMove(goodMove):
                validMoves.append(goodMove)

        return validMoves