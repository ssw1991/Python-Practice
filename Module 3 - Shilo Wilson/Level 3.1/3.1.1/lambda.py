"""
Author: Shilo Wllson
1) Create a stored lambda function that calculates the hypotenuse of a right triangle; it should take base and height as
its parameter. Invoke (test) this lambda with different arguments.

"""

hypotenuseCalc = lambda a, b: (a**2 + b**2)**.5


def main():
    print(hypotenuseCalc(3, 4))


if __name__ == '__main__':
    main()
