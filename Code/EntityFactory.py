from Code.Background import Background
from Code.Const import WIN_WIDTH


class EntityFactory:


    @staticmethod
    def get_entity(entity_name: str, position = (0, 0)):
        match entity_name:
            case 'summer':
                list_sum = []
                for i in range(3):
                    list_sum.append(Background(f'summer{i}', (0, 0)))
                    list_sum.append(Background(f'summer{i}', (WIN_WIDTH, 0)))
                return list_sum



