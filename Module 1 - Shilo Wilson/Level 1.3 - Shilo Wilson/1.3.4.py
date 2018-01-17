# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: Shilo S Wilson

Exersize 1.3.4


 Create a function that calculates the variance of a passed-in list
 
 
 
"""


def mean(container):
    """
    Returns mean of passed in list

    """
    avg = 0

    for i in container:
        avg += i / float(len(container))
    return (avg)


def var(container):
    
    """
    Returns Variance of passed in list
    
    """
    avg = mean(container)
    deviation = 0

    for i in container:
        deviation += (i - avg)**2/float(len(container))
    return(deviation)

        


def main():
    
   print('============= Exercise 1.3.4 =============\n\n\n')
    
   print var([1,3,5])

    
if __name__ == '__main__':
    main()