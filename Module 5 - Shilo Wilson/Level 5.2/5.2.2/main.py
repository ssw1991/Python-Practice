"""
Author: Shilo Wilson

Create a memoize decorator
"""

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel('WARN')

import time
from Utilities.Timer.Timer import Timer as Timer
from Utilities.utilities import memoize




@Timer
@memoize
def fib(n):
    """
    Using iteration to not get multiple calls to the timer
    :param n:
    :return:
    """
    if n == 0:
        return 0
    if n ==1:
        return 1
    n_2 = 0
    n_1 = 1
    result = 0
    for i in range(2,n):
        result = n_1 + n_2
        n_2 = n_1
        n_1 = result
    return result

@Timer
@memoize
def mysum(*args):
    time.sleep(5)
    return sum(args)


def main():
    print '========== Exercise 5.2.2 =========='


    print(fib(10000))
    print(fib(10000))

    mysum(1,2,3,4)
    mysum(1,2,3,4)

if __name__ == '__main__':
    main()