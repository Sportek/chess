from ChessPieces.CPieces import CPieces


class Pawn(CPieces):
    def __init__(self, coordonates, team):
        super().__init__(coordonates, team)
        self.value = 1
        self.name = "pawn"

    def getPossibleMovements(self, board: list[list[CPieces]]):
        possible_positions = []
        case = [self.coordonates[0], self.coordonates[1] + (1 if self.getTeam() == "black" else -1)]
        if (8 > case[0] >= 0) and (8 > case[1] >= 0):
            if board[case[0]][case[1]] == "":
                possible_positions.append(case)
        if self.coordonates[1] == (6 if self.getTeam() == "white" else 1):
            case = [self.coordonates[0], self.coordonates[1] + (2 if self.getTeam() == "black" else -2)]
            if board[case[0]][case[1]] == "":
                possible_positions.append(case)
        vals = [[-1, -1], [1, -1]] if self.getTeam() == "white" else [[1, 1], [-1, 1]]
        for i in vals:
            case = [self.coordonates[0] + i[0], self.coordonates[1] + i[1]]
            if (8 > case[0] >= 0) and (8 > case[1] >= 0):
                if board[case[0]][case[1]] != "" and board[case[0]][case[1]].getTeam() != self.getTeam() and board[case[0]][case[1]] != "":
                    possible_positions.append(case)
        return possible_positions
