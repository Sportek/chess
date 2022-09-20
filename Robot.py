import random

from ChessPieces.CPieces import CPieces


class Robot:

    def __init__(self, board: list[list[CPieces]], team):
        self.board = board
        self.team = team

    # TODO return true if a piece can eat you
    def isSafe(self, coordonates):
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                if piece == "":
                    continue
                movements: list[int] = piece.getPossibleMovements(self.board)
                if coordonates in movements:
                    return False
        return True

    # def find_safe_place(self, piece: CPieces):
    #     moves = piece.getPossibleMovements(self.board)
    #     for move in moves:
    #         if not self.isSafe(move):

    # Trouver un moyen si jamais les pions sont attaqués (en soustrayants des points).
    def get_all_possible_movements(self):
        possibilities = []
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                # Check si la piece est de la bonne team
                if piece and piece.getTeam() == self.team:
                    possible_moves = piece.getPossibleMovements(self.board)
                    addValue = 0
                    # Regarder si la pièce peut actuellement se faire manger
                    if not self.isSafe([x, y]):
                        addValue += piece.getValue()

                    # Pour chacun des mouvements possibles de la pièce, on compte le nombre de points possibles.
                    for move in possible_moves:
                        value = 0
                        opponent = self.board[move[0]][move[1]]
                        if opponent:
                            value += opponent.getValue()

                        # Regarder si dans le prochain mouvement, c'est sécuritaire.
                        # Si non, soustraire la value de la piece
                        if not self.isSafe(move):
                            value -= piece.getValue()

                        possibilities.append([{"piece": [x, y], "place": move}, value])
        return possibilities

    def choose_movement(self):
        possibilities = self.get_all_possible_movements()
        possibilities.sort(key=lambda x: x[1], reverse=True)

        # Implémenter une touche de random
        new_possibilities = [possibilities[0]]
        for i in range(len(possibilities)):
            if len(possibilities) > (i + 1):
                if possibilities[i][1] == possibilities[i + 1][1]:
                    new_possibilities.append(possibilities[i + 1])
            break

        return random.choice(new_possibilities)
