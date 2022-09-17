class CPieces:
    def __init__(self, coordonates, team):
        self.value = None
        self.coordonates = coordonates
        self.moved = False
        self.name = None
        self.team = team

    def setCoordonates(self, coordonates):
        self.coordonates = coordonates

    def getCoordonates(self):
        return self.coordonates

    def getFullName(self):
        return self.team + "_" + self.name

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def hasMoved(self):
        return self.moved

    def setMoved(self, boolean):
        self.moved = boolean

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
