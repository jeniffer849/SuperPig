import sys
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

from Code.Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT
from Code.Controls import Controls
from Code.Level import Level
from Code.Menu import Menu
import pygame

from Code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))


    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()


            if menu_return == MENU_OPTION[0]:
                player_score = [0, 0]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run()
                score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[1]:
                controls_screen = Controls(self.window)
                controls_screen.run()

            elif menu_return == MENU_OPTION[2]:
                score.show()

            elif menu_return == MENU_OPTION[3]:
                pygame.quit()  # Close Window
                sys.exit()  # End Pygame
            else:
                pass

