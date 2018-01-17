# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: wilso

Exersize 1.3.1


 Write a function that can print out the day of the week for a given number. 
 I.e. Sunday is 1, Monday is 2, etc. It should return a tuple of the original number and the corresponding name of the day. 
 
 
 
"""



def weekday(num):
    
    """
    Takes a number 1 - 7 returns tuple(weekday, number) in data types tuple(<str>,<int>)
    
    """
    
    days = {1:'Sunday',
            2: 'Monday',
            3: 'Tuesday',
            4: 'Wednesday',
            5: 'Thursday',
            6: 'Friday',
            7:'Saturday'}
    
    try:
        return (days[num], num)
    except:
        print 'The number {} does not correspond to a day'.format(str(num))
        

def main():
    
   print('============= Exersize 1.3.1 =============\n\n\n')
    
   for i in range(1,9):
       print(weekday(i))
    
if __name__ == '__main__':
    main()


        