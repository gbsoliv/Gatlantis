#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.EntityMediator import EntityMediator
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player
from Const import EVENT_TIMEOUT, EVENT_ENEMY, SPAWN_TIME, COLOR_PURPLE


class Level:

    def __init__(self, window: Surface, name: str, player_score: list[int]):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

        player = EntityFactory.get_entity('Player')
        player.score = player_score[0]
        self.entity_list.append(player)

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, millis=100)  # 100ms

    pass

    def run(self, player_score: list[int]):
        pygame.mixer.music.load('./assets/level1-song.mp3')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                    if ent.name == 'Player':
                        self.level_text(18, f'HP: {ent.health} | Score: {ent.score}', COLOR_PURPLE, (10, 5))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy1'))
                    self.entity_list.append(EntityFactory.get_entity('Enemy2'))

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player) and ent.name == 'Player':
                        player_score[0] = ent.score
                        found_player = True

                if not found_player:
                    return False

            # printed text
            # self.level_text(16, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_BLACK, (10, 5))
            # self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            # self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # COLLISION
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
