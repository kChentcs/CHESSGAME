import pygame
import random

class AI:
    def __init__(self, color, board, difficulty):
        self.color = color
        self.board = board
        self.difficulty = difficulty

    def makeMove(self):
        if self.color == "black":
            findPieces = self.board.black
        else:
            findPieces = self.board.white
        RandomMoveSquare = None
        randomPieceMoved = None

        while RandomMoveSquare == None:
            randomPieceMoved = findPieces[random.randint(0, len(findPieces) - 1)]
            print(randomPieceMoved.Type)
            AIRandomMoves = randomPieceMoved.getValidMoves()
            print(len(AIRandomMoves))
            if len(AIRandomMoves) >= 1:
                RandomMoveSquare = AIRandomMoves[random.randint(0, len(AIRandomMoves) -1)]
                print(RandomMoveSquare.x, RandomMoveSquare.y)

        randomPieceMoved.move(RandomMoveSquare)
        if self.board.promotingPiece:
            self.board.promote("queen")