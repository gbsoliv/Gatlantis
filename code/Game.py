#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.Level import Level
from code.Menu import Menu
from Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTIONS


class Game:
    # Main Game class responsible for initializing and running the game.
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        # Run the main game loop. Handles menu interaction and game states.

        while True:
            # Display the main menu and get the user selection.
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTIONS[0]:  # PLAY
                # Start the game level if the PLAY option is selected.
                player_score = [0]  # Initialize the player score.
                level = Level(self.window, 'Level1', player_score)
                level_return = level.run(player_score)

            # elif menu_return == MENU_OPTIONS[1]:                   # SCORE
            # Display the score if the SCORE option is selected.

            elif menu_return == MENU_OPTIONS[2]:  # QUIT
                # Exit the game if the QUIT option is selected.
                pygame.quit()  # Close the game window.
                quit()  # End the program.
            else:
                # Handle unexpected menu return values.
                pygame.quit()
                sys.exit()
