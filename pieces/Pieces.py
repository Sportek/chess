import Board


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
                if self.get_team() == "black":
                    possible_positions.append(self.pos)

        print("possible positions:", possible_positions)
        return possible_positions
