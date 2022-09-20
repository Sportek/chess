from ChessPieces.CPieces import CPieces


class King(CPieces):
    def __init__(self, coordonates, team):
        super().__init__(coordonates, team)
        self.value = 900
        self.name = "king"

    def getPossibleMovements(self, board: list[list[CPieces]]):
        possible_positions = []
        values = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
        for i in values:
            case = [self.coordonates[0] + i[0], self.coordonates[1] + i[1]]
            if (8 > case[0] >= 0) and (8 > case[1] >= 0):
                if board[case[0]][case[1]] == "" or board[case[0]][case[1]].getTeam() != self.getTeam():
                    possible_positions.append(case)
        return possible_positions
