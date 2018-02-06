"""
Implement the probability Game.

The optimal solution would be too switch as knowledge was gained by the host selection of doors,
so the conditional probability that the prize is behind the unselected door is 2/3
"""
from game import player
from game import game
import logging
from Timer.Timer import Timer
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel('INFO')

@Timer
def runGame(strat, doors, n):
    results = [game(player(strat), doors)() for i in xrange(n)]
    return float(sum(results)) / len(results)


def main():
    print('The probability of success with a switching strategy is {}'.format(runGame(1, [1, 2, 3], 10000000)))
    print('The probability of success without a switching strategy is {}'.format(runGame(0, [1, 2, 3], 10000000)))

if __name__ =='__main__':
    main()