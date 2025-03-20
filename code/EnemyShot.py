from code.Entity import Entity
from Const import ENTITY_SPEED


# Represents an enemy shot in the game, derived from the base Entity class.
class EnemyShot(Entity):
    # Initialize the enemy shot with its name and starting position.
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    # Moves the enemy shot by decreasing its horizontal position.
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
