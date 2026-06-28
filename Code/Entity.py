from abc import ABC, abstractmethod

import pygame.image

from Code.Const import ENTITY_DAMAGE, ENTITY_HEALTH


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./Asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH.get(self.name, 1)
        self.damage = ENTITY_DAMAGE.get(self.name, 1)
        self.last_dmg = 'None'

    @abstractmethod
    def move(self, ):
        pass