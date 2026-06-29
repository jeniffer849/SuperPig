import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from Code.Const import WIN_HEIGHT, EVENT_ENEMY, COLOR_RED, COLOR_WHITE
from Code.Enemy import Enemy
from Code.Entity import Entity
from Code.EntityFactory import EntityFactory
from Code.EntityMediator import EntityMediator
from Code.Player import Player


class Level:

    def __init__(self, window, name, game_mode, player_score):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.player_score = player_score
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('summer'))
        self.entity_list.extend(EntityFactory.get_entity('player'))
        self.timeout = 20000 #20 Seconds
        self.spawn_timer = 2000
        self.spawn_cooldown = 2000
        self.last_enemy = ''


    def run(self):
        pygame.mixer_music.load(f'./Asset/placeful-song-loop-.wav') #Level1 Music
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            dt = clock.tick(40)
            self.window.fill((0, 0, 0))
            self.spawn_timer += dt
            if self.spawn_timer >= self.spawn_cooldown:
                sort_enemy = random.choice(['enemy1', 'enemy2'])

                self.last_enemy = sort_enemy
                new_enemy = EntityFactory.get_entity(sort_enemy)
                self.entity_list.extend(new_enemy)
                self.spawn_cooldown = random.randint(1500, 3000)
                self.spawn_timer = 0

            new_shots = []
            for ent in self.entity_list:
                if ent is not None:
                    if hasattr(ent, 'update'):
                        ent.update(dt)

                    self.window.blit(source = ent.surf, dest = ent.rect)
                    ent.move()

                    if isinstance(ent, (Player, Enemy)):
                        shoot = ent.shoot()
                        if shoot is not None:
                            new_shots.append(shoot)
                    if ent.name == 'player':
                        self.level_text(20, f'Player - Health: {ent.health} | Score: {ent.score}', COLOR_RED, (10, 25))
            if new_shots:
                self.entity_list.extend(new_shots)
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            self.timeout -= dt

            #Look for the player in the list to see if they are still alive
            active_player = False
            for ent in self.entity_list:
                if ent is not None and ent.name == 'player':
                    active_player = True
                    #Updates the Game.py score list with the player's current points
                    self.player_score[0] = ent.score
                    break

            #DEFEAT CONDITION: If the player has disappeared from the list (died), the level ends
            if not active_player:
                return False

            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Close window in the level1
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.extend(EntityFactory.get_entity('enemy1'))

            # Printed text
            self.level_text(14,f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entitades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            self.entity_list = [ent for ent in self.entity_list if ent is not None and ent.health > 0 and ent.rect.right > -100]

            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name = "Lucida Sans Typewriter" , size = text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left = text_pos[0], top = text_pos[1])
        self.window.blit(source = text_surf, dest = text_rect)
