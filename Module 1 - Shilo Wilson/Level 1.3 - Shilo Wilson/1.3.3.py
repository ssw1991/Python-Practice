# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: wilso

Exersize 1.3.3


 Create a function that calculates the mean of a passed-in list
 
 
 
"""



def mean(container):
    
    """
    Returns mean of passed in list
    
    """
    avg = 0
    
    for i in container:
        avg+=i/float(len(container))
    return(avg)

        


def main():
    
   print('============= Exersize 1.3.3 =============\n\n\n')
    
   print mean([1,3,5])
  
    
if __name__ == '__main__':
    main()


        