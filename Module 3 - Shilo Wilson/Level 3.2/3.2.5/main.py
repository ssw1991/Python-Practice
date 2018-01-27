"""
Author: Shilo Wilson

5) Generator expressions:
    a. Create a list comprehension that contains the square of all numbers from 0-5,000,000, using range. Sum this list,
    using the built-in sum function.
    b. Port the above to a generator expression, using xrange. Sum this generator expression, using the built-in sum
    function.
    c. Compare the total time taken to build and sum each. Which one is faster? What are the benefits of using the
    generator instead of the list comprehension? Why?
"""

from Timer import Timer as timer


def main():
    print ('========== Exercise 3.2.5 ==========\n')

    t = timer()
    t.start()
    print('Sum of list : {}'.format(sum([i ** 2 for i in range(5000001)])))
    t.end()

    t.start()
    print('Sum of generator : {}'.format(sum(i ** 2 for i in xrange(5000001))))
    t.end()

    """
    The generator is marginally faster.   However, it does not hold the list in memory and is more efficient
    """


if __name__ == '__main__':
    main()