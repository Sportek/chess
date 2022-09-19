from ChessPieces.CPieces import CPieces


class Knight(CPieces):
    def __init__(self, coordonates, team):
        super().__init__(coordonates, team)
        super.value = 3
        super.name = "knight"
