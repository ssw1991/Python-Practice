"""
Author: Shilo Wilson

2) Extend exercise 1) to handle the situation when the user inputs something other than a number, using exception handling.
If the user does not enter a number, the code should provide the user with an error message and ask the user to try again.

Note that this is an example of duck typing.
"""

def main():
    print('========== Exercise 3.3.2 ==========')
    complete = 1
    while complete:
        numerator = raw_input('Please enter the numerator: ')
        denominator = raw_input('Please enter the denominator: ')
        try:
            print float(numerator) / float(denominator)
            complete = 0
        except ZeroDivisionError as e:
            print(e.message)
            print('Please try again')
        except ValueError as e:
            print(e.message)
            print('Please try again')



if __name__ == '__main__':
    main()