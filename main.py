import sys

import pygame
import time

from pygame.rect import Rect

from Board import Board

pygame.init()

# ball = pygame.image.load("intro_ball.gif")
# king = pygame.image.load("images/king.png")
# ballrect = ball.get_rect().y =
# kingrect = king.get_rect().

Board(pygame).draw_actual_board()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            Board.click_event(Board, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    time.sleep(0.01)

    pygame.display.flip()
