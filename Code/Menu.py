import pygame.image
from pygame.font import Font
import sys
from pygame.rect import Rect
from pygame.surface import Surface

from Code.Const import WINDOW_WIDTH, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./Asset/demo.jpg')
        self.rect = self.surf.get_rect(left = 0, top= 0)

    def run(self, ):
        pygame.mixer_music.load('./Asset/Enchanted Festival.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(60, "Super Pig", COLOR_YELLOW, ((WINDOW_WIDTH / 2), 50))


            for i in range(len(MENU_OPTION)):
                self.menu_text(40, MENU_OPTION[i], COLOR_WHITE, ((WINDOW_WIDTH / 2), 200 + 60 * i))


            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End Pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("./asset/MysteryQuest-Regular.ttf", size = text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center = text_center_pos)
        self.window.blit(source=text_surf, dest = text_rect)