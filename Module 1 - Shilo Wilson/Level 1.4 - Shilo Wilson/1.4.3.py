# coding=utf-8
"""
Name:  Shilo S Wilson

Exercise: 1.4.3

 Sum the full list of mortgages, to obtain the total amount owed to your firm.

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

    print('============= Exercise 1.4.3 =============\n\n\n')

    mortgages         = Mortgages(1000)
    miniMortgages     = filter(lambda x: x<200,mortgages)
    standardMortgages = filter(lambda x: 200<=x<=467,mortgages)
    jumboMortgages    = filter(lambda x: x>467,mortgages)



    print sum(mortgages)


if __name__ == '__main__':
    main()