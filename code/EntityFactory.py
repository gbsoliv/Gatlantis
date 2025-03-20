#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from Const import WIN_WIDTH, WIN_HEIGHT


# Factory class responsible for creating and providing game entities based on their type/name.
class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        # Returns an entity instance based on the provided entity name.
        match entity_name:
            case 'Level1Bg':
                # Create a list of 5 background objects for Level 1.
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                return list_bg

            case 'Player':
                # Create and return the player entity starting at a fixed position.
                return Player('Player', (10, WIN_HEIGHT / 2))

            case 'Enemy1':
                # Create and return the first type of enemy, positioned randomly vertically.
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

            case 'Enemy2':
                # Create and return the second type of enemy, positioned randomly vertically.
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
