# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:23 2017

@author: wilso

Exersize 1.2.8


Create two lists: 
    The first list should be called ‘players’, and contain at least ten unique names. 
    The second list should be called ‘injured_players’, and contain a few names of players from the first list. 
    Create a list comprehension which results in a list containing all active (non-injured) players. 
  
 
"""




def main():
    
    print('============= Exersize 1.2.8 =============\n\n\n')
    
    names = ['James', 'John', 'Jack', 'Bill','Terry','Tim','Tom','Sam','Derick','Tony']
    injured = ['John','Terry','Tim']
    
    non_injured = [i for i in names if i not in injured]
    
    
    print 'The following players are not injured\n'
    
    print ', '.join(str(o) for o in non_injured)
   
    
if __name__ == '__main__':
    main()


        