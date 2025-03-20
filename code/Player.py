#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.PlayerShot import PlayerShot
from code.Entity import Entity
from Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_SHOOT, \
    ENTITY_SHOT_DELAY


class Player(Entity):
    # Player class represents the playable character, inheriting common behavior from the Entity class.
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Delay between player shots.

    def move(self, ):
        # Handles the player's movement in response to keyboard inputs.
        pressed_key = pygame.key.get_pressed()

        # Move the player up if UP key is pressed and not at the window's top edge.
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        # Move the player down if DOWN key is pressed and not at the window's bottom edge.
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        # Move the player left if LEFT key is pressed and not at the window's left edge.
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        # Move the player right if RIGHT key is pressed and not at the window's right edge.
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shoot(self):
        # Handles the player's shooting mechanism with a configurable delay.
        self.shot_delay -= 1  # Decrease shot delay.

        # Check if the shot delay has reached zero.
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Reset shot delay.

            pressed_key = pygame.key.get_pressed()  # Detect pressed keys.

            # Shoot if the player's shoot key is pressed.
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                # Create and return a new PlayerShot instance positioned at the player's current location.
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
