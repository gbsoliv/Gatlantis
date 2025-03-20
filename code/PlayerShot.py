from code.Entity import Entity
from Const import ENTITY_SPEED


class PlayerShot(Entity):
    # Initialize the PlayerShot object with a name and position
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    # Move the PlayerShot horizontally based on its speed
    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]
