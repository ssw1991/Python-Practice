# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: wilso

Exersize 1.3.2


 Write a function that returns the Fibonacci sequence as a list. 
 The function should take a parameter called N and return the entire sequence of Fibonaccis, from 0-N. 
 You may use either iterative or recursive programming techniques (bonus if you implement both!). 
 
 
 
"""



def fib_iterative(N):
    
    """
    Returns list of fibonacci using an iterative approach
    
    """
    fibs = []
    
    for i in range(N):
        if i <=1:
            fibs.append(1)
        else:
            fibs.append(fibs[-2]+fibs[-1])
            
    return(fibs)


        


def main():
    
   print('============= Exersize 1.3.2 =============\n\n\n')
    
   print fib_iterative(5)
  
    
if __name__ == '__main__':
    main()


        