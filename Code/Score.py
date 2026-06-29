import sys

from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from Code.Const import COLOR_WHITE, SCORE_POS, COLOR_RED, MENU_OPTION
from Code.DBProxy import DBProxy


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./Asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./Asset/Enchanted Festival.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        text = 'Enter player name (8 characters): '
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(45, 'GAME OVER!', (194, 22, 9), SCORE_POS['Title1'])
            if game_mode == MENU_OPTION[0]:
                score = player_score

            self.score_text(24, text, COLOR_WHITE, SCORE_POS['EnterName'])


            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Close window in the level1
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) <= 8:
                        db_proxy.save({'name': name, 'score': score[0], 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 8:
                            name += event.unicode
            self.score_text(35, name, COLOR_WHITE, SCORE_POS['Name'])

            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./Asset/Enchanted Festival.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(35, 'TOP 10 SCORE', COLOR_RED, SCORE_POS['Title2'])
        col_name_x = 80
        col_score_x = 320
        col_date_x = 480

        y_label = SCORE_POS['Label'][1]
        self.score_text(22, 'NAME', COLOR_WHITE, (col_name_x, y_label), align_left=True)
        self.score_text(22, 'SCORE', COLOR_WHITE, (col_score_x, y_label), align_left=True)
        self.score_text(22, 'DATE', COLOR_WHITE, (col_date_x, y_label), align_left=True)

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for index, player_score in enumerate(list_score):
            id_, name, score, date = player_score

            pos_y = SCORE_POS[index][1]

            self.score_text(18, f'{name}', COLOR_WHITE, (col_name_x, pos_y), align_left=True)
            self.score_text(18, f'{score:05d}', COLOR_WHITE, (col_score_x, pos_y), align_left=True)
            self.score_text(18, f'{date}', COLOR_WHITE, (col_date_x, pos_y), align_left=True)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Close window in the level1
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, align_left = False):
        text_font: Font = pygame.font.SysFont(name = "Lucida Sans Typewriter" , size = text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        if align_left:
            text_rect: Rect = text_surf.get_rect(left = text_pos[0], top = text_pos[1])
        else:
            text_rect: Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"