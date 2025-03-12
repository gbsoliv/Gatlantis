#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity
from const import WIN_WIDTH



class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pass
