# MEDIAN

The MEDIAN game, as described [here](https://gilkalai.wordpress.com/2017/01/14/the-median-game/).

## How the game is played

The goal is to end the game with the median number of points.  Each game lasts 8 rounds.
Every round, players say a number between 1 and 8 inclusive.  If there is a median score,
that player gets 1 point for that round.  Ties mean no points are awarded.

The winner is the person who has the median score after all 8 rounds.  Ties mean nobody wins.

For example, if a round's guesses are 1, 6, and 4, the third player gets a point.
If a round's guesses are 3, 5, and 5, nobody gets any points for that round.

Similarly, if the final score is 2, 0, 4, the first player wins.
If the final score is 2, 2, 3, nobody wins.

## Usage

You can run a tournament by invoking `$ python median.py`.  This will run a sample
tournament of 1000 games with some default players.  After it's done it will
print out the winning percentages of each player.

For interactive use, you can create three `Player`s of your choice and use
`median.run_tournament` to pit them against each other.

## Roadmap

Add as many strategies as practical.
