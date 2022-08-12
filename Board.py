import pygame.transform
from pygame.rect import Rect

import Chess
from pieces.Pieces import Pieces


def convert_coordinates_to_cases(pos):
    return [pos[0] // Chess.CUBE_SIZE, pos[1] // Chess.CUBE_SIZE] # Todo to check


class Board:
    def __init__(self, pygame):
        self.pygame = pygame
        self.board = [
            ["black_rook", "black_knight", "black_bishop", "black_queen", "black_king", "black_bishop", "black_knight",
             "black_rook"],
            ["black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn",
             "black_pawn"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["white_pawn", "white_pawn", "white_pawn", "white_pawn", "white_pawn", "white_pawn", "white_pawn",
             "white_pawn"],
            ["white_rook", "white_knight", "white_bishop", "white_queen", "white_king", "white_bishop", "white_knight",
             "white_rook"]
        ]
        self.selected = [None, None]
        self.possible_moves = []

    def draw_actual_board(self):

        size = width, height = Chess.CUBE_SIZE * 8, Chess.CUBE_SIZE * 8
        screen = self.pygame.display.set_mode(size)

        a = 0
        b = 0
        num = 0
        color = "Blue"

        for y in range(8):
            a = a + b
            for x in range(8):
                num = num + 1
                if self.selected == [y, x]:
                    color = Chess.SELECTED_COLOR
                elif (a % 2) == 0:
                    color = Chess.WHITE_COLOR
                else:
                    color = Chess.BLACK_COLOR
                self.pygame.draw.rect(screen, color,
                                      Rect(x * Chess.CUBE_SIZE, y * Chess.CUBE_SIZE, Chess.CUBE_SIZE, Chess.CUBE_SIZE))

                if self.board[y][x]:
                    piece = self.pygame.image.load(f"images/{self.board[y][x]}.png")
                    piece = pygame.transform.scale(piece, Chess.DEFAULT_IMAGE_SIZE)
                    piece_rect = Rect(x * Chess.CUBE_SIZE, y * Chess.CUBE_SIZE, piece.get_rect().width,
                                      piece.get_rect().height)
                    screen.blit(piece, piece_rect)

                if self.possible_moves:
                    for i in self.possible_moves:
                        possible_move = self.pygame.draw.rect(screen, "BLUE",
                                                              Rect(i[0] * Chess.CUBE_SIZE, i[1] * Chess.CUBE_SIZE,
                                                                   Chess.CUBE_SIZE, Chess.CUBE_SIZE))

                a = a + 1
            a = 0
            b = b + 1

    def click_event(self, pos):
        case = convert_coordinates_to_cases(pos)
        print(case)

        piece_name = self.board[case[0]][case[1]]

        if piece_name:  # check if it's not empty
            self.selected = case
            self.possible_moves = Pieces(piece_name, convert_coordinates_to_cases(pos), self.board).get_possible_movement()
            self.draw_actual_board()
        else:
            if self.selected:
                piece_name = self.board[self.selected[0]][self.selected[1]]
                self.board[self.selected[0]][self.selected[1]] = ""
            self.selected = ""
            self.possible_moves = []
            self.draw_actual_board()
