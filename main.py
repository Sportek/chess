import sys
import time

import pygame

from Board import Board

pygame.init()

# ball = pygame.image.load("intro_ball.gif")
# king = pygame.image.load("images/king.png")
# ballrect = ball.get_rect().y =
# kingrect = king.get_rect().

board = Board(pygame).draw_actual_board()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            board.click_event(pygame.mouse.get_pos())

    time.sleep(0.01)

    pygame.display.flip()
