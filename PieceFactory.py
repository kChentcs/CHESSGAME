from Pawn import Pawn
from Pieces import Piece
from Bishop import Bishop
from Rook import Rook
from King import King
from Queen import Queen
from Knight import Knight
class PieceFactory:
    def makePiece(square,Type,color,board):
        if Type == "pawn":
            return Pawn(square,Type,color,board)
        elif Type == "bishop":
            return Bishop(square,Type,color, board)
        elif Type == "rook":
            return Rook(square,Type,color, board)
        elif Type == "knight":
            return Knight(square,Type,color, board)
        elif Type == "king":
            return King(square,Type,color, board)
        elif Type == "queen":
            return Queen(square,Type,color, board)
        
        else:
            return Piece(square,Type,color,board)
