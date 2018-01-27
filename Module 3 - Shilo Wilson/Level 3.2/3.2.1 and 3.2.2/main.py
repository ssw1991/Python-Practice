"""
Author: Shilo Wilson

 Create a list of 1000 numbers. Convert the list to an iterable and iterate through it.

 The instructions are a bit confusing, as a list is already an iterable.   Is the intention
 to create an iterator to iterate through the list?
"""



def main():
    print('========== Exercise 3.2.1 and 3.2.2 ==========')
    mylist = range(1000)
    myiterator = iter(mylist)
    myreverse = reversed(mylist)

    for i in range(len(mylist)):
        print myiterator.next()

    for i in range(len(mylist)):
        print myreverse.next()


if __name__ == '__main__':
    main()