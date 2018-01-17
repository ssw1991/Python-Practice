# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: wilso

Exersize 1.2.9


9) Create a list of names, and a second list of ages which correspond to a name in the first list: 
    a. Zip them together and print the result. 
    b. Using a list comprehension, create a list that contains all the names for which the corresponding age is greater than or equals to 18. 
    (Hint: Use zip as necessary. Can you also do this without zip? Which is better?). 
  
 
"""




def main():
    
    print('============= Exersize 1.2.9 =============\n\n\n')
    
    names = ['James', 'John', 'Jack', 'Bill','Terry','Tim','Tom','Sam','Derick','Tony']
    ages =  [9,15,18,21,23,21,23,15,25,76]
    
    ages_name = zip(names,ages)
       
    
    """
    above_18 = []
    for i in range(len(names)):
        if ages[i] >=18:
            above_18.append(names[i])
    
    This method is both more verbose and and error prone (if list arent same length) than using zip and list comprehension
    """
    
    above_18 = [j[0] for j in ages_name if j[1] >= 18]
    
    print 'The following athletes are 18 and above\n'
    print ', '.join(str(o) for o in above_18)
   
    
if __name__ == '__main__':
    main()


        