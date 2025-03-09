#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from const import COLOR_BLACK, WIN_WIDTH, MENU_OPTIONS


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/Menu.png')
        self.rectangle = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./assets/menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rectangle)
            self.menu_text(70, "Gatlantis", COLOR_BLACK, (WIN_WIDTH / 2, 70))

            for i in range(len(MENU_OPTIONS)):
                self.menu_text(30, MENU_OPTIONS[i], COLOR_BLACK, (WIN_WIDTH / 2, 150 + 30 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple) -> None:
        text_font: Font = pygame.font.SysFont("Courier New", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
