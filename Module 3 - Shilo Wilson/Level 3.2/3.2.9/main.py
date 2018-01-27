"""
Author: Shilo Wilson

9) Create a list of ten names. Loop through the list and output each name in the following format:
Name 1: Henry Name 2: Jake
"""

def main():
    print ('========== Exercise 3.2.9 ==========\n')

    names =['Ryan', 'Natalia', 'Jack', 'James', 'Bill', 'Megan', 'Stephanie', 'Marine', 'Jesse', 'Jodi']

    for i, v in enumerate(names):
        print('Name {}: {}'.format(i+1, v))


if __name__ == '__main__':
    main()