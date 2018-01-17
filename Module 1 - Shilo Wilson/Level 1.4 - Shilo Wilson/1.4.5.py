# coding=utf-8
"""
Name:  Shilo S Wilson

Exercise: 1.4.5

 Create any code that demonstrates usage of the abs function.

"""

import numpy as np


def AverageDeviation(container):
    """
    A function which computes the average deviation
    :param container: list
    :return: float
    """
    avg = sum(container)/ len(container)
    avg_dev = 0
    for i in container:
        avg_dev += abs((i-avg)/len(container))
    return(avg_dev)

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



    print 'The average deviation from the mean is {}'.format(AverageDeviation(mortgages))

if __name__ == '__main__':
    main()