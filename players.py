import random


class Player:
    def play(self, *args, **kwargs):
        raise NotImplementedError


class RandomPlayer(Player):
    def __init__(self):
        self.name = 'Random'

    def play(self, *args, **kwargs):
        return random.randrange(1, 9)


class ConstantPlayer(Player):
    def __init__(self, constant=4):
        self.name = 'Constant {}'.format(constant)
        self.constant = constant

    def play(self, *args, **kwargs):
        return self.constant


class ScorePlusTwoPlayer(Player):
    def __init__(self):
        self.name = 'Score+2'

    def play(self, game=None, position=None):
        return min(8, game.get_score()[position] + 2)


class HumanPlayer(Player):
    def __init__(self):
        self.name = 'Human'

    def play(self, game=None, position=None):
        print(f'Game (you are player #{position}:')
        print(game)
        print(game.get_score())
        return int(input('>'))
