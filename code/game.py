#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.level import Level
from code.menu import Menu
from const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTIONS


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTIONS[0]:  # PLAY
                level = Level(self.window, 'Level1')                 #!!!!
                level_return = level.run()

            elif menu_return == MENU_OPTIONS[2]:  # QUIT
                pygame.quit()
                quit()
                pass

            else:
                pass
