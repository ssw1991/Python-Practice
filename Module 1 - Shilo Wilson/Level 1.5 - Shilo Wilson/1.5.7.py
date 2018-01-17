# coding=utf-8
"""
Name:  Shilo S Wilson

Exercise: 1.5.7

Extend the mortgage function to return a dict of address:mortgage. For simplicity, address should be a unique
six-character string. For example {‘867E23’ : 120}. Once you have done this, modify the filtering code from 1.4.1
to do the following:
    a. Provide three separate dicts, filtered the same way as problem 1).
    b. Modify one value in the jumboMortgages dict. Check the original dict; did it remain intact or change? Why?
    c. Extract the lists of amounts from each separate dict. Modify one value in the miniMortgages list.
    Does the miniMortgages dict change? How about the original dict? Why?

"""
import random
import string
import numpy as np
from copy import deepcopy as deepcopy

def Mortgages(N):
    """
    A function that returns an unsorted list of mortgage amounts

    :param N:
    :return:

    """

    return list(np.random.random_integers(100,1000,size = N))



def main():

    print('============= Exercise 1.5.7 =============\n\n\n')

    mortgages = Mortgages(1000)
    miniMortgages = filter(lambda x: x < 200, mortgages)
    standardMortgages = filter(lambda x: 200 <= x <= 467, mortgages)
    jumboMortgages = filter(lambda x: x > 467, mortgages)

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
    """
    Going too create dicts from the mortgages lists
    
    """
    mortgage_dict = {keys[i]: mortgages[i] for i in range(len(mortgages))}

    mini_dict = {k:v for k,v in mortgage_dict.iteritems() if v < 200}
    standard_dict = {k:v for k,v in mortgage_dict.iteritems() if 200<=v <= 467}
    jumbo_dict = {k:v for k,v in mortgage_dict.iteritems() if v > 467}

    """
    Create test dicts to check for equivalence after changing the original dicts
    """
    test_mort = deepcopy(mortgage_dict)
    test_mini = deepcopy(mini_dict)


    mini_vals = list(mini_dict.itervalues())
    standard_vals = list(standard_dict.itervalues())
    jumbo_vals = list(jumbo_dict.itervalues())
    all_vals = list(mortgage_dict.itervalues())

    # getting a key to change in jumbodict
    jumbo_key = list(jumbo_dict.iterkeys())[0]
    jumbo_dict[jumbo_key] = 1
    print jumbo_key,jumbo_dict[jumbo_key]


    print mortgage_dict == test_mort
    # This is true, implying that the original dict was not changed


    mini_vals = list(mini_dict.itervalues())
    mini_vals[0] = 10000

    print mini_dict == test_mini
    print mortgage_dict == test_mort
    #  These are both true, implying the dicts were not changed

    standard_vals = list(standard_dict.itervalues())
    jumbo_vals = list(jumbo_dict.itervalues())
    all_vals = list(mortgage_dict.itervalues())


if __name__ == '__main__':
    main()