#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from Const import ENTITY_SPEED, ENTITY_SHOT_DELAY


# Represents an enemy entity and its behaviors.
class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        """
        Initializes the enemy with a name and starting position.
        """
        super().__init__(name, position)
        # Time delay between the enemy's shots, based on the entity name.
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        """
        Moves the enemy horizontally (left) on the screen based on its speed.
        """
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        """
        Makes the enemy shoot, creating an EnemyShot if the delay timer reaches 0.
        Resets the shot delay after firing.
        """
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
