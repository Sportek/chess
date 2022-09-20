from ChessPieces.CPieces import CPieces


class Robot:

    def __init__(self, board: list[list[CPieces]], team):
        self.board = board
        self.team = team

    # TODO return true if a piece can eat you
    def can_they_eat_me(self, coordonates):
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                if piece == "":
                    continue
                movements: list[int] = piece.getPossibleMovements(self.board)
                if coordonates in movements:
                    return True
        return False

# Trouver un moyen si jamais les pions sont attaqués (en soustrayants des points).
    def get_all_possible_movements(self):
        possibilities = []
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                if piece and piece.getTeam() == self.team:
                    possible_moves = piece.getPossibleMovements(self.board)
                    for move in possible_moves:
                        value = 0
                        against_piece = self.board[move[0]][move[1]]
                        if against_piece == "":
                            value = 0.25
                        else:
                            value += against_piece.getValue()
                        if self.can_they_eat_me([move[0], move[1]]):
                            value -= piece.getValue()
                        possibilities.append([[[x, y], move], value])
        return possibilities

    def choose_movement(self):
        possibilities = self.get_all_possible_movements()
        possibilities.sort(key=lambda x: x[1], reverse=True)
        return possibilities[0][0]
