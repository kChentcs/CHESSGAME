import pygame
from Board import Board
from textButton import textButton
from ImageButton import ImageButton
from AI import AI
pygame.init()
smallFont = pygame.font.Font("Fonts/Cinzel-VariableFont_wght.ttf", 20)
mediumFont = pygame.font.Font("Fonts/Cinzel-VariableFont_wght.ttf", 60)
largeFont = pygame.font.Font("Fonts/Cinzel-VariableFont_wght.ttf", 120)

state = "replay"
screenX = 800
screenY = 800
screen = pygame.display.set_mode((screenX, screenY))
board = Board(screen)
AIplayer = False

done = False

def switchState(newState, AIgame = False):
    global state, board, ArtificialIntelligence, AIplayer
    state = newState
    if state == "game":
        board = Board(screen)
        board.setupBoard()
        AIplayer = AIgame
        if AIgame:
            ArtificialIntelligence = AI("black", board, "Easy")
            board.AI = True

board.setupBoard()

ArtificialIntelligence = None

startButton = textButton(lambda : switchState("playerChoose"), screen, "Play", screenX/2 - 100, screenY/2 - 50, 200, 100, mediumFont)
AIButton = textButton(lambda : switchState("AIDifficulty"), screen, "1 player", screenX/3 -100, screenY/2, 200, 100, smallFont)
ChooseHumanButton = textButton(lambda : switchState("game", False), screen, "2 players", screenX/3 -100 + 300, screenY/2, 200, 100, smallFont)
EasyAI = textButton(lambda : switchState("game", True), screen, "Easy", screenX/2 - 125, screenY/3, 250, 100, smallFont)
MediumAI = textButton(lambda : switchState("game", True), screen, "Medium", screenX/2 - 125, screenY/2, 250, 100, smallFont)
HardAI = textButton(lambda : switchState("game", True), screen, "Hard", screenX/2 - 125, screenY * 2/3, 250, 100, smallFont)
playAgainButton = textButton(lambda : switchState("playerChoose"), screen, "Play again", screenX/3 - 100, screenY/2, 200, 100, smallFont)
endButton = textButton(quit, screen, "End game?", screenX/3 -100 + 400, screenY/2, 200, 100, smallFont)
KnightButton = ImageButton(lambda : board.promote("knight"), screen, "chess/w_knight_1x_ns.png", screenX/2 - 50, screenY/2 - 200, 100, 100)
BishopButton = ImageButton(lambda : board.promote("bishop"), screen, "chess/w_bishop_1x_ns.png", screenX/2 - 50, screenY/2 - 100, 100, 100)
RookButton = ImageButton(lambda : board.promote("rook"), screen, "chess/w_rook_1x_ns.png", screenX/2 - 50, screenY/2 , 100, 100)
QueenButton = ImageButton(lambda : board.promote("queen"), screen, "chess/w_queen_1x_ns.png", screenX/2 - 50, screenY/2 + 100, 100, 100)
mouseUp = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and mouseUp:
            mouseUp = False
            if state == "replay":
                startButton.handleEvent(event)
            elif state == "playerChoose":
                AIButton.handleEvent(event)
                ChooseHumanButton.handleEvent(event)
            elif state == "AIDifficulty":
                EasyAI.handleEvent(event)
                MediumAI.handleEvent(event)
                HardAI.handleEvent(event)
            elif state == "game":
                if board.promotingPiece:
                    KnightButton.handleEvent(event)
                    BishopButton.handleEvent(event)
                    RookButton.handleEvent(event)
                    QueenButton.handleEvent(event)
                else:
                    board.click()

            elif state == "play again":
                playAgainButton.handleEvent(event)
                endButton.handleEvent(event)
        if event.type == pygame.MOUSEBUTTONUP:
            mouseUp = True
        if event.type == pygame.QUIT:
            done = True
    if state == "replay":
        screen.fill((0, 0, 0))
        titleText = largeFont.render("Chess", True, (255, 255, 255))
        textRect = titleText.get_rect()
        textRect.center = (screenX / 2, screenY/ 5)
        screen.blit(titleText, textRect)
        startButton.update()
    if state == "playerChoose":
        screen.fill((0, 0, 0))
        titleText = largeFont.render("Chess", True, (255, 255, 255))
        textRect = titleText.get_rect()
        textRect.center = (screenX / 2, screenY / 5)
        screen.blit(titleText, textRect)
        ChooseHumanButton.update()
        AIButton.update()
    if state == "AIDifficulty":
        screen.fill((0, 0, 0))
        titleText = mediumFont.render("Chess", True, (255, 255, 255))
        textRect = titleText.get_rect()
        textRect.center = (screenX / 2, screenY / 5)
        screen.blit(titleText, textRect)
        EasyAI.update()
        MediumAI.update()
        HardAI.update()
    if state == "game":
        board.drawBoard()
        if board.promotingPiece:
            if board.promotingPiece.color == "white":
                KnightButton.changeImage("chess/w_knight_1x_ns.png")
                BishopButton.changeImage("chess/w_bishop_1x_ns.png")
                RookButton.changeImage("chess/w_rook_1x_ns.png")
                QueenButton.changeImage("chess/w_queen_1x_ns.png")
            else:
                KnightButton.changeImage("chess/b_knight_1x_ns.png")
                BishopButton.changeImage("chess/b_bishop_1x_ns.png")
                RookButton.changeImage("chess/b_rook_1x_ns.png")
                QueenButton.changeImage("chess/b_queen_1x_ns.png")
            KnightButton.update()
            BishopButton.update()
            RookButton.update()
            QueenButton.update()
        if board.blackTurn == True and AIplayer:
            if board.checkMate:
                state = "play again"
                continue
            ArtificialIntelligence.makeMove()
            board.whiteTurn = True
            board.blackTurn = False
        if board.checkMate:
            state = "play again"
    if state == "play again":
        screen.fill((0, 0, 0))
        titleText = mediumFont.render(board.checkmate() + " wins!", True, (255, 255, 255))
        textRect = titleText.get_rect()
        textRect.center = (screenX / 2, screenY / 5)
        screen.blit(titleText, textRect)
        playAgainButton.update()
        endButton.update()
    pygame.display.update()
pygame.quit()

