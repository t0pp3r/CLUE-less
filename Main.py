from Constants import *
from GameController import *
from Components.Card import *
from Components.BoardPiece import *
from Components.Player import *
                
def getCharacterList():
        return NAMES.keys()
        
def getInitialCardDeck():
        cards = []
        for key in CARDS.keys():
                for label in CARDS[key]:
                        cards.append(Card(key,label))
        return cards

def getInitialBoardLayout():
        board = []
        rows = 5
        cols = 5
        
        # Initialize board layout
        row1 = [BoardPiece(STUDY,ROOM), BoardPiece(H3, HALLWAY), BoardPiece(HALL,ROOM), BoardPiece(H8,HALLWAY), BoardPiece(LOUNGE,ROOM)]
        board.append(row1)
        row2 = [BoardPiece(H1,HALLWAY), None, BoardPiece(H6,ROOM), None, BoardPiece(H11,ROOM)]
        board.append(row2)
        row3 = [BoardPiece(LIBRARY,ROOM), BoardPiece(H4, HALLWAY), BoardPiece(BILLIARD_ROOM,ROOM), BoardPiece(H9,HALLWAY), BoardPiece(DINING_ROOM,ROOM)]
        board.append(row3)
        row4 = [BoardPiece(H2,HALLWAY), None, BoardPiece(H7,ROOM), None, BoardPiece(H12,ROOM)]
        board.append(row4)
        row5 = [BoardPiece(CONSERVATORY,ROOM),BoardPiece(H5, HALLWAY),BoardPiece(BALLROOM,ROOM),BoardPiece(H10,HALLWAY),BoardPiece(KITCHEN,ROOM)]
        board.append(row5)
        
        # Initialize piece adjacency attributes
        for i in range(0,rows):
                for j in range(0,cols):
                        if board[i][j] == None:
                                #print "BREAK"
                                continue
                        #print "i: %d, j: %d" % (i,j)
                        if i == 0:
                                board[i][j].above = None
                                if board[i+1][j]:
                                        board[i][j].below = board[i+1][j].name
                                if j == 0:
                                        board[i][j].secret = board[rows-1][cols-1].name
                                elif j == cols - 1:
                                        board[i][j].secret = board[rows-1][0].name
                        elif i < rows - 1:
                                if board[i-1][j]:
                                        board[i][j].above = board[i-1][j].name
                                if board[i+1][j]:
                                        board[i][j].below = board[i+1][j].name
                        else:
                                if board[i-1][j]:
                                        board[i][j].above = board[i-1][j].name
                                board[i][j].below = None
                                if j == 0:
                                        board[i][j].secret = board[0][cols-1].name
                                elif j == cols - 1:
                                        board[i][j].secret = board[0][0].name
                        if j == 0:
                                board[i][j].left = None
                                if board[i][j+1]:
                                        board[i][j].right = board[i][j+1].name
                        elif j < cols - 1:
                                if board[i][j-1]:
                                        board[i][j].left = board[i][j-1].name
                                if board[i][j+1]:
                                        board[i][j].right = board[i][j+1].name
                        else:
                                if board[i][j-1]:
                                        board[i][j].left = board[i][j-1].name
                                board[i][j].right = None
                                        
        # Turn board into 1D list
        new_board = []
        for row in board:
                for piece in row:
                        if piece != None:
                                new_board.append(piece)

        # Add in starting spots
        new_board.append(BoardPiece(COLONEL_MUSTARD, START, left=H11))
        new_board.append(BoardPiece(MISS_SCARLET, START, below=H8))
        new_board.append(BoardPiece(PROFESSOR_PLUM, START, right=H1))
        new_board.append(BoardPiece(MR_GREEN, START, above=H5))
        new_board.append(BoardPiece(MRS_WHITE, START, above=H10))
        new_board.append(BoardPiece(MRS_PEACOCK, START, right=H2))

        # test
        for p in new_board:
                p.players = []

        #for b in new_board:
                #print "%s: %s" % (b.name, str(b.getAdjacentSpots()))
        return new_board
        
def main():
        cards = getInitialCardDeck()
        board = getInitialBoardLayout()
        players = []
        
        gameController = GameController(cards, board, players)
        print "Initialized GameController"
        print "Starting game!"
        gameController.startGame()
        print "Closing game"

if __name__ == "__main__":
        main()
