from Code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY
from Code.EnemyShot import EnemyShot
from Code.Entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple, images: list):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.images = images
        self.current_index = 0
        self.elapsed_time = 0
        self.surf = self.images[self.current_index]
        self.rect = self.surf.get_rect(topleft=position)


    def update(self, dt: int):
        self.elapsed_time += dt

        #Makes the raven's wings flap and the wolf run by switching frames every 60ms
        if self.elapsed_time > 60:
            self.current_index = (self.current_index + 1) % len(self.images)
            self.surf = self.images[self.current_index]
            self.elapsed_time = 0


    def move(self):
        #It causes them to move continuously to the left.
        self.rect.centerx -= ENTITY_SPEED[self.name]

        #If they go off-screen, they reappear on the right
        if self.rect.right < 0:
            self.rect.left = WIN_WIDTH + 100

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))