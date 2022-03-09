import pygame
from Pieces import Piece
from Pawn import Pawn
from King import King
from PieceFactory import PieceFactory
class Square:
    def __init__(self, x, y, image,screen , board):
        self.x = x
        self.y = y
        self.image = image
        self. screen = screen
        self.piece = None
        self.selected = False
        self.board = board
        self.threatenedBy = []
    def drawSquare(self):
          self.screen.blit(self.image, (self.x,self.y))
          if self.piece:
              if self.piece.Type == "king" and self.piece.Check():
                  pygame.draw.rect(self.screen,(255,0,0),[self.x,self.y,100,100])
              self.piece.draw()
          if self.selected == True:
              pygame.draw.rect(self.screen,(0,255,255),[self.x,self.y,100,100],5)
    def addPiece(self,Type, color):
         self.piece = PieceFactory.makePiece(self,Type,color,self.board)
         return self.piece
    def Update(self, selectedPiece):
        mouse = pygame.mouse.get_pos()
        if self.x <= mouse[0] and mouse[0]<=self.x +100 and self.y <= mouse[1]and mouse[1]<=self.y +100:
            if self.selected == False:
                if selectedPiece and (not self.piece or self.piece.color != selectedPiece.color) and selectedPiece.isValidMove(self):
                    if self.board.whiteTurn and selectedPiece.color == "white":
                        selectedPiece.move(self)
                        self.board.checkmate()
                        if not self.board.promotingPiece:
                            self.board.blackTurn = True
                            self.board.whiteTurn = False
                    elif self.board.blackTurn and selectedPiece.color == "black" and self.board.AI == False:
                        selectedPiece.move(self)
                        self.board.checkmate()
                        if not self.board.promotingPiece:
                            self.board.whiteTurn = True
                            self.board.blackTurn = False
                    self.board.selected = None

                else:
                    self.selected = True
                    if self.piece:
                        self.piece.selected = True
            else:
                self.selected = False
                if self.piece:
                    self.piece.selected = False
                    self.board.selected = None
        else:
            self.selected = False
            if self.piece:
                self.piece.selected = False
    def Threatened(self,color):
        self.threatenedBy.clear()
        if color == "white":
            colorList = self.board.white
        if color == "black":
            colorList = self.board.black
        threatened = False

        for Piece in colorList:
            if Piece.isValidMove(self, True):
                threatened = True
                self.threatenedBy.append(Piece)
        return threatened
class Board:
    def __init__(self, screen):
        self.screen = screen
        self.board = []
        self.selected = None
        self.black = []
        self.white = []
        self.promotingPiece = None
        self.whiteTurn = True
        self.blackTurn = False
        self.whiteKing = None
        self.blackKing = None
        self.AI = False
        self.checkMate = None
        lightSquare = pygame.image.load("chess/square brown light_1x_ns.png")
        lightSquare = pygame.transform.scale(lightSquare,(100,100))
        darkSquare = pygame.image.load("chess/square brown dark_1x_ns.png")
        darkSquare = pygame.transform.scale(darkSquare,(100,100))
        lastSquare = darkSquare
        for x in range(8):
            if lastSquare == darkSquare :
                lastSquare = lightSquare
            else:
                 lastSquare = darkSquare
            column = []
            self.board.append(column)
            for y in range(8):
                if lastSquare == darkSquare :
                    lastSquare = lightSquare
                else :
                    lastSquare = darkSquare
                square = Square(x *100,y*100,lastSquare,screen,self)
                self.board[x].append(square)
    def drawBoard(self):
        for column in self.board:
            for square in column:
                square.drawSquare()
    def setupBoard(self):
        self.black.append(self.board[0][7].addPiece("rook","black"))
        self.black.append(self.board[1][7].addPiece("knight","black"))
        self.black.append(self.board[2][7].addPiece("bishop","black"))
        self.black.append(self.board[3][7].addPiece("queen","black"))
        self.blackKing = self.board[4][7].addPiece("king","black")
        self.black.append(self.blackKing)
        self.black.append(self.board[5][7].addPiece("bishop","black"))
        self.black.append(self.board[6][7].addPiece("knight","black"))
        self.black.append(self.board[7][7].addPiece("rook","black"))

        self.white.append(self.board[0][0].addPiece("rook","white"))
        self.white.append(self.board[1][0].addPiece("knight","white"))
        self.white.append(self.board[2][0].addPiece("bishop","white"))
        self.white.append(self.board[3][0].addPiece("queen","white"))
        self.whiteKing = self.board[4][0].addPiece("king","white")
        self.white.append(self.whiteKing)
        self.white.append(self.board[5][0].addPiece("bishop","white"))
        self.white.append(self.board[6][0].addPiece("knight","white"))
        self.white.append(self.board[7][0].addPiece("rook","white"))
        
        for i in range (8):
            self.black.append(self.board[i][6].addPiece("pawn","black"))
            self.white.append(self.board[i][1].addPiece("pawn","white"))
    def click(self):
        for column in self.board:
            for square in column:
                square.Update(self.selected)
                if square.selected:
                    self.selected = square.piece

    def predict(self, piece, square):
        board = self.makeCopy()
        startSquare = board.board[int(piece.square.x/100)][int(piece.square.y/100)]
        newPiece = startSquare.piece
        targetSquare = board.board[int(square.x/100)][int(square.y/100)]
        newPiece.move(targetSquare)
        return board

    def makeCopy(self):
        copyBoard = Board(self.screen)
        copyBoard.promotingPiece = self.promotingPiece
        copyBoard.whiteTurn = self.whiteTurn
        copyBoard.blackTurn = self.blackTurn
        for whitePiece in self.white:
            piece = copyBoard.board[int(whitePiece.square.x/100)][int(whitePiece.square.y/100)].addPiece(whitePiece.Type, whitePiece.color)
            copyBoard.white.append(piece)
            if piece.Type == "king":
                copyBoard.whiteKing = piece
        for blackPiece in self.black:
            piece = copyBoard.board[int(blackPiece.square.x / 100)][int(blackPiece.square.y / 100)].addPiece(blackPiece.Type, blackPiece.color)
            copyBoard.black.append(piece)
            if piece.Type == "king":
                copyBoard.blackKing = piece
        return copyBoard

    def checkmate(self):
        BC = False
        WC = False
        if self.blackKing.Check():
            BC = True
            for i in range(3):
                i2 = int(self.blackKing.square.x/100) + i - 1
                if i2 >= 0 and i2 <= 7:
                    for j in range(3):
                        j2 = int(self.blackKing.square.y/100) + j - 1
                        if j2 >= 0 and j2 <= 7:
                            square = self.board[i2][j2]
                            if self.blackKing.isValidMove(square):
                                BC = False

            for piece in self.black:
                if piece == self.blackKing:
                    continue
                if len(piece.getValidMoves()) > 0:
                    BC = False
                    break


            '''for Pieces in self.blackKing.square.threatenedBy:
                if Pieces.Type == "bishop" or Pieces.Type == "rook" or Pieces.Type == "queen":
                    otherX = int(Pieces.square.x/100)
                    otherY = int(Pieces.square.y/100)
                    x = int(self.blackKing.square.x/100)
                    y = int(self.blackKing.square.y/100)
                    while x != otherX or y != otherY:
                        if otherX > x:
                            x += 1
                        if otherX < x:
                            x -= 1
                        if otherY > y:
                            y += 1
                        if otherY < y:
                            y -= 1
                        for blackPiece in self.black:
                            square = self.board[x][y]
                            if blackPiece.isValidMove(square):
                                pass'''


        if self.whiteKing.Check():
            WC = True
            #print("--START WC--")
            for i in range(3):
                i2 = int(self.whiteKing.square.x/100) + i - 1
                if i2 >= 0 and i2 <= 7:
                    for j in range(3):
                        j2 = int(self.whiteKing.square.y/100) + j - 1
                        if j2 >= 0 and j2 <= 7:
                            square = self.board[i2][j2]
                            if self.whiteKing.isValidMove(square):
                                WC = False

            for piece in self.white:
                if piece == self.whiteKing:
                    continue
                if len(piece.getValidMoves()) > 0:
                    WC = False
                    break

        winner = None
        if WC:
            winner = "Black"
        if BC:
            winner = "White"
        self.checkMate = winner
        return winner

    def promote(self, type):
        self.promotingPiece.promote(type)
        self.promotingPiece = None
        self.blackTurn = not self.blackTurn
        self.whiteTurn = not self.whiteTurn

    def doNotBlit(self):
        for column in self.board:
            row = ""
            for square in column:
                if square.piece:
                    row += square.piece.Type[0]
                else:
                    row += "_"
            print(row)



                        
