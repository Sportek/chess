from ChessPieces.CPieces import CPieces


class Knight(CPieces):
    def __init__(self, coordonates, team):
        super().__init__(coordonates, team)
        self.value = 3
        self.name = "knight"

    def getPossibleMovements(self, board: list[list[CPieces]]):
        possible_positions = []
        values = [[1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]
        for i in values:
            case = [self.coordonates[0] + i[0], self.coordonates[1] + i[1]]
            if (8 > case[0] >= 0) and (8 > case[1] >= 0):
                if board[case[0]][case[1]] == "" or board[case[0]][case[1]].getTeam() != self.getTeam():
                    possible_positions.append(case)
        return possible_positions
