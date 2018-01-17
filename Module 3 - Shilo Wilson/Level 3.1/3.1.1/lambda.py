"""
Author: Shilo Wllson
1) Create a stored lambda function that calculates the hypotenuse of a right triangle; it should take base and height as
its parameter. Invoke (test) this lambda with different arguments.

"""

hypotenuseCalc = lambda a, b: (a**2 + b**2)**.5


def main():
    txt = 'The hypotenuse of a triangle with ' \
          'base {} and height {} is {}'

    print txt.format(5, 6, hypotenuseCalc(5, 6))
    print txt.format(14, 32, hypotenuseCalc(14, 32))
    print txt.format(8, 9, hypotenuseCalc(8, 9))


if __name__ == '__main__':
    main()
