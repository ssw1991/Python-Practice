# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 16:26:01 2017

@author: Shilo S Wilson

Exersize 1.1.6

Create a program that computes the area of a triangle

"""



def type_test(val):
    """
    Test if the input value is numeric, returns boolean
    
    """
    
    if type(val) == int or type(val) == float:
        return(True)
    else :
        return(False)

def main():
    print('=========== Exersize 1.1.7 ===========' )
    
    b = None
    h = None
    
    while not b:    
        base = input('Please the base of your triangle: ')
        b = type_test(base)
        if not b:
             print('The base was non-numeric, please try again')
             
    while not h:    
        height = input('Please enter the height of your triangle: ')
        h = type_test(height)
        if not h:
            print('The height was non-numeric, please try again')
    # Using 2.0 to prevent type being casted from float to int\
    area = base*height/2.0
    print('The area of the triange is ' + str(area))
    
    
  
        
        
if __name__ =='__main__':
    main()
