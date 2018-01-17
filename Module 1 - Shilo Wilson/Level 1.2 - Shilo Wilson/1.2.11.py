# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: wilso

Exersize 1.2.11


11) Create a list of lists of any type. Use the double list-comprehension syntax, as described in the lecture, to create a flattened single list. 
Note that this can be useful in situations where one has a function that returns a list of items, and calls the function many times, 
resulting in a large list of lists (which can then be flattened, for simplicity). 
 
 
 
"""




def main():
    
   print('============= Exersize 1.2.11 =============\n\n\n')
    
   lst_o_lst = [[1,2],[3,4],[5,6]] 

   flattened = [i[j] for i in lst_o_lst for j in range(len(i))] 
   
   print flattened
    
if __name__ == '__main__':
    main()


        