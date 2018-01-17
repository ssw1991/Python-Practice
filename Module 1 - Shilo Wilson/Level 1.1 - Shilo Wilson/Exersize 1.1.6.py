# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 16:26:01 2017

@author: Shilo S Wilson

Exersize 1.1.6

Create a program that takes input from a user and stores it in a variable, then displays the input variable to the user

"""



def main():
    print('=========== Exersize 1.1.6 ===========' )
    
    myVar = input('Please enter a value: ')
    
    print('The value you entered was: ' + str(myVar))
    
    if type(myVar) == float or type(myVar)==int:    
        
        print('The inputted value is a number.')
        
        if myVar < 64:
             print('The inputted number is less than 65')
             
        elif 64<= myVar <= 65:
            # I made it inclusive to ensure output
            print('The inputted number is between 64 and 65')
            
        else: 
            # The homework assignment reads 'the inputted number is greater than 64, however given the context of this assingment I assumed that to be a typo
            print('The inputted number is greater than 65')
            
    elif type(myVar) == str:
        print('The inputted value is a string')
        
    else:
        print('The inputted value is neither a number nor a string')
        
        
if __name__ =='__main__':
    main()
