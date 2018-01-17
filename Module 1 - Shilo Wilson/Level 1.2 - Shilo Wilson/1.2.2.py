# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: wilso

Exersize 1.2.2 

Create a list of ten numbers. Should contain some integers and some decimals. Perform the following operations: 
    a. Display the first two numbers from the list (using indexing). 
    b. Display the last two numbers. 
    c. Display all the numbers besides the last number, using a single print statement. 
    d. Display all the numbers besides the first number, using a single print statement. 
    e. Display all the numbers besides the first two and last three numbers, using a single print. 
    f. Append one number to the end of the list. 
    g. Append five numbers to the end of the list, using a single operation. 
    h. Insert one number right after the third number in the list. 
    i. Modify the fourth-to-last number in the list. 
    j. Display the list backwards, using splicing. 
    k. Display every second item in the list. 
    l. Display every second item in the list, backwards.  
 
"""



def main():
    
    myLst = [4,5,3,8.2,5.3,7.6,9,10,23,45]
    
    #a. Display the first two numbers from the list (using indexing).
    
    print(myLst[0:2])
    
    #b. Display the last two numbers.
     
    print(myLst[-2:])
    
    #c. Display all the numbers besides the last number, using a single print statement. 
    
    print(myLst[:-1])
    
    #d. Display all the numbers besides the first number, using a single print statement.
    
    print(myLst[1:])
    
    #e. Display all the numbers besides the first two and last three numbers, using a single print. 
    
    print(myLst[2:-3])
    
    #f. Append one number to the end of the list. 
    
    myLst.append(17)
    
    #g. Append five numbers to the end of the list, using a single operation. 
    
    myLst.extend([3,2,5,12.3,21])

    #h. Insert one number right after the third number in the list. 
    
    myLst.insert(3,69)
    
    #i. Modify the fourth-to-last number in the list. 
    
    myLst[-4] = 17.4
    
    #j. Display the list backwards, using splicing. 
    
    print(myLst[::-1])
    
    #k. Display every second item in the list. 
    
    print(myLst[0::2])
    
    #l. Display every second item in the list, backwards.  
    
    print(myLst[::-2])
    
if __name__ == '__main__':
    main()


        