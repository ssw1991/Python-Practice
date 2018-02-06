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
import multiprocessing
from functools import partial



def runGame(strat, doors):
    return game(player(strat), doors)()

@Timer
def mp_pool(nproc, size):
    f0 = partial(runGame, doors=[1, 2, 3])
    f1 = partial(runGame, doors=[1, 2, 3])
    pool = multiprocessing.Pool(nproc)
    ns1 = [1] * size
    ns0 = [0] * size
    res0 = pool.map(f0, ns0)
    res1 = pool.map(f1, ns1)
    print('The probability of success with a switching strategy is {}'.format(float(sum(res0)) / len(res0)))
    print('The probability of success without a switching strategy is {}'.format(float(sum(res1)) / len(res1)))


def main():
    mp_pool(8, 10000000)

if __name__ =='__main__':
    main()