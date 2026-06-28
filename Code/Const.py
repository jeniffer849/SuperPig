# C
import pygame

COLOR_YELLOW = (230, 191, 38)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (161, 250, 79)

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
ENTITY_SHOT_DELAY = {
    'player': 4,
    'enemy1' : 30,
    'enemy2' : 30
}
# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')
# P
PLAYER_KEY_SHOOT = {'player': pygame.K_SPACE
                    }

# W
WIN_WIDTH = 700
WIN_HEIGHT = 394