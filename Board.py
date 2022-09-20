import pygame.transform
from pygame.rect import Rect

import Chess
from ChessPieces.Bishop import Bishop
from ChessPieces.CPieces import CPieces
from ChessPieces.King import King
from ChessPieces.Knight import Knight
from ChessPieces.Pawn import Pawn
from ChessPieces.Queen import Queen
from ChessPieces.Rook import Rook


def convert_coordinates_to_cases(pos):
    return [pos[0] // Chess.CUBE_SIZE, pos[1] // Chess.CUBE_SIZE]


class Board:
    def __init__(self, pygame):
        self.screen = None
        self.pygame = pygame
        self.board: list[list[CPieces]] | list[list[str]] = [
            ["black_rook", "black_pawn", "", "", "", "", "white_pawn", "white_rook"],
            ["black_knight", "black_pawn", "", "", "", "", "white_pawn", "white_knight"],
            ["black_bishop", "black_pawn", "", "", "", "", "white_pawn", "white_bishop"],
            ["black_queen", "black_pawn", "", "", "", "", "white_pawn", "white_queen"],
            ["black_king", "black_pawn", "", "", "", "", "white_pawn", "white_king"],
            ["black_bishop", "black_pawn", "", "", "", "", "white_pawn", "white_bishop"],
            ["black_knight", "black_pawn", "", "", "", "", "white_pawn", "white_knight"],
            ["black_rook", "black_pawn", "", "", "", "", "white_pawn", "white_rook"],
        ]
        self.selected = [None, None]
        self.possible_moves = []
        self.king_has_move = False
        self.black_rooks_has_move = [False, False]
        self.white_rooks_has_move = [False, False]
        self.promotion_screen = False
        self.promotion_choices = {}
        self.promotion_coordinates = None
        self.promotion_team = None
        self.turn = "white"

    def show_selector(self):
        cube = 75
        self.pygame.draw.rect(self.screen, (100, 100, 100),
                              Rect(0, (8 * Chess.CUBE_SIZE + 10 + 10 + cube) / 3 - 34, Chess.CUBE_SIZE * 8, 140))

        self.promotion_choices = {
            "queen": Rect(10 + cube * 0, (8 * Chess.CUBE_SIZE + 10 + 10 + cube) / 3, cube, cube).move(24 + 0 * 10, 0),
            "bishop": Rect(10 + cube * 1, (8 * Chess.CUBE_SIZE + 10 + 10 + cube) / 3, cube, cube).move(24 + 1 * 10, 0),
            "rook": Rect(10 + cube * 2, (8 * Chess.CUBE_SIZE + 10 + 10 + cube) / 3, cube, cube).move(24 + 2 * 10, 0),
            "knight": Rect(10 + cube * 3, (8 * Chess.CUBE_SIZE + 10 + 10 + cube) / 3, cube, cube).move(24 + 3 * 10, 0)}

        for key, value in self.promotion_choices.items():
            self.pygame.draw.rect(self.screen, (75, 75, 75), value)
            image = self.pygame.image.load("images/" + self.promotion_team + "_" + key + ".png")
            image = pygame.transform.scale(image, (cube, cube))
            self.screen.blit(image, value)

    def move_piece_to_location(self, now_pos, then_pos):
        self.board[then_pos[0]][then_pos[1]] = self.board[now_pos[0]][now_pos[1]]
        self.board[then_pos[0]][then_pos[1]].setCoordonates(then_pos)
        self.board[now_pos[0]][now_pos[1]] = ""
        self.turn = "black" if self.turn == "white" else "white"

    def draw_actual_board(self):
        pygame.display.set_caption(f"Chess ⁕ by Sportek | Turn to {self.turn}")

        size = width, height = Chess.CUBE_SIZE * 8, Chess.CUBE_SIZE * 8
        self.screen = self.pygame.display.set_mode(size)

        a = 0
        b = 0
        num = 0
        color = ""

        for x in range(8):
            a = a + b
            for y in range(8):
                num = num + 1
                if self.selected == [x, y]:
                    color = Chess.SELECTED_COLOR
                elif [x, y] in self.possible_moves:
                    color = Chess.POSSIBLE_CHOICE
                elif (a % 2) == 0:
                    color = Chess.WHITE_COLOR
                else:
                    color = Chess.BLACK_COLOR
                self.pygame.draw.rect(self.screen, color,
                                      Rect(x * Chess.CUBE_SIZE, y * Chess.CUBE_SIZE, Chess.CUBE_SIZE, Chess.CUBE_SIZE))

                if self.board[x][y]:
                    piece = self.pygame.image.load(f"images/{self.board[x][y].getFullName()}.png")
                    piece = pygame.transform.scale(piece, Chess.DEFAULT_IMAGE_SIZE)
                    piece_rect = Rect(x * Chess.CUBE_SIZE, y * Chess.CUBE_SIZE, piece.get_rect().width,
                                      piece.get_rect().height)
                    self.screen.blit(piece, piece_rect)

                a = a + 1
            a = 0
            b = b + 1
            if self.promotion_screen:
                self.show_selector()

    def replaceStringToObject(self):
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                if piece:
                    team = piece.split("_")[0]
                    piece_type = piece.split("_")[1]
                    match piece_type:
                        case "pawn":
                            self.board[x][y] = Pawn([x, y], team)
                        case "bishop":
                            self.board[x][y] = Bishop([x, y], team)
                        case "rook":
                            self.board[x][y] = Rook([x, y], team)
                        case "queen":
                            self.board[x][y] = Queen([x, y], team)
                        case "king":
                            self.board[x][y] = King([x, y], team)
                        case "knight":
                            self.board[x][y] = Knight([x, y], team)

    def check_if_promotion(self, case):
        piece = self.board[case[0]][case[1]]
        if piece.getTeam() == "pawn":
            if (piece.getTeam() == "white" and case[1] == 0) or (piece.getTeam() == "black" and case[1] == 7):
                self.promotion_coordinates = case
                self.promotion_team = piece.getTeam()
                self.promotion_screen = True

    def click_event(self, pos):
        if not self.promotion_screen:
            self.play_movement(pos)
        else:
            self.promotion_screen_click_event(pos)

    def promotion_screen_click_event(self, pos):
        val = ""
        for key, value in self.promotion_choices.items():
            if value.collidepoint(pos):
                val = key
                # break
        if val != "":
            self.board[self.promotion_coordinates[0]][self.promotion_coordinates[1]] = f"{self.promotion_team}_{val}"
            self.promotion_screen = False
            self.draw_actual_board()

    def play_movement(self, pos):
        case = convert_coordinates_to_cases(pos)
        piece_name = self.board[case[0]][case[1]]

        if piece_name:  # Do actions if user select a piece
            if self.selected != [] and (
                    case in self.possible_moves):  # If there was something selected and in the possible locations
                self.move_piece_to_location(self.selected, case)  # Eat
                self.check_if_promotion(case)
                self.selected = []
                self.possible_moves = []
            else:  # To change the selected case
                if piece_name.getTeam() == self.turn:
                    self.selected = case
                    self.possible_moves = piece_name.getPossibleMovements(self.board)

        else:  # Do actions if user select nothing
            if self.selected:  # If there was something selected
                if case in self.possible_moves:  # Move piece if user click in a possible locations
                    self.move_piece_to_location(self.selected, case)
                    self.check_if_promotion(case)
                #  Reset movements
                self.selected = []
                self.possible_moves = []
        self.draw_actual_board()
