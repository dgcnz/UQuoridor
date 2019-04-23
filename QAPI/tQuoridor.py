import numpy
import uuid
import re
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
    def __init__(self, north_west, orient):
        assert orient.lower() == "v" or orient.lower() == "h" #Move all the check for correct input to where to before object creation
        self.south_east = tuple(north_west.x, north_west.y) if orient.lower() == v else tuple(north_west.x+1, north_west.y)
        self.north_west = north_west
        self.orient = orient
    def getCoords(self):
        return tuple(self.north_west, self.south_east)
    def getOrient(self):
        return self.orient

class QMove:
    def __init__(self, q_string):
        self.q_string = q_string
        self.color = 0 #TODO Parse qstring
    def getQPlayerColor(self):
        return self.color
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
        self.coords_to = tuple(0,0) #TODO Parse q_string into coords
        self.color = 0 #TODO Parse q_string into color
        self.walls_remaining = 10
    def getCountWalls(self):
        return self.walls_remaining
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

    def parse_string(qstr, i, j):
        parser = re.compile("^(?:w|b)(([a-i][1-9])|([a-i][1-9](v|h)))$")
        while(True):
            ipt =str(input(""))
            m = parser.match(ipt)
            print m.group()
    
    def getState(self):
        return self.board
    def getQPlayerById(self, q_id):
        return self.players[0] if self.players[0].getId() == q_id else players[1]
    def getQPlayerByColor(self, color):
        return self.players[0] if self.players[0].getColor() == color else player[1]

    def movePlayer(q_id, q_pmove):
        if(!validMove(q_pmove)):
            return False
        q_player = getQPlayerById(q_id)
        updateBoard(q_pmove)
        q_player.move(q_pmove.getCoords())
        if(isDone()):
            endGame()
        return True

    def placeWall(q_id, q_wmove):
        if(!validMove(q_wmove)):
            return False

        self.walls.append(q_wmove.getWall())
        q_player = getQPlayerById(q_id)
        updateBoard()
        return True

    def isDone():
        return players[0].coords[1] = i-1 or players[1].coords[1] = 0
   
    def validMove(q_move):
        return validWallPlace(q_move) if q_move.isWallPlace() else validPlayerMove(q_move)

    def validWallPlace(q_wmove):
            wall_t = q_wmove.getWall()
            nw,se = wall_t.getCoords()
            ori = wall_t.getOrient()

            #Check to make sure it's within bounds
            if(nw[0] < 0 or se[0] < 0 or nw[1] > i-1 or se[1] > j-1):
                return False

            #Check for making sure it's not place on top of other wall
            for w in self.walls:
                if w.orient == ori and nw == w.getCoords()[0] and se.getCoords()[1] == se:
                    return False
                if w.orient = "h":
                    if nw == w.getCoords[0] and se == tuple(se[0], se[1]-1):
                            return False
                if w.orient = "v":
                    if nw == w.getCoords()[0] == and tuple(se[0]+1, se[1]):
                            return False
            #Check to make sure there's still a path to the goal
            #TODO Implement A* or something else
            return True


    def validPlayerMove(q_pmove):
       if(q_pmove.getPlayerColor() != self.color_turn):
           return False
       q_player = getQPlayerByColor(q_pmove.getPlayerColor())
       x,y = qp_move.getTo();

       #Make sure the move request is in the bound of the board and it's not the same position
       if(x > 0 and x >= self.i):
           return False
       if(y < 0 or y >= self.j):
           return False
       if(x == q_player.getCoords()[0] and y == q_player.getCoords()[1]):
           return False
        if(!isConnected(q_player.getCoords(), tuple(x,y)):
                return False
        return True

    def updateBoard(last_p_move):
        if self.last_move == None:
            return

        if self.last_move.isWallPlace():
            a = 1
        else:
            x,y = last_p_move.getCoords();
            p_x, p_y, = self.getPlayerByColor(last_p_move.getPlayerColor())

            for j in range(0, self.j*self.j):
                pos_to_update = self.board[transform_to_sparse(tuple(p_x,p_y), self.i)][j]
        


