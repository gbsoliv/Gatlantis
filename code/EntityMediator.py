from code.EnemyShot import EnemyShot
from code.PlayerShot import PlayerShot
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
from Const import WIN_WIDTH


class EntityMediator:
    # Mediator class for managing interactions and collisions between game entities.

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):  # If an Enemy moves off the left edge, set its health to 0.
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):  # If a PlayerShot leaves the right edge of the window, set its health to 0.
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):  # If an EnemyShot leaves the left edge of the window, set its health to 0.
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        # Check if two entities have collided and handle resulting state changes.
        valid_interaction = False

        # Determine if a valid interaction exists between the entities.
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:  # If valid entities interact, check for collision.
            if (ent1.rect.right >= ent2.rect.left and  # Horizontal overlap.
                    ent1.rect.left <= ent2.rect.right and  # Horizontal overlap.
                    ent1.rect.bottom >= ent2.rect.top and  # Vertical overlap.
                    ent1.rect.top <= ent2.rect.bottom):  # Vertical overlap.

                # Update health and record names for damage tracking.
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_damage = ent2.name
                ent2.last_damage = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        # Award score to the player if the enemy was destroyed by a PlayerShot.
        if enemy.last_damage == 'PlayerShot':  # Check if the last damage source was a PlayerShot.
            for ent in entity_list:
                if ent.name == 'Player':  # Find the Player entity and add the enemy's score value.
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        # Check collisions between entities and handle any relevant interactions.
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)  # Check if entity is out of bounds.

            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)  # Check for collisions with other entities.

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        # Remove entities with 0 or less health and handle special cases like scoring.
        for ent in entity_list:
            if ent.health <= 0:  # Remove dead entities.
                if isinstance(ent, Enemy):  # If an Enemy is destroyed, award score to the player.
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)  # Remove the entity from the list.
