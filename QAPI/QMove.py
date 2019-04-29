class QMove:
    def __init__(self, q_string:str):
        self.q_string:str = q_string
        self.color:Color = q_string[0]
    def getQPlayerColor(self)->Color:
        return self.color
    def isWallPlace(self)->bool:
        return False
    def isPlayerMove(self)->bool:
        return False

class QMoveWall(QMove):
    def __init__(self, q_string:str):
        QMove.__init__(q_string)
        self.wall = QWall(tuple(0,0), "h") #TODO Parse into wall movement and orientation
    def isWallPlace(self)->bool:
        return True
    def isPlayerMove(self)->bool:
        return False
    def getWall(self):
        return self.wall

class QMovePlayer(QMove):
    def __init__(self, q_string:str):
        QMove.__init__(q_string)
        self.coords_to:SparsePoint = tuple(0,0) #TODO Parse q_string into coords
        self.color:Color = 0 #TODO Parse q_string into color
        self.walls_remaining:int = 10
    def getCountWalls(self)->int:
        return self.walls_remaining
    def isWallPlace(self)->bool:
        return False
    def isPLayerMove(self)->bool:
        return True
    def getQPlayerColor(self)->Color:
        return self.color
    def getTo(self)->SparsePoint:
        return self.coords_to


