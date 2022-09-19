from ChessPieces.CPieces import CPieces


class Queen(CPieces):
    def __init__(self, coordonates, team):
        super().__init__(coordonates, team)
        super.value = 9
        super.name = "queen"
