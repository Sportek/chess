import sys
import time

import pygame

from Board import Board

pygame.init()

pygame.display.set_caption("Chess ⁕ by Sportek")
pygame.display.set_icon(pygame.image.load("images/black_king.png"))
board = Board(pygame)
board.replaceStringToObject()
board.draw_actual_board()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            board.click_event(pygame.mouse.get_pos())
    time.sleep(0.01)
    pygame.display.flip()
