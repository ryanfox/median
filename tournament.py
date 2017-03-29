from game import Game


class Tournament:
    def __init__(self, players, rounds=1000):
        self.players = players
        self.rounds = rounds
        self.scores = [0, 0, 0]

    def play(self):
        for i in range(self.rounds):
            game = Game()

            for j in range(game.length):
                plays = [player.play(game, position) for position, player in enumerate(self.players)]
                game.play_round(*plays)

            if game.winner():
                self.scores[game.winner() - 1] += 1

        return self.scores
