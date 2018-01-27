"""
Author: Shilo Wilson

3) Create a function that calculates the factorial of an input number. If the input value is invalid, raise an exception.
 Test this out in main(), and handle the exception. Provide several examples, using explicit error handling and general
 error handling (catching all error types).
"""


def factorial(n):
    if int(n) != n:
        raise TypeError('Number could not be converted to Integer without loss of data')
    if n < 0:
        raise ValueError('Factorial Not defined for negative integers')
    return reduce(lambda x, y: x*y, [1]+range(1, n+1))


def main():
    print('========== Exercise 3.3.3 ==========')

    try:
        print(factorial(5))
    except TypeError as e:
        print e.message
    except ValueError as e:
        print e.args[0]
    except Exception as e:
        print e.message

    try:
        print(factorial(-5))
    except TypeError as e:
        print e.message
    except ValueError as e:
        print e.args[0]
    except Exception as e:
        print e.message

    try:
        print(factorial(5.4))
    except TypeError as e:
        print e.message
    except ValueError as e:
        print e.message
    except Exception as e:
        print e

    try:
        print(factorial('f'))
    except TypeError as e:
        print e.message
    except ValueError as e:
        print e.message
    except Exception as e:
        print e.message



if __name__ == '__main__':
    main()