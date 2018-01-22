"""
Jan 14, 2018
Author: Shilo Wilson

2) This exercise is a modification of Exercise 1.5.8, to use the reduce function. To this end, create a list of loan
terms and a list of rates:
    a. Use the reduce function, with a regular function as its callable, to calculate the WAM of the list of terms.
    b. Use the reduce function, with a lambda as its callable, to calculate the WAR of the list of rates.
    c. Modify your WAR and WAM functions in your LoanPool class to use the above code.

8) Modify the dict from 7) to be a dict of address keys and the following tuple as value: (amount, rate, term in months).
Amount should now be between 100,000 and 1,000,000. Once you have done this, do the following:
    a. Extract a list of tuple values from the dict, and sort the list by amount (descending).
    b. Create a function that calculates the Weighted Average Rate of the mortgage pool. The input parameter should be a
     list of mortgage tuples (amount,rate,term). Print the rate percentage, rounded to the nearest hundredths.
    c. Create a function that calculates the Weighted Average Maturity (term) of the mortgage pool. The input parameter
     should be a list of mortgage tuples (amount,rate,term). d. Create a new dict (by processing the original dict) with
     Term as the key and a list of (amount, rate) tuples for each Term key

"""

import random
import string
import numpy as np

from assets.Car.Car import Civic as Civic
from assets.Car.Car import Lexus as Lexus
from assets.House.HouseBase import PrimaryHome as Primary
from assets.House.HouseBase import VacationHome as Vacation
from loan import LoanPool as LoanPool
from MortgageMixin import FixedRateMortgage
from loan import FixedAutoLoan

def WAM(prev, x):
    """
    Computes the weighted average maturity
    :param x: <list> [<tuple>(<int> amount,<float> rate, <term>
    :return: Weighted average maturity
    """
    wam = prev + (x[0] * float(x[2]))
    return wam


WAR = lambda prev, (x, y, z): prev + x*y


def Mortgages(N):
    """
    A function that returns an unsorted list of mortgage amounts

    :param N:
    :return:

    """

    return list(np.random.random_integers(100000,1000000,size = N))

def main():
    print ('========== Exercise 3.1.2 ==========\n')
    mortgages = Mortgages(1000)
    # Generating random values for rate and term ( not realistic just for purposes of this exersice)
    rates = list(np.random.uniform(.01, .07, 1000))

    # Terms will be between 15 and 45

    terms = list(np.random.random_integers(1, 3, 1000) * 15)

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

    sorted_morts = sorted(mortgage_dict.itervalues(), key=lambda x: x[0])
    total_val = reduce(lambda sum, (x, y, z): sum+float(x), sorted_morts, 0)

    weighted_return = reduce(WAR, sorted_morts, 0) / total_val
    weighted_mat = reduce(WAM, sorted_morts, 0) / total_val

    print('WAR is: {}'.format(weighted_return))
    print('WAM is: {}'.format(weighted_mat))
    myHome = FixedRateMortgage(Primary(200000), 360, .045, 200000)
    myVacation = FixedRateMortgage(Vacation(300000), 180, .055, 300000)
    myCivic = FixedAutoLoan(Civic(20000), 48, .075, 20000)
    myLexus = FixedAutoLoan(Lexus(35000), 72, .075, 40000)

    loanpool = LoanPool([myHome, myVacation, myCivic, myLexus])

    print('WAR is: {}'.format(loanpool.WAR()))
    print('WAM is: {}'.format(loanpool.WAM()))





if __name__ == '__main__':
    main()