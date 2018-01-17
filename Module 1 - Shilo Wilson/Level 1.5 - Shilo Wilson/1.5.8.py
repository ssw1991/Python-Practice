# coding=utf-8
"""
Name:  Shilo S Wilson

Exercise: 1.5.8

Modify the dict from 7) to be a dict of address keys and the following tuple as value: (amount, rate, term in months).
Amount should now be between 100,000 and 1,000,000. Once you have done this, do the following:
    a. Extract a list of tuple values from the dict, and sort the list by amount (descending).
    b. Create a function that calculates the Weighted Average Rate of the mortgage pool. The input parameter should be a
    list of mortgage tuples (amount,rate,term). Print the rate percentage, rounded to the nearest hundredths.
    c. Create a function that calculates the Weighted Average Maturity (term) of the mortgage pool. The input parameter
    should be a list of mortgage tuples (amount,rate,term).
    d. Create a new dict (by processing the original dict) with Term as the key and a list of (amount, rate) tuples for each Term key.

"""
import random
import string
import numpy as np
from copy import deepcopy as deepcopy


def WAR(mortgage_tuples):
    """
    Computes the weighted average rate
    :param mortgage_tuples: <list> [<tuple>(<int> amount,<float> rate, <term>
    :return: Weighted average rate
    """

    total_val = sum([float(i[0]) for i in mortgage_tuples])
    war = 0

    for i in mortgage_tuples:
        war += (i[0] * i[1]) / total_val
    return war


def WAM(mortgage_tuples):
    """
    Computes the weighted average maturity
    :param mortgage_tuples: <list> [<tuple>(<int> amount,<float> rate, <term>
    :return: Weighted average maturity
    """

    total_val = sum([float(i[0]) for i in mortgage_tuples])
    wam = 0

    for i in mortgage_tuples:
        wam += (i[0] * float(i[2])) / total_val

    return wam

def Mortgages(N):
    """
    A function that returns an unsorted list of mortgage amounts

    :param N:
    :return:

    """

    return list(np.random.random_integers(100000,1000000,size = N))



def main():

    print('============= Exercise 1.5.8 =============\n\n\n')

    mortgages = Mortgages(1000)

    # Generating random values for rate and term ( not realistic just for purposes of this exersice)
    rates = list(np.random.uniform(.01,.07,1000))

    # Terms will be between 15 and 45

    terms = list(np.random.random_integers(1,3,1000)*15)

    mort_tuples = zip(mortgages, rates, terms)


    """
    Generating unique keys 
    
    """
    keys = []
    for i in range(len(mortgages)):
        k = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(6))

        if k not in keys:
            keys.append(k)
        else:
            random.choice()
            while k in keys:
                k = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(6))
                if k not in keys:
                    keys.append(k)

    # Create the dict
    mortgage_dict = {}
    for i in range(len(mortgages)):
        mortgage_dict[keys[i]] = mort_tuples[i]

    sorted_morts = sorted(mortgage_dict.itervalues(), key =lambda x: x[0])

    weighted_return = WAR(sorted_morts)*100
    weighted_mat = WAM(sorted_morts)


    print 'The weighted average return is {0:.2f}%, the weighted average maturity is {1:.2f}'.format(weighted_return, weighted_mat)

    term_dict = {}

    for i in mortgage_dict:
        if mortgage_dict[i][2] not in term_dict:
            term_dict[mortgage_dict[i][2]] = [tuple(mortgage_dict[i][0:-1])]
        else:
            term_dict[mortgage_dict[i][2]].append(tuple(mortgage_dict[i][0:-1]))
    print term_dict[15]
    
if __name__ == '__main__':
    main()