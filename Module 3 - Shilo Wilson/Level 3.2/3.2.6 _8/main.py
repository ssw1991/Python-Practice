"""
Author: Shilo Wilson

6) Create three generator expressions and use itertools.chain to attach them together. Print out the result as a list.

7) Create three generator expressions and zip them together. Print out the result as a list.

8) Create three generator expressions and use the appropriate itertools function to get all the combinations of the values.
 Print out the result as a list.
"""
from itertools import chain
from itertools import izip
from itertools import product


def oddIntegers(n):
    i=0
    while i <= n:
        yield i*2 + 1
        i += 1


def fact(n):
    i = 0
    prev = 1
    while i <=n:
        yield max(1, i*prev)
        prev = max(1, i*prev)
        i += 1


def squares(n):
    i=0
    while i <= n:
        yield i**2
        i += 1


def main():
    print ('========== Exercises 3.2.6, 3.2.7, 3.2.8 ==========\n')

    odd = oddIntegers(5)
    facts = fact(5)
    square = squares(5)

    chained = chain(odd, facts, square)
    print('Chained List: {}'.format(list(chained)))

    odd = oddIntegers(5)
    facts = fact(5)
    square = squares(5)

    zipped = izip(odd, facts, square)
    print('Zipped List: {}'. format(list(zipped)))

    odd = oddIntegers(5)
    facts = fact(5)
    square = squares(5)

    prod = product(odd, facts, square)
    print('Products {}'.format(list(prod)))


if __name__ == '__main__':
    main()
