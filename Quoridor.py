import numpy


i = 9
j = 9

def transform_to_sparse(coords):
    return coords[0]*8+coords[1]

class QuoridorGame:
    def __init__(self):
        self.turn_time = 15 #In seconds
        self.board = numpy.zeroes(i*i,j*j)
        self.players = [tuple(0,4), tuple(8,4)]
        #Pos is in the form (x,y)
        #Starting positions are in the middle at oposite sites of the board
        self.walls = dict() #Contains tuple(Edge, Edge) where Edge = pair<int, int>
   
    def isConnected(self, coords1, coords2):
        return self.board[transform_to_sparse(coords1)][transform_to_sparse(coords2)]
   
    def connect(self, coords1, coords2):
        self.board[transform_to_sparse(coords1)][transform_to_sparse(coords2)] = 1
   
    def getState():
        return self.board

    def movePlayer(player_num, new_pos):
        self.players[player_num] = new_pos
        updateBoard()
        if(isDone())
            #Send done message
    def isDone()
        return players[0][0] = 8 or players[1][0] = 0
   
   def updateBoard():
        #Update positions for players and walls


