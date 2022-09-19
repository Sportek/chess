from ChessPieces.CPieces import CPieces


class Pawn(CPieces):
    def __init__(self, coordonates, team):
        super().__init__(coordonates, team)
        super.value = 1
        super.name = "pawn"
