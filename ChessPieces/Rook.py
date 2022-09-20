from ChessPieces.CPieces import CPieces


class Rook(CPieces):
    def __init__(self, coordonates, team):
        super().__init__(coordonates, team)
        self.value = 5
        self.name = "rook"

    def getPossibleMovements(self, board: list[list[CPieces]]):
        possible_positions = []
        for z in range(2):
            for y in range(1, 8, 1):
                value = (y if z else -y)
                second = self.coordonates[1] + value
                if 8 > second >= 0:
                    case = [self.coordonates[0], second]
                    if board[case[0]][case[1]] == "" or board[case[0]][case[1]].getTeam() != self.getTeam():
                        possible_positions.append(case)
                    if board[case[0]][case[1]]:
                        break
            for y in range(1, 8, 1):
                value = (y if z else -y)
                second = self.coordonates[0] + value
                if 8 > second >= 0:
                    case = [second, self.coordonates[1]]
                    if board[case[0]][case[1]] == "" or board[case[0]][case[1]].getTeam() != self.getTeam():
                        possible_positions.append(case)
                    if board[case[0]][case[1]]:
                        break
        return possible_positions
