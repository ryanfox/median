class GameError(Exception):
    pass


class Game:
    def __init__(self, length=8):
        self.plays = []
        self.length = length

    def __str__(self):
        return '\n'.join([str(play) for play in self.plays])

    def play_round(self, num1, num2, num3):
        if len(self.plays) > self.length:
            raise GameError('Already played full game')
        if any(num > 8 for num in [num1, num2, num3]):
            raise GameError(f'Play {max(num1, num2, num3)} out of range')
        if any(num < 1 for num in [num1, num2, num3]):
            raise GameError(f'Play {min(num1, num2, num3)} out of range')

        self.plays.append((num1, num2, num3))

    @staticmethod
    def median(score1, score2, score3):
        if score2 < score1 < score3 or score3 < score1 < score2:
            return 1
        if score1 < score2 < score3 or score3 < score2 < score1:
            return 2
        if score1 < score3 < score2 or score2 < score3 < score1:
            return 3
        return None

    def get_score(self):
        scores = [0, 0, 0]
        for i in range(len(self.plays)):
            if self.median(*self.plays[i]):
                scores[self.median(*self.plays[i]) - 1] += 1

        return scores

    def winner(self):
        return self.median(*self.get_score())
