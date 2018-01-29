"""
Author: Shilo Wilson

3) Create a list as follows: ['C:', 'Users', 'Me', 'Desktop', 'MyTable.csv']. Perform the following:
a. Join the list together to create a valid pathname.
b. Insert another folder into the list, between 'Desktop' and 'MyTable.csv' and join the resulting list to create a valid pathname.

"""


def main():
    print('========== 4.1.3 ==========')
    test = ['C:', 'Users', 'Me', 'Desktop', 'MyTable.csv']
    print('A: Pathname is {}'.format('\\'.join(test)))
    test.insert(-1, 'Loans')
    newpath = '\\'.join(test)
    print('C: New path is {}'.format(newpath))


if __name__ == '__main__':
    main()
