import pygame.transform
from pygame.rect import Rect

import Chess
from Pieces import Pieces


def convert_coordinates_to_cases(pos):
    return [pos[0] // Chess.CUBE_SIZE, pos[1] // Chess.CUBE_SIZE]


class Board:
    def __init__(self, pygame):
        self.pygame = pygame
        self.board = [
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

    def move_piece_to_location(self, now_pos, then_pos):
        self.board[then_pos[0]][then_pos[1]] = self.board[now_pos[0]][now_pos[1]]
        self.board[now_pos[0]][now_pos[1]] = ""

    def draw_actual_board(self):

        size = width, height = Chess.CUBE_SIZE * 8, Chess.CUBE_SIZE * 8
        screen = self.pygame.display.set_mode(size)

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
                self.pygame.draw.rect(screen, color,
                                      Rect(x * Chess.CUBE_SIZE, y * Chess.CUBE_SIZE, Chess.CUBE_SIZE, Chess.CUBE_SIZE))

                if self.board[x][y]:
                    piece = self.pygame.image.load(f"images/{self.board[x][y]}.png")
                    piece = pygame.transform.scale(piece, Chess.DEFAULT_IMAGE_SIZE)
                    piece_rect = Rect(x * Chess.CUBE_SIZE, y * Chess.CUBE_SIZE, piece.get_rect().width,
                                      piece.get_rect().height)
                    screen.blit(piece, piece_rect)

                a = a + 1
            a = 0
            b = b + 1

    def click_event(self, pos):
        case = convert_coordinates_to_cases(pos)
        piece_name = self.board[case[0]][case[1]]

        if piece_name:  # Do actions if user select a piece
            if self.selected != [] and (
                    case in self.possible_moves):  # If there was something selected and in the possible locations
                self.move_piece_to_location(self.selected, case)
                self.selected = []
                self.possible_moves = []
            else:  # To change the selected case
                self.selected = case
                self.possible_moves = Pieces(piece_name, convert_coordinates_to_cases(pos),
                                             self.board).get_possible_movement()

        else:  # Do actions if user select nothing
            if self.selected:  # If there was something selected
                if case in self.possible_moves:  # Move piece if user click in a possible locations
                    self.move_piece_to_location(self.selected, case)
                #  Reset movements
                self.selected = []
                self.possible_moves = []
        self.draw_actual_board()
