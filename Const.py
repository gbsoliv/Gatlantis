# Game configuration constants for a 2D Pygame project, including settings for colors,
# entity stats (speed, health, damage, etc.), game events, menu options, controls,
# and screen dimensions. These values define the basic mechanics and appearance of the game.

import pygame

# C
COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_PURPLE = (128, 0, 128)

# E

ENTITY_SPEED = {
    'Player': 5,
    'PlayerShot': 3,

    'Enemy1': 1,
    'Enemy1Shot': 5,

    'Enemy2': 1,
    'Enemy2Shot': 2,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,

    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,

    'Player': 300,
    'PlayerShot': 3,

    'Enemy1': 50,
    'Enemy1Shot': 1,

    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'Player': 20,
    'Enemy1': 80,
    'Enemy2': 120,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,

    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,

    'Player': 1,
    'PlayerShot': 25,

    'Enemy1': 1,
    'Enemy1Shot': 15,

    'Enemy2': 1,
    'Enemy2Shot': 15,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,

    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,

    'Player': 0,
    'PlayerShot': 0,

    'Enemy1': 100,
    'Enemy1Shot': 0,

    'Enemy2': 125,
    'Enemy2Shot': 0,
}

EVENT_TIMEOUT = pygame.USEREVENT + 2
EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTIONS = ('NEW GAME ',
                'EXIT')

TIMEOUT_LEVEL = 20000  # 20s

# P

PLAYER_KEY_SHOOT = {'Player': pygame.K_SPACE}

# S

SPAWN_TIME = 3000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
