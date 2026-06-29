# C
import pygame
from pygame.examples.grid import WINDOW_WIDTH

COLOR_YELLOW = (230, 191, 38)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (161, 250, 79)
COLOR_RED = (255, 3, 3)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'summer0': 0,
    'summer1': 1,
    'summer2': 1,
    'player': 5,
    'enemy1': 5,
    'enemy2': 8,
    'PlayerShot': 10,
    'playerShot': 10,
    'enemy1Shot': 10,
    'enemy2Shot': 10

}
ENTITY_HEALTH = {
    'summer0': 999,
    'summer1': 999,
    'summer2': 999,
    'player': 100,
    'PlayerShot': 1,
    'playerShot': 1,
    'enemy1': 1,
    'enemy1Shot': 1,
    'enemy2': 1,
    'enemy2Shot': 1
}
ENTITY_DAMAGE = {
    'summer0': 0,
    'summer1': 0,
    'summer2': 0,
    'player' : 1,
    'PlayerShot': 1,
    'playerShot': 1,
    'enemy1': 10,
    'enemy1Shot': 20,
    'enemy2': 10,
    'enemy2Shot': 15
}
ENTITY_SCORE = {
    'summer0': 0,
    'summer1': 0,
    'summer2': 0,
    'player' : 0,
    'PlayerShot': 0,
    'playerShot': 0,
    'enemy1': 100,
    'enemy1Shot': 0,
    'enemy2': 50,
    'enemy2Shot': 0
}
ENTITY_SHOT_DELAY = {
    'player': 6,
    'enemy1' : 30,
    'enemy2' : 30
}
# M
MENU_OPTION = ('NEW GAME',
               'CONTROLS',
               'SCORE',
               'EXIT'
               )
# P
PLAYER_KEY_SHOOT = {'player': pygame.K_SPACE
                    }

# W
WIN_WIDTH = 700
WIN_HEIGHT = 394

# S
SCORE_POS = {
    'Title1': (WIN_WIDTH / 2, 100),
    'EnterName': (WIN_WIDTH / 2, 180),
    'Name': (WIN_WIDTH / 2, 250),
    'Title2': (WIN_WIDTH / 2, 40),
    'Label': (WIN_WIDTH / 2, 85),
    0: (WIN_WIDTH / 2, 120),
    1: (WIN_WIDTH / 2, 142),
    2: (WIN_WIDTH / 2, 164),
    3: (WIN_WIDTH / 2, 186),
    4: (WIN_WIDTH / 2, 208),
    5: (WIN_WIDTH / 2, 230),
    6: (WIN_WIDTH / 2, 252),
    7: (WIN_WIDTH / 2, 274),
    8: (WIN_WIDTH / 2, 296),
    9: (WIN_WIDTH / 2, 318),
}