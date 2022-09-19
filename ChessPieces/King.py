from ChessPieces.CPieces import CPieces


class King(CPieces):
    def __init__(self, coordonates, team):
        super().__init__(coordonates, team)
        super.value = 900
        super.name = "king"

