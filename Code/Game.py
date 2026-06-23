from Code.Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT
from Code.Level import Level
from Code.Menu import Menu
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))


    def run(self, ):


        while True:
            menu = Menu(self.window)
            menu_return = menu.run()


            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()  # Close Window
                quit()  # End Pygame
            else:
                pass

