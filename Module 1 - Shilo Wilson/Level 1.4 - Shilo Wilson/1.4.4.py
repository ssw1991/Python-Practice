# coding=utf-8
"""
Name:  Shilo S Wilson

Exercise: 1.4.4

 Find the minimum and maximum mortgage amount owed, for each mortgage sub-list.

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

    print('============= Exercise 1.4.4 =============\n\n\n')

    mortgages         = Mortgages(1000)
    miniMortgages     = filter(lambda x: x<200,mortgages)
    standardMortgages = filter(lambda x: 200<=x<=467,mortgages)
    jumboMortgages    = filter(lambda x: x>467,mortgages)



    print 'The minimum mini-mortgage is {}, the maximum is {}'.format(min(miniMortgages), max(miniMortgages))
    print 'The minimum standard-mortgage is {}, the maximum is {}'.format(min(standardMortgages), max(standardMortgages))
    print 'The minimum jumbo-mortgage is {}, the maximum is {}'.format(min(jumboMortgages), max(jumboMortgages))


if __name__ == '__main__':
    main()