# coding=utf-8
"""
Name:  Shilo S Wilson

Exercise: 1.5.3

Create a list of unique mortgage amounts.
"""


import numpy as np

def main():

    print('============= Exercise 1.5.3 =============\n\n\n')

    uniqueMortgage = list(set(np.random.random_integers(100,1000,1000)))

    print len(uniqueMortgage)



if __name__ == '__main__':
    main()