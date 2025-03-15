#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity
from const import ENTITY_SPEED


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        pass