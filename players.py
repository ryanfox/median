import random


class Player:
    def play(self, *args, **kwargs):
        raise NotImplementedError

    @staticmethod
    def is_winning(game, position):
        return game.winner() == position + 1


class GreedyPlayer(Player):
    """
    Attempts to play a greedy strategy: if not currently winning, plays 4/5.
    If currently winning, plays 1/8.
    """
    def __init__(self):
        self.name = 'Greedy'

    def play(self, game=None, position=None):
        if self.is_winning(game, position):
            return random.choice([1, 8])

        return random.choice([4, 5])


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


class ScorePlusPlayer(Player):
    def __init__(self, plus=2):
        self.name = f'Score+{plus}'
        self.plus = plus

    def play(self, game=None, position=None):
        return min(8, game.get_score()[position] + self.plus)


class HumanPlayer(Player):
    def __init__(self):
        self.name = 'Human'

    def play(self, game=None, position=None):
        print(f'Game (you are player #{position + 1}):')
        print(game)
        print('Scores:')
        print(game.get_score())
        return int(input('>'))
