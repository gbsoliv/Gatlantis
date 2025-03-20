#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity


# Represents a background entity in the game which is derived from the base Entity class.
# Initializes the background entity with a name and position.


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    # Placeholder for the move logic of the background entity.
    def move(self):
        pass
