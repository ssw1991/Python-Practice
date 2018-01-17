# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: wilso

Exersize 1.2.10


10) Write a list comprehension that results in a list of all numbers 0 through 10,000,000. 
    a. Using a loop, filter the resulting list, to create another list that only contains numbers ending with the digit 0. 
    b. Do the same as a) using a list comprehension. 
    Use the time.time function to capture the time taken for each version. Which is quicker? Why  
 
"""

import time


def main():
    
    print('============= Exersize 1.2.10 =============\n\n\n')
    
    numbers = [i for i in range(10000001)]
    div_10_loop = []
    
    
    start = time.time()
    
    for i in numbers:
        if i%10 ==0:
            div_10_loop.append(i)
    loop_time = time.time() - start
                         
    start = time.time()

    div_10_comp = [i for i in numbers if i%10==0]
    
    comp_time = time.time() - start 
                         
    print 'It took {0:.10f} seconds for the loop to complete, and {0:.10f} seconds for the list comprehension to complete.'.format(loop_time,comp_time)
    
        
    """
    On my computer both are running the at the same speed
    """
    
if __name__ == '__main__':
    main()


        