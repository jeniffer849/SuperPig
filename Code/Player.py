import pygame.key

from Code.Const import ENTITY_SPEED, WIN_WIDTH
from Code.Entity import Entity

class Player(Entity):

    def __init__(self, name: str, position: tuple, images_run: list, images_jump: list):
        super().__init__(name, position)

        #left and right variables
        self.images_run = images_run
        self.images_jump = images_jump
        self.current_index = 0
        self.elapsed_time = 0
        self.surf = self.images_run[self.current_index]
        self.is_running = False
        self.facing_left = False
        self.rect = self.surf.get_rect(topleft=position)

        #Variable for the jump
        self.speed_y = 0
        self.gravity = 1
        self.jump_force = -16
        self.floor_y = position[1] #use position[1] to get only the Y-height from the ground
        self.is_jumping = False

    def update(self, dt: int):
            self.elapsed_time += dt #Adds the time that has elapsed since the last game frame

            if self.elapsed_time > 40:
                if self.is_running or self.is_jumping:
                    self.current_index = (self.current_index + 1) % 25
                else:
                    self.current_index = 3
                self.elapsed_time = 0

            if self.is_jumping:
                actual_frame = self.images_jump[self.current_index]
            else:
                actual_frame = self.images_run[self.current_index]

            if self.facing_left:
                self.surf = pygame.transform.flip(actual_frame, True, False)
            else:
                self.surf = actual_frame

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        self.is_running = False

        #Moving to the right
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
            self.is_running = True
            self.facing_left = False


        #Moving to the left
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
            self.is_running = True
            self.facing_left = True

        #jumping
        if (pressed_key[pygame.K_SPACE] or pressed_key[pygame.K_UP]) and not self.is_jumping:
            self.speed_y = self.jump_force
            self.is_jumping = True
            self.current_index = 0

        self.speed_y += self.gravity
        self.rect.top += self.speed_y

        if self.rect.top >= self.floor_y:
            self.rect.top = self.floor_y
            self.speed_y = 0
            self.is_jumping = False

        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH

        if self.rect.left < 0:
                self.rect.left = 0