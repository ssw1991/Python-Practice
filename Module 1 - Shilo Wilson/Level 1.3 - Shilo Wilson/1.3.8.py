# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: Shilo S Wilson

Exercise 1.3.7


Extend 1.3.8 to print all **kwargs
 
 
"""


def description(name, age, **kwargs):
    """

    :param name: String
    :param age: Integer
    :param kwargs: State, Height and Weight
    :return: None

    """

    print 'name: ' + name
    print 'age: ' + str(age)


    for i in kwargs:
        print i + ': ' + str(kwargs.get(i))
    print('\n')



def main():
    
   print('============= Exercise 1.3.8 =============\n\n\n')
    
   description('Jack',15,height = 70, weight = 130, state = 'Colorado')
   description('Jack2', 15, height = 70)
   description('Jill', 15, hairColor = 'blue')

    
if __name__ == '__main__':
    main()