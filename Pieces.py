class Pieces:
    def __init__(self, name, pos, board):
        self.name = name
        self.pos = pos
        self.board = board

    def get_type(self):
        return self.name.split("_")[1]

    def get_team(self):
        return self.name.split("_")[0]

    def get_possible_movement(self):
        possible_positions = []
        match self.get_type():
            case "pawn":
                case = [self.pos[0], self.pos[1] + (1 if self.get_team() == "black" else -1)]
                if self.board[case[0]][case[1]].split("_")[0] != self.get_team():
                    possible_positions.append(case)
                if (self.pos[1] == 1 and self.get_team() == "black") or (self.pos[1] == 6 and self.get_team() == "white"):
                    case = [self.pos[0], self.pos[1] + (2 if self.get_team() == "black" else -2)]
                    if self.board[case[0]][case[1]].split("_")[0] != self.get_team():
                        possible_positions.append(case)

            case "rook":
                for z in range(2):
                    for y in range(1, 8, 1):
                        value = (y if z else -y)
                        second = self.pos[1] + value
                        if 8 > second >= 0:
                            case = [self.pos[0], second]
                            if self.board[case[0]][case[1]].split("_")[0] != self.get_team():
                                possible_positions.append(case)
                            if self.board[case[0]][case[1]]:
                                break
                    for y in range(1, 8, 1):
                        value = (y if z else -y)
                        second = self.pos[0] + value
                        if 8 > second >= 0:
                            case = [second, self.pos[1]]
                            if self.board[case[0]][case[1]].split("_")[0] != self.get_team():
                                possible_positions.append(case)
                            if self.board[case[0]][case[1]]:
                                break
            case "knight":
                values = [[1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2]]
                for i in values:
                    case = [self.pos[0] + i[0], self.pos[1] + i[1]]
                    if (8 > case[0] >= 0) and (8 > case[1] >= 0):
                        if self.board[case[0]][case[1]].split("_")[0] != self.get_team():
                            possible_positions.append(case)
            case "bishop":
                stade = [[-1, -1], [1, 1], [-1, 1], [1, -1]]
                for z in range(4):
                    for value in range(1, 8, 1):
                        case = [self.pos[0] + stade[z][0] * value, self.pos[1] + stade[z][1] * value]
                        if (8 > case[0] >= 0) and (8 > case[1] >= 0):
                            if self.board[case[0]][case[1]].split("_")[0] != self.get_team():
                                possible_positions.append(case)
                            if self.board[case[0]][case[1]]:
                                break
            case "king":
                values = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
                for i in values:
                    case = [self.pos[0] + i[0], self.pos[1] + i[1]]
                    if (8 > case[0] >= 0) and (8 > case[1] >= 0):
                        if self.board[case[0]][case[1]].split("_")[0] != self.get_team():
                            possible_positions.append(case)
            case "queen":
                values = ["bishop", "rook"]
                for i in values:
                    self.name = self.get_team() + "_" + i
                    possible_positions.extend(self.get_possible_movement())
        return possible_positions
