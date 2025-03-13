import pygame

# C
COLOR_BLACK = 0, 0, 0
COLOR_GREEN = 0, 255, 0
COLOR_WHITE = 255, 255, 255

# E

ENTITY_SPEED = {
    #    'Level1Bg1':0,
    #    'Level1Bg2':0,
    #    'Level1Bg3':0,
    #    'Level1Bg4':0,

    'Player': 5,

    'Enemy1': 2,
    'Enemy2': 1
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

#S

SPAWN_TIME = 3000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
