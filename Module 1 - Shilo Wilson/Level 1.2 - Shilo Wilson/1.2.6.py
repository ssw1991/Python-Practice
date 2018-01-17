# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: wilso

Exersize 1.2.6

Print out the aggregate list from 5), backwards and separated by commas. 
 
"""

import sys


def main():
    
    print('============= Exersize 1.2.6 =============\n\n\n')
    
    myOddlst = [2*i+1 for i in range(500)]
    myEvenlst = [2*i for i in range(500)]
    
    # Per assignment
    #myLst = myEvenlst + myOddlst
    
    # This loop will ensure the numbers are in order
    
    myLst = []
    for i,v in enumerate(myEvenlst):
        myLst.extend([myEvenlst[i],myOddlst[i]])
        
    # This Problem did not require a loop
    
    print ', '.join(str(i) for i in myLst[::-1])
    
   
    
if __name__ == '__main__':
    main()


        