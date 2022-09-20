from ChessPieces.Bishop import Bishop
from ChessPieces.CPieces import CPieces
from ChessPieces.Rook import Rook


class Queen(CPieces):
    def __init__(self, coordonates, team):
        super().__init__(coordonates, team)
        self.value = 9
        self.name = "queen"

    def getPossibleMovements(self, board: list[list[CPieces]]):
        possible_positions = []
        values = [Bishop(self.coordonates, self.team), Rook(self.coordonates, self.team)]
        for i in values:
            possible_positions.extend(i.getPossibleMovements(board))
        return possible_positions
