import numpy
import uuid

def transform_to_sparse(coords, i):
    return coords[0]*i-1+coords[1]

class QPlayer:
    def __init__(self, name):
        self.uuid = uuid.uuid1()
        self.name = name
        self.pos_x = 0
        self.pos_y = 0
        self.color = None
    def getId(self):
        return self.uuid
    def getName(self):
        return self.name
    def getColor(self):
        return self.color
    def getCoords(self):
        return tuple(self.pos_x, self.pos_y)
    def move(self, pos):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
    def setColor(self, color):
        self.color = color


class QWall:
    """
        :param north_west: (int,int) leftmost corner where wall should be placed
        :param orient: Defining if walls is to be place horizontally or vertically
    """
    def __init__(self, north_west, orient):
        assert orient.lower() == "v" or orient.lower() == "h" #Move all the check for correct input to where to before object creation
        self.south_east = tuple(north_west.x, north_west.y) if orient.lower() == v else tuple(north_west.x+1, north_west.y)
        self.north_west = north_west
        self.orient = orient
    """
        :returns: tuple of tuple of (x,y) coordinates of oposite ends of the wall 
    """
    def getCoords(self):
        return tuple(self.north_west, self.south_east)
    def getOrient(self):
        return self.orient

class QMove:
    def __init__(self, q_string):
        self.q_string = q_string
    def isWallPlace(self):
        return False
    def isPlayerMove(self):
        return False

class QMoveWall(QMove):
    def __init__(self, q_string):
        QMove.__init__(q_string)
        self.wall = QWall(tuple(0,0), "h") #TODO Parse into wall movement and orientation
    def isWallPlace(self):
        return True
    def isPlayerMove(self):
        return False
    def getWall(self):
        return self.wall
class QMovePlayer(QMove):
    def __init__(self, q_string):
        QMove.__init__(q_string)
        self.coords = tuple(0,0) #TODO Parse q_string into coords
        self.color = 0 #TODO Parse q_string into color
    def isWallPlace(self):
        return False
    def isPLayerMove(self):
        return True
    def getQPlayerColor(self):
        return self.color
    def getTo(self):
        return self.coords_to

class QuoridorGame:
    def __init__(self, i, j):
        self.turn_time = 15
        self.i = i
        self.j = j
        self.board = numpy.zeroes(i*i,j*j)
        self.players = []
        self.walls = []
        self.color_turn = "w"
        self.last_move = None
        self.running = False

    def populateBoard(self):
        for x in range(0, i):
            for y in range(0, j):
                if(x - 1 >= 0):
                    self.connect(tuple(x,y), tuple(x-1,y)) 
                if(x + 1 < self.i):
                    self.connect(tuple(x,y), tuple(x+1,y))
                if(y - 1 >= 0):
                    self.connect(tuple(x,y), tuple(x,y-1))
                if(y + 1 < self.j)
                    self.connect(tuple(x,y), tuple(x,y-1))
    
    def addPlayer(self, qplayer):
        assert len(players) < 2

        if(len(players) == 1):
            qplayer.color = "w" if players[0].color == "b" else "b"
        else
            qplayer.color = "w"

        players.append(qplayer)


    def startGame(self):
        self.running = True
        while(running):
            inpt = input("Move: ")
            if(inpt == "exit"):
                break

    def endGame(self):
        self.running = False

    def isConnected(self, coords1, coords2):
        return self.board[transform_to_sparse(coords1)][transform_to_sparse(coords2)]
    def connect(self, coords1, coords2):
        self.board[transform_to_sparse(coords1)][transform_to_sparse(coords2)] = 1
    def disconnect(self, coords1, coords2):
        self.board[transform_to_sparse(coords1)][transform_to_sparse(coords2)] = 0

    def getState(self):
        return self.board
    def getQPlayerById(self, q_id):
        return self.players[0] if self.players[0].getId() == q_id else players[1]

    def movePlayer(q_id, new_pos):
        t_player = getQPlayerById(q_id)
        t_player.move(new_pos)
        updateBoard()
        if(isDone()):
            endGame()
    def addWall(q_wall):
        self.walls.append(q_wall)
        updateBoard()
    
    def isDone():
        return players[0].coords[1] = i-1 or players[1].coords[1] = 0
   
    def validPlayerMove(q_str_move):
       a = 1 #TODO Validate player move / wall place and delegate to correct method


    def updateBoard():
        a = 1 #Get last move and update accordingly    

