import pygame

# C
COLOR_BLACK = 0, 0, 0
COLOR_GREEN = 0, 255, 0
COLOR_WHITE = 255, 255, 255

# E

ENTITY_SPEED = {
    'Player': 5,
    'PlayerShot': 2,

    'Enemy1': 2,
    'Enemy2': 1,
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
}

EVENT_TIMEOUT = pygame.USEREVENT + 2
EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTIONS = ('NEW GAME ',
                'SCORE',
                'EXIT')

TIMEOUT_LEVEL = 20000  # 20s

# P

PLAYER_KEY_SHOOT = {'Player': pygame.K_SPACE}

# S

SPAWN_TIME = 3000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
