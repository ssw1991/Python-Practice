"""
Author: Shilo Wilson

1) Create code that takes a numerator and denominator input from the user. Output the quotient in decimal form.
Handle the divide-by-zero case gracefully, using exception handling.
"""


def main():
    print('========== Exercise 3.3.1 ==========')
    numerator = raw_input('Please enter the numerator: ')
    denominator = raw_input('Please enter the denominator: ')

    try:
        print float(numerator) / float(denominator)
    except ZeroDivisionError as e:
        print(e.message)


if __name__ == '__main__':
    main()