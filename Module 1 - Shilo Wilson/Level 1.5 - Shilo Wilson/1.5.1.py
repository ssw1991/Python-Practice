# coding=utf-8
"""
Name:  Shilo S Wilson

Exercise: 1.5.1

 Port Exercise 1.2.8 to use sets instead of lists. What’s the benefit?

Create two lists: The first list should be called ‘players’, and contain at least ten unique names. The second list
should be called ‘injured_players’, and contain a few names of players from the first list. Create a list comprehension
which results in a list containing all active (non-injured) players

"""





def main():

    print('============= Exercise 1.5.1 =============\n\n\n')

    names = set(['James', 'John', 'Jack', 'Bill', 'Terry', 'Tim', 'Tom', 'Sam', 'Derick', 'Tony'])
    injured = set(['John', 'Terry', 'Tim'])

    non_injured = (names - injured)

    print 'The following players are not injured\n'

    print ', '.join(str(o) for o in non_injured)

    """
    The advantage of set over list is that they operate faster than list in checking for content 
    which makes finding the difference better.
    """


if __name__ == '__main__':
    main()