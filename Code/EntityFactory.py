import pygame.image


from Code.Background import Background
from Code.Const import WIN_WIDTH
from Code.Enemy import Enemy
from Code.Player import Player


class EntityFactory:


    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'summer':
                list_sum = []
                for i in range(3):
                    list_sum.append(Background(f'summer{i}', (0, 0)))
                    list_sum.append(Background(f'summer{i}', (WIN_WIDTH, 0)))
                return list_sum
            case 'player':
                SheetRun = pygame.image.load("./Asset/pig-run.png").convert_alpha()
                SheetJump = pygame.image.load("./Asset/pig-jump.png").convert_alpha()

                #Define the dimensions of the uploaded image note
                columns = 5
                lines = 5

                #Divide the dimensions to find the size of each individual piggy bank
                w_run = SheetRun.get_width() // columns
                h_run = SheetRun.get_height() // lines

                w_jump = SheetJump.get_width() // columns
                h_jump = SheetJump.get_height() // lines

                SpriteRun = []
                SpriteJump = []

                #It traverses the rows and columns, slicing each frame.
                for l in range(lines):
                    for c in range(columns):

                        #Run Slicing (Maintaining the 140x140 size you chose)
                        area_run = pygame.Rect(c * w_run, l * h_run, w_run, h_run)
                        pig_run = pygame.transform.scale(SheetRun.subsurface(area_run), (140, 140))
                        SpriteRun.append(pig_run)

                        #Jump to Slicing (Also in 140x140 to maintain the aspect ratio)
                        area_jump = pygame.Rect(c * w_jump, l * h_jump, w_jump, h_jump)
                        pig_jump = pygame.transform.scale(SheetJump.subsurface(area_jump), (140, 140))
                        SpriteJump.append(pig_jump)

                list_play = []
                list_play.append(Player('player', (50, 220), SpriteRun, SpriteJump))

                return list_play

            #Enemy 1
            case 'enemy1':
                SpriteWolf = [
                    pygame.image.load("./Asset/EnemyRun1.png").convert_alpha(),
                    pygame.image.load("./Asset/EnemyRun2.png").convert_alpha(),
                    pygame.image.load("./Asset/EnemyRun3.png").convert_alpha(),
                    pygame.image.load("./Asset/EnemyRun4.png").convert_alpha(),
                    pygame.image.load("./Asset/EnemyRun5.png").convert_alpha(),
                    pygame.image.load("./Asset/EnemyRun6.png").convert_alpha(),
                    pygame.image.load("./Asset/EnemyRun7.png").convert_alpha(),
                    pygame.image.load("./Asset/EnemyRun8.png").convert_alpha(),
                    pygame.image.load("./Asset/EnemyRun9.png").convert_alpha()
                ]

                sheet_wolf = pygame.image.load("./Asset/Enemy1.png").convert_alpha()
                sheet_wolf.set_colorkey((255, 255, 255))
                columns = 8
                frame_width = sheet_wolf.get_width() // columns
                frame_height = sheet_wolf.get_height()

                #Resizes while maintaining the correct aspect ratio
                for i in range(len(SpriteWolf)):
                    SpriteWolf[i] = pygame.transform.scale(SpriteWolf[i], (100, 100))

                return [Enemy('enemy1', (WIN_WIDTH + 10, 250), SpriteWolf)]

            case 'enemy2':

                #Loads each individual frame of the wolf, already cut out and cleaned up
                SpriteBird = [
                    pygame.image.load("./Asset/EnemyBird1.png").convert_alpha(),
                    pygame.image.load("./Asset/EnemyBird2.png").convert_alpha(),
                    pygame.image.load("./Asset/EnemyBird3.png").convert_alpha(),
                    pygame.image.load("./Asset/EnemyBird4.png").convert_alpha(),
                    pygame.image.load("./Asset/EnemyBird5.png").convert_alpha(),
                    pygame.image.load("./Asset/EnemyBird6.png").convert_alpha(),

                ]

                #Resizes while maintaining the correct aspect ratio
                for i in range(len(SpriteBird)):
                    SpriteBird[i] = pygame.transform.scale(SpriteBird[i], (50, 50))

                return [Enemy('enemy2', (WIN_WIDTH + 10, 170), SpriteBird)]


        return None


