# coding=utf-8
"""
Name:  Shilo S Wilson

Exercise: 1.4.1

You are a lender, holding onto a large number of mortgages. Create code that does the following:
    a. A function that returns an unsorted list of mortgage amounts, in thousands. Numbers should range from 100 to 1,000
    and do not need to all be unique.

    b. Filter the result of a) into three lists: Amounts below 200, amounts between 200 and 467, and amounts greater than 467.
    Call these ‘miniMortgages’, ‘standardMortgages’, and ‘jumboMortgages’ respectively.

    c. Use the all function with an if statement to verify that the resulting lists of b) indeed contain only numbers
    within the specified ranges.

    d. Use the any function with an if statement to verify that the resulting lists of b) indeed contain only numbers
    within the specified ranges.

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
    print('============= Exercise 1.4.1 =============\n\n\n')

    mortgages         = Mortgages(1000)
    miniMortgages     = filter(lambda x: x<200,mortgages)
    standardMortgages = filter(lambda x: 200<=x<=467,mortgages)
    jumboMortgages    = filter(lambda x: x>467,mortgages)

    # Should all come up true

    print all(i< 200 for i in miniMortgages)
    print all(200<=i<=467 for i in standardMortgages)
    print all(i > 467 for i in jumboMortgages)

    # Should all come up false

    print any(i >= 200 for i in miniMortgages)
    print any(200 > i or i > 467 for i in standardMortgages)
    print any(i <= 467 for i in jumboMortgages)


if __name__ == '__main__':
    main()