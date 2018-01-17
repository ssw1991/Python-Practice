# coding=utf-8
"""
Name:  Shilo S Wilson

Exercise: 1.5.5

 Create a simple dictionary that has country name as the key and population as the value (country:population).
 Do this for at least ten countries. Then, do the following:
    a. Create code that prompts the user for the name of a country (‘0’ to exit).
        Display the population for that country. Repeat until the user enters ‘0’.
        If the country does not exist in the dict:
            i. Display a message to the user that the population is unknown and prompt the user to enter the population.
            ii. Update the dict with the value provided by the user.
     Display the final dict once the user exits the loop. Display should be in the format:
     Country 1 has population X Country 2 has population Y

     c. Note that the above display will not necessarily be sorted.
     Modify the code from part b to display sorted by
     1) country then 2) population, largest first (Hint: Use the sorted function).
"""


import numpy as np

def print_dict(pairs):
    for pair in pairs:
        print '{} has population {}'.format(pair[0],str(pair[1]))



def main():

    print('============= Exercise 1.5.5 =============\n\n\n')

    population = {
                    'United States':323,
                    'Canada':36,
                    'Mexico':127,
                    'Columbia':129,
                    'Brazil':202,
                    'UK':65,
                    'Ireland':4,
                    'Angola':21,
                    'Thailand':65,
                    'Australia':24
                    }
    entry = True

    while entry:
        entry = raw_input('Please enter the name of a country.  Press 0 to exit: ')

        # Test if entry is '0' sets entry to int 0, then exits iteration.  because entry is 0 loop will exit
        if entry == '0':
            entry = int(entry)
            continue

        try:
            print 'The population of {} is {} million'.format(entry,str(population[entry]))
        except:
            pop = int(raw_input('We do not have population data for that country.  Please enter the population: '))
            population[entry] = pop

    print_dict(population.iteritems())
    print_dict(sorted(population.iteritems(), key = lambda x: x[0]))
    print_dict(sorted(population.iteritems(), key=lambda x: x[1], reverse = True))

if __name__ == '__main__':
    main()