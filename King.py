import pygame
from Board import *
from Pieces import Piece
class King(Piece):
    def __init__(self, square,Type, color,board):
        self.rook = None
        self.castling = False
        if color == "black" :
            self.image = pygame.image.load("chess/b_king_1x_ns.png")
        else :
            self.image = pygame.image.load("chess/w_king_1x_ns.png")
        Piece.__init__(self,square,Type,color,board)
    def isValidMove(self ,Square, check = False):
        if not Piece.isValidMove(self, Square, check = check):
            #print("15")
            return False
        if not check:
            if self.color == "white" and Square.Threatened("black"):
                #print("18")
                return False
            if self.color == "black" and Square.Threatened("white"):
                #print("18")
                return False
        if abs(Square.y - self.square.y) <= 100 and abs(Square.x - self.square.x) <= 100:
            #print("24")
            return True
        elif abs(self.square.x - Square.x) == 200 and abs(Square.y- self.square.y) == 0 and not check:
            #print("27")
            if not self.hasMoved:
                if self.square.x >  Square.x :
                    self.rook = self.board.board[0][int(self.square.y/100)].piece
                    if self.rook and self.rook.Type == "rook" and self.rook.color == self.color:
                        self.castling =  not self.board.board[1][int(self.square.y/100)].piece and not self.board.board[2][int(self.square.y/100)].piece and not self.board.board[3][int(self.square.y/100)].piece
                        return self.castling
                if self.square.x < Square.x :
                    self.rook = self.board.board[7][int(self.square.y/100)].piece
                    if self.rook and self.rook.Type == "rook" and self.rook.color == self.color:
                        self.castling = not self.board.board[5][int(self.square.y/100)].piece and not self.board.board[6][int(self.square.y/100)].piece
                        return self.castling
        else:
            #print("40")
            return False
    def move(self,square):
        Piece.move(self,square)
        if self.castling:
            self.rook.Castle()
            self.rook = None
            self.castling = False

    def Check(self):
        if self.color == "white":
            return self.square.Threatened("black")
        if self.color == "black":
            return self.square.Threatened("white")

    def getValidMoves(self):
        validMoves = []
        for i in range(3):
            i2 = int(self.square.x / 100) + i - 1
            if i2 >= 0 and i2 <= 7:
                for j in range(3):
                    j2 = int(self.square.y / 100) + j - 1
                    if j2 >= 0 and j2 <= 7:
                        square = self.board.board[i2][j2]
                        if self.isValidMove(square):
                            validMoves.append(square)
        if self.hasMoved == False :
            square = self.board.board[int(self.square.x/100) - 2][int(self.square.y/100)]
            if self.isValidMove(square):
                validMoves.append(square)
            square = self.board.board[int(self.square.x / 100)  + 2][int(self.square.y / 100)]
            if self.isValidMove(square):
                validMoves.append(square)

        return validMoves

        
