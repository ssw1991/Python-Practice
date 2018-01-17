# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: wilso

Exersize 1.2.3

Create a list of all even integers 1-1000. Write a loop that prints all numbers in the above list, separated by commas.  
 
"""

import sys


def main():
    
    print('============= Exersize 1.2.3 =============\n\n\n')
    
    myEvenlst = [2*i for i in range(501)]
    
    # This would be simpler, but assignment required loop
    
    # print ', '.join(str(i) for i in myEvenlst)
    
    for i in myEvenlst[:-1]:
        
        # Not writing last element as I do not want it to have trailing comma
        # Using sys.stdout because it prints at last place, print statement adds new line
        
        sys.stdout.write(str(i)+', ')
    sys.stdout.write(str(myEvenlst[-1]))
    
if __name__ == '__main__':
    main()


        