import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Code.Const import COLOR_YELLOW, COLOR_WHITE, COLOR_GREEN


class Controls:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./Asset/ControlsBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def run(self):

        pygame.mixer_music.load('./Asset/Enchanted Festival.mp3')
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()
        center_x = self.window.get_width() / 2

        while True:
            clock.tick(40)

            self.window.blit(source=self.surf, dest=self.rect)

            controls = [
                "Up Arrow - Jump",
                "Right Arrow - Move to the Right",
                "Left Arrow - Move to the Left",
                "Space - Shoot",
                "Esc - Back to Menu"
            ]

            y_offset = 160
            for linha in controls:
                self.control_text(30, linha, COLOR_WHITE, (center_x, y_offset))
                y_offset += 50

            # Event monitoring to close or return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:

                    # If you press ESC or SPACE, it returns to exit this loop and go back to the menu
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                        return

            pygame.display.flip()

    def control_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):

        # Reuses the same stylized font from the menu
        text_font: Font = pygame.font.Font("./Asset/MysteryQuest-Regular.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)