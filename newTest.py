import pytest
from Sprites import Player 
import os
import pygame
import Levels

def test_board_initialization():
    pygame.init()
    screen = pygame.display.set_mode([606, 606])
    FONTPATH = os.path.join(os.getcwd(), 'resources/font/ALGER.TTF')
    font = pygame.font.Font(FONTPATH, 18)
    for num_level in range(1, Levels.NUMLEVELS+1):
        if num_level == 1:
            level = Levels.Level1()
            screen.fill((0, 0, 0 ))
    BlinkyPATH = os.path.join(os.getcwd(), 'resources/images/Blinky.png')
    board = Player(287, 199,BlinkyPATH)
    direction=[0,2]
    board.is_move=True
    assert board.changeSpeed(direction) == [0,60]
    # assert board.size == 6
    # assert len(board.snakes) == 3
    # assert len(board.ladders) == 3