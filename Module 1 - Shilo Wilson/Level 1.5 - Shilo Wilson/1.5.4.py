# coding=utf-8
"""
Name:  Shilo S Wilson

Exercise: 1.5.4

 Create a set of mortgage terms, in years (10, 15, 30):
    a. Add a 5-year term to the set.
    b. Remove the 15-year term from the set.
    c. Remove a 45-year term from the set. What happens? How can you prevent that?
"""


import numpy as np

def main():

    print('============= Exercise 1.5.4 =============\n\n\n')

    terms = set([10,15,30])
    terms.add(5)
    terms.remove(15)

    #Remove throws an error if the item is not presen
    #terms.remove(45)

    terms.discard(45)

    print(terms)

if __name__ == '__main__':
    main()