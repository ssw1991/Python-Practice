# coding=utf-8
"""
Name:  Shilo S Wilson

Exercise: 1.4.2

Find the length of each list in part b of the previous exercise.
Then, verify that the lengths of all three lists indeed add up to the length of the full list in part a.


"""

import numpy as np

def Mortgages(N):
    """
    A function that returns an unsorted list of mortgage amounts

    :param N:
    :return:

    """

    return list(np.random.random_integers(100,1000,size = N))



def main():

    print('============= Exercise 1.4.2 =============\n\n\n')

    mortgages         = Mortgages(1000)
    miniMortgages     = filter(lambda x: x<200,mortgages)
    standardMortgages = filter(lambda x: 200<=x<=467,mortgages)
    jumboMortgages    = filter(lambda x: x>467,mortgages)

    full_list = len(mortgages)

    print full_list == (len(miniMortgages + standardMortgages + jumboMortgages))


if __name__ == '__main__':
    main()