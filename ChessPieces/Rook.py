from ChessPieces.CPieces import CPieces


class Rook(CPieces):
    def __init__(self, coordonates, team):
        super().__init__(coordonates, team)
        super.value = 5
        super.name = "rook"
