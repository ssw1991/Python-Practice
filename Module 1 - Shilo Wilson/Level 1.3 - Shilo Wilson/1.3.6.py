# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: Shilo S Wilson

Exersize 1.3.6


 Create a function that calculates the mean using args
 
 
 
"""


def argMean(*args):
    """
    Returns mean of passed in list

    """
    avg = 0

    for i in args:
        avg += i / float(len(args))
    return (avg)



        


def main():
    
   print('============= Exercise 1.3.6 =============\n\n\n')
    
   print argMean(1,3,5)

    
if __name__ == '__main__':
    main()