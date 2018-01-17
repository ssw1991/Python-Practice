# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: wilso

Exersize 1.2.7


7) Write a list comprehension that results in a list of the squares of all numbers 0 through 100: 
    a. Filter the resulting list, to create another list that only contains numbers greater than 1000. 
    b. Filter further, to create another list that only contains even numbers (hint: use the Modulus operator). 
 
"""




def main():
    
    print('============= Exersize 1.2.7 =============\n\n\n')
    
    myLst = [i**2 for i in range(101)]
    
    myBigLst = [i for i in myLst if i>1000]
    
    myEvenlst = [i for i in myLst if i%2==0]
    
    print('List of squares\n')
    print ','.join(str(o) for o in myLst)
    
    print('\nList of squares larger than 1000\n')
    print ','.join(str(o) for o in myBigLst)
    
    print('\nList of squares that are even\n')
    print ','.join(str(o) for o in myEvenlst)
   
    
if __name__ == '__main__':
    main()


        