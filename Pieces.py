import time


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
                possible_positions.append([self.pos[0], self.pos[1] + (1 if self.get_team() == "black" else -1)])
                if self.pos[1] == 1 or self.pos[1] == 6:
                    possible_positions.append([self.pos[0], self.pos[1] + (2 if self.get_team() == "black" else -2)])
            case "rook":
                print("===========================")
                for i in range(2):
                    val = True
                    for y in range(-8, 8):
                        second = self.pos[i] + y
                        if (8 > second >= 0) and (y != 0):
                            case = [self.pos[0], second] if i else [second, self.pos[1]]
                            if val:
                                possible_positions.append(case)
                            if self.board[case[0]][case[1]]:
                                if y < 0:
                                    val = True
                                else:
                                    break
                print(possible_positions)
        return possible_positions
