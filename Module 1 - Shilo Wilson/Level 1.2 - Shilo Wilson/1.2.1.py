# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: wilso

Exersize 1.2.1 

Write a program that does the following: 
    a. Keeps asking the user for a number, until the user enters the letter s. 
    b. Once the user finishes entering numbers, calculate and display the average of the numbers. You should do this using a loop. 
 
"""

def main():
    
    user_stop = None
    lst = []
    
    while not user_stop:
        val = raw_input('Please enter a number, enter "s" to quit: ')
        
        if val =='s':
            #Test for exit condition
            user_stop = True
        else:
            try:
                #Test the entry is valid
                lst.append(float(val))
            except:
                # Print error message
                print('Entry not valid')
    # Using loop to compute average

    avg = 0
    for i in range(len(lst)):
        avg+= lst[i]/len(lst)
    print('The average is ' + str(avg))
    
    
if __name__ == '__main__':
    main()


        