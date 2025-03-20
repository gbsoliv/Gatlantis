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
        # Initialize the level with a window, level name, and player's score.
        self.timeout = 20000  # Set the timeout for the level.
        self.window = window  # The window in which the level is rendered.
        self.name = name  # The name of the level.
        self.entity_list: list[Entity] = []  # List to store all entities in the level.
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # Add background entities to the list.

        player = EntityFactory.get_entity('Player')  # Create the player entity.
        player.score = player_score[0]  # Assign the player's score.
        self.entity_list.append(player)  # Add the player to the entity list.

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # Timer for spawning enemies.
        pygame.time.set_timer(EVENT_TIMEOUT, millis=100)  # Timer for timeout events every 100ms.

    pass

    def run(self, player_score: list[int]):
        # Play background music for the level.
        pygame.mixer.music.load('./assets/level1-song.mp3')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()  # Use a clock to control the frame rate.

        while True:
            clock.tick(60)  # Limit the game to 60 frames per second.
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # Draw each entity on the screen.
                ent.move()  # Update the entity's position.

                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()  # Check if the entity can shoot.
                    if shoot is not None:
                        self.entity_list.append(shoot)  # Add the shot to the entity list.
                    if ent.name == 'Player':
                        # Display player's health and score on the screen.
                        self.level_text(18, f'HP: {ent.health} | Score: {ent.score}', COLOR_PURPLE, (10, 5))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Exit the game if the player closes the window.
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:  # Spawn enemies when the timer triggers.
                    self.entity_list.append(EntityFactory.get_entity('Enemy1'))
                    self.entity_list.append(EntityFactory.get_entity('Enemy2'))

                found_player = False
                for ent in self.entity_list:
                    # Check if the player is still alive and update the score.
                    if isinstance(ent, Player) and ent.name == 'Player':
                        player_score[0] = ent.score
                        found_player = True

                if not found_player:  # End the game if the player is not found.
                    return False

            # Handle collisions and update the health of all entities.
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            pygame.display.flip()  # Update the display with the latest changes.

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        # Render text and display it on the screen at a specific position.
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)  # Draw the text on the screen.
