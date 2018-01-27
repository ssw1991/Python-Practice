"""
Author: Shilo Wilson

Create a fibonnaci generator function

"""


def fibonacci():
    x = 0
    y = 1
    while 1:
        yield x
        x, y = y, x + y


def main():

    print ('========== Exercise 3.2.4 ==========\n')
    fib = fibonacci()

    print('1: {}'.format(fib.next()))
    print('2: {}'.format(fib.next()))

    for i in range(3, 1000000):
        print('{}: {}'.format(i, fib.next()))



if __name__ == '__main__':
    main()