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
    
    base = None
    height = None
    
    while not base:    
        try:
            base = float(raw_input('Please enter the base of your triange: '))
        except:
            print('The base was non-numeric, please try again')
             
    while not height:  
        try:
            height = float(raw_input('Please enter the height of your triangle: '))
        except:
            print('The height was non-numeric, please try again')
    # Using 2.0 to prevent type being casted from float to int\
    area = base*height/2.0
    print('The area of the triange is ' + str(area))
    
    
  
        
        
if __name__ =='__main__':
    main()
