#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from Const import COLOR_BLACK, WIN_WIDTH, MENU_OPTIONS, COLOR_GREEN


class Menu:
    def __init__(self, window):
        # Initialize the Menu object with the game window
        self.window = window
        # Load the background image for the menu
        self.surf = pygame.image.load('./assets/Menu.png').convert_alpha()
        # Set the initial position of the menu background
        self.rectangle = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        # Holds the current menu option being highlighted
        menu_option = 0

        # Load and play background music for the menu on loop
        pygame.mixer_music.load('./assets/menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            # Draw the menu background image
            self.window.blit(source=self.surf, dest=self.rectangle)
            # Render the game title text at the top
            self.menu_text(70, "Gatlantis", COLOR_BLACK, (WIN_WIDTH / 2, 70))

            # Draw menu options and highlight the currently selected one
            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    # Highlight the selected menu option in green
                    self.menu_text(30, MENU_OPTIONS[i], COLOR_GREEN, (WIN_WIDTH / 2, 150 + 30 * i))
                else:
                    # Render unselected menu options in black
                    self.menu_text(30, MENU_OPTIONS[i], COLOR_BLACK, (WIN_WIDTH / 2, 150 + 30 * i))

            # Update the display with the drawn elements
            pygame.display.flip()

            # Handle user inputs and system events
            for event in pygame.event.get():
                # Quit the application if the user closes the window
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()

                # Handle keyboard inputs for navigation and selection
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # Pressing DOWN key
                        # Move selection down or loop back to the top
                        if menu_option < len(MENU_OPTIONS) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # Pressing UP key
                        # Move selection up or loop back to the bottom
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1

                    if event.key == pygame.K_RETURN:  # Pressing ENTER key
                        # Return the currently selected menu option
                        return MENU_OPTIONS[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        # Render a given text centered at a specific position on the screen
        text_font: Font = pygame.font.SysFont("Courier New", text_size)  # Set the font and size
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # Render the text
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)  # Center the text at the desired position
        self.window.blit(text_surf, text_rect)  # Draw the text on the game window
