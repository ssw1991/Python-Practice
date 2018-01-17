# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: wilso

Exersize 1.2.5

Create an aggregate list from 3) and 4) and print it out, separated by commas.
 
"""

import sys


def main():
    
    print('============= Exersize 1.2.5 =============\n\n\n')
    
    myOddlst = [2*i+1 for i in range(500)]
    myEvenlst = [2*i for i in range(500)]
    
    myLst = myEvenlst + myOddlst
    
    # This Problem did not require a loop
    
    print ', '.join(str(i) for i in myLst)
    
   
    
if __name__ == '__main__':
    main()


        