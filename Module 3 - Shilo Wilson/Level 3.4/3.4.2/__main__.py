"""
Author: Shilo Wilson

Modify the Timer class to work as a context manager. Essentially, it should be possible to do the following:
"""
from Timer import Timer as Timer


def main():
    print '========== Exercise 3.4.2 =========='

    with Timer('My Timer') as t:
        sum(i**2 for i in xrange(5000000))
        t.configureTimerDisplay('s')



if __name__ == '__main__':
    main()