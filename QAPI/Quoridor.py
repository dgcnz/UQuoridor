import numpy
import uuid
import re
from typing import NewType, Tuple

Color = NewType("Color", str)
Orient = NewType("Orient", str)
SparsePoint = NewType("SparsePoint", tuple)
SparseCoords = NewType("SparseCoords", tuple)

#Coords = tuple(x, y)
#i = board size i

def transform_to_sparse(coords:SparsePoint, i:int):
    return coords[0]*i-1+coords[1]

class QPlayer:
    def __init__(self, name:str):
        self.uuid = uuid.uuid1()
        self.name:str = name
        self.pos_x:int = 0
        self.pos_y:int = 0
        self.color:Color = None
    def getId(self):
        return self.uuid

    def getName(self)->str:
        return self.name

    def getColor(self)->str:
        return self.color

    def getCoords(self)->SparsePoint:
        return tuple(self.pos_x, self.pos_y)

    def move(self, pos:SparsePoint):
        self.pos_x:int = pos[0]
        self.pos_y:int = pos[1]
    def setColor(self, color:Color):
        self.color:Color = color


class QWall:
    def __init__(self, north_west, orient):
        assert orient.lower() == "v" or orient.lower() == "h" #Move all the check for correct input to where to before object creation
        self.south_east = tuple(north_west.x, north_west.y) if orient.lower() == v else tuple(north_west.x+1, north_west.y)
        self.north_west = north_west
        self.orient:Orient = orient
    def getCoords(self)->tuple:
        return tuple(self.north_west, self.south_east)
    def getOrient(self)->Orient:
        return self.orient

class QuoridorGame:
    def __init__(self, i:int, j:int):
        self.turn_time:int = 15
        self.i:int = i
        self.j:int = j
        self.board = numpy.zeroes(i*i,j*j)
        self.players:list = []
        self.walls:list = []
        self.color_turn:Color = "w"
        self.last_move = None
        self.running:bool = False

    def populateBoard(self):
        for x in range(0, i):
            for y in range(0, j):
                if(x - 1 >= 0):
                    self.connect(tuple(x,y), tuple(x-1,y))
                if(x + 1 < self.i):
                    self.connect(tuple(x,y), tuple(x+1,y))
                if(y - 1 >= 0):
                    self.connect(tuple(x,y), tuple(x,y-1))
                if(y + 1 < self.j):
                    self.connect(tuple(x,y), tuple(x,y-1))

    def addPlayer(self, qplayer):
        assert len(players) < 2

        if(len(players) == 1):
            qplayer.color = "w" if players[0].color == "b" else "b"
        else:
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

    def isConnected(self, coords1:SparsePoint, coords2:SparsePoint)->bool:
        return self.board[transform_to_sparse(coords1)][transform_to_sparse(coords2)]

    def connect(self, coords1:SparsePoint, coords2:SparsePoint):
        self.board[transform_to_sparse(coords1)][transform_to_sparse(coords2)] = 1

    def disconnect(self, coords1:SparsePoint, coords2:SparsePoint):
        self.board[transform_to_sparse(coords1)][transform_to_sparse(coords2)] = 0

    #TODO FIXXX
    def parse_string(self, qstr:str, i:int, j:int):
        parser = re.compile("^(?:w|b)(([a-i][1-9])|([a-i][1-9](v|h)))$")
        while(True):
            ipt =str(input(""))
            m = parser.match(ipt)
            print(m.group())

    def getState(self):
        return self.board
    def getQPlayerById(self, q_id):
        return self.players[0] if self.players[0].getId() == q_id else players[1]
    def getQPlayerByColor(self, color:Color):
        return self.players[0] if self.players[0].getColor() == color else player[1]

    def movePlayer(self, q_id, q_pmove)->bool:
        if not validMove(q_pmove):
            return False
        q_player = getQPlayerById(q_id)
        updateBoard(q_pmove)
        q_player.move(q_pmove.getCoords())
        if(isDone()):
            endGame()
        return True

    def placeWall(self, q_id, q_wmove)->bool:
        if not validMove(q_wmove) :
            return False

        self.walls.append(q_wmove.getWall())
        q_player = getQPlayerById(q_id)
        updateBoard()
        return True

    def isDone(self)->bool:
        return players[0].coords[1] == i-1 or players[1].coords[1] == 0

    def validMove(self, q_move)->bool:
        return validWallPlace(q_move) if q_move.isWallPlace() else validPlayerMove(q_move)

    def validWallPlace(self, q_wmove)->bool:
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
                if w.orient == "h":
                    if nw == w.getCoords[0] and se == tuple(se[0], se[1]-1):
                            return False
                if w.orient == "v":
                    if nw == w.getCoords[0] == and tuple(se[0]+1, se[1]):
                            return False
            #Check to make sure there's still a path to the goal
            #TODO Implement A* or something else
            return True


    def validPlayerMove(self, q_pmove)->bool:
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
        if not isConnected(q_player.getCoords(), tuple(x,y) :
                return False
        return True

    def updateBoard(self, last_p_move):
        if self.last_move == None:
            return

        #Update move on wall move

        if self.last_move.isWallPlace():
            #TODO Update move when wall is placed
            a = 1

        #Update board on player move
        else:
            x,y = last_p_move.getCoords()
            p_x, p_y, = self.getPlayerByColor(last_p_move.getPlayerColor()).getCoords()

            #Check sparse matrix for all positions pointing to the last place and updates
            #TODO Check for walls
            if(p_x > 0):
                self.board[transform_to_sparse(tuple(x,y), self.i)][transform_to_sparse(tuple(p_x-1, p_y), self.i)] = 1
            if(p_x < self.i-1):
                self.board[transform_to_sparse(tuple(x,y), self.i)][transform_to_sparse(tuple(p_x+1, p_y), self.i)] = 1
            if(p_y > 0):
                self.board[transform_to_sparse(tuple(x,y), self.i)][transform_to_sparse(tuple(p_x, p_y-1), self.i)] = 1
            if(p_y < self.j-1):
                self.board[transform_to_sparse(tuple(x,y), self.i)][transform_to_sparse(tuple(p_x, p_y+1), self.i)] = 1
                """
            for w in self.walls: #TODO Write conditions for checking a wall when a ove is made
                if(p_x > 0):
                    if( (w.north_west[0] == p_x - 1 and w.north_west[1] == p_y) or w.north_west[
                """



