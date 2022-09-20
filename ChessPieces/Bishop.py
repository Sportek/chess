from ChessPieces.CPieces import CPieces


class Bishop(CPieces):
    def __init__(self, coordonates, team):
        super().__init__(coordonates, team)
        self.value = 3
        self.name = "bishop"

    def getPossibleMovements(self, board: list[list[CPieces]]):
        possible_positions = []
        stade = [[-1, -1], [1, 1], [-1, 1], [1, -1]]
        for z in range(4):
            for value in range(1, 8, 1):
                case = [self.coordonates[0] + stade[z][0] * value, self.coordonates[1] + stade[z][1] * value]
                if (8 > case[0] >= 0) and (8 > case[1] >= 0):
                    if board[case[0]][case[1]] == "" or board[case[0]][case[1]].getTeam() != self.getTeam():
                        possible_positions.append(case)
                    if board[case[0]][case[1]]:
                        break
        return possible_positions
