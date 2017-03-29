# The MEDIAN game.  Via:
# https://gilkalai.wordpress.com/2017/01/14/the-median-game/

from players import RandomPlayer, ConstantPlayer, ScorePlusTwoPlayer
from tournament import Tournament


def run_tournament(player1, player2, player3):
    tournament = Tournament((player1, player2, player3))
    results = tournament.play()

    width = max(len(player.name) for player in [player1, player2, player3])

    player = 'Player'
    print(f'{player:>{width}} |  Win%')
    print(f'{player1.name:>{width}} | {results[0] / tournament.rounds:.3f}')
    print(f'{player2.name:>{width}} | {results[1] / tournament.rounds:.3f}')
    print(f'{player3.name:>{width}} | {results[2] / tournament.rounds:.3f}')

    tie = 'Tie'
    print(f'{tie:>{width}} | {sum(results) / tournament.rounds:.3f}')


if __name__ == '__main__':
    run_tournament(ScorePlusTwoPlayer(), RandomPlayer(), ConstantPlayer())
