# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: Shilo S Wilson

Exersize 1.3.5


 Create a function that calculates the variance of a passed-in list, with degree of freedom parameter
 
 
 
"""


def mean(container):
    """
    Returns mean of passed in list

    """
    return sum(container) / len(container)


def var(container, degOfFreedom = 1):
    
    """
    Returns Variance of passed in list
    
    """
    avg = mean(container)
    deviation = 0

    for i in container:
        deviation += (i - avg)**2/float(len(container) - degOfFreedom)
    return(deviation)

        


def main():
    
   print('============= Exercise 1.3.5 =============\n\n\n')
    
   print var([1,3,5])
   print var([1,3,5], 0)
    
if __name__ == '__main__':
    main()