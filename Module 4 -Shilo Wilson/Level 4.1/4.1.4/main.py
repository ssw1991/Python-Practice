"""
Author: Shilo Wilson

4) Create a program that does the following:
a. Prompts the user for name, age (integer), and country of residence. Display the information as follows:
<name> is <age> years old and lives in <country>.
b. Do the same as above, but using a decimal number for the age.
Display the number with one decimal place.
Write a separate version of the above using format flags, a version using the format function with numeric placeholders,
and a version using the format function with keyword placeholders which is cleaner?

"""


def main():
    print('========== 4.1.4 ==========\n')

    age = int(raw_input('Please enter your age: '))
    name = raw_input('Please enter your name: ')
    country = raw_input('Please entry your country of residence: ')

    print 'Using format flags'
    print('%s is %i years old and lives in %s' % (name, age, country))
    print 'With decimal'
    print('%s is %.1f years old and lives in %s' % (name, age, country))
    print 'With format function and numeric placeholders'
    print('{0} is {1} years old and lives in {2}'.format(name, age, country))
    print 'With format function and keyword placeholders'
    print('{name} is {age} years old and lives in {country}'.format(name=name, age=age, country=country))


if __name__ == '__main__':
    main()