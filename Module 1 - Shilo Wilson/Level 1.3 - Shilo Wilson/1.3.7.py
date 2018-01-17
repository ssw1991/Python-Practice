# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: Shilo S Wilson

Exersize 1.3.7


 Write a function that takes name, age as parameters.
 It should also take **kwargs. The function should display the name, age, and any of ‘state’, ‘height’, and ‘weight’
 that happen to exist in the kwargs. Call the function with names, ages, and different combinations of keyword arguments
 (state, height, weight, hairColor, etc.).
 
 
 
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

    lst = ['state','height', 'weight']
    for i in kwargs:
        if i in lst:
            print i + ': ' + str(kwargs.get(i))
    print('\n')



def main():
    
   print('============= Exercise 1.3.7 =============\n\n\n')
    
   description('Jack',15,height = 70, weight = 130, state = 'Colorado')
   description('Jack2', 15, height = 70)
   description('Jill', 15, hairColor = 'blue')

    
if __name__ == '__main__':
    main()