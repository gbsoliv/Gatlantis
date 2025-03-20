#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

from Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    # Base class for all game entities, providing common functionality like position, health, and damage.

    def __init__(self, name: str, position: tuple):
        # Initialize entity with its name, position, and associated attributes.
        self.name = name  # Name of the entity (used to identify it).
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()  # Load the entity's image.
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  # Get the position and size of the entity.
        self.speed = 0  # Initial movement speed of the entity.
        self.health = ENTITY_HEALTH[self.name]  # Set entity's health based on its name.
        self.damage = ENTITY_DAMAGE[self.name]  # Set entity's damage value based on its name.
        self.score = ENTITY_SCORE[self.name]  # Set entity's score value based on its name.
        self.last_damage = 'Null'  # Track the last entity that dealt damage (if applicable).

    # Abstract method to define movement behavior for entities (to be implemented by subclasses).
    @abstractmethod
    def move(self, ):
        pass
