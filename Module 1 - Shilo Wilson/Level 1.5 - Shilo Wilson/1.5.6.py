# coding=utf-8
"""
Name:  Shilo S Wilson

Exercise: 1.5.6

Create the mode function, building off the frequency function that was demonstrated in the lecture.
The function should return a tuple, containing a list of mode values (containing one or more items) and their frequency.
Be sure to fully test it.
"""

import numpy as np

def freqMap(values):
    """
    Returns a map of value : frequency
    :param values: list or tuple of values
    :return: dict {value: frequency}
    """
    map = {}

    for v in values:
        if not map.get(v):
            map[v]=1
        else:
            map[v] += 1

    return map

def mode(values):
    """
    Takes a list of values, returns the a tuple ([mode values], frequency)
    :param values: container
    :return: <tuple> (<list> mode values, <int> frequency)
    """
    freq = freqMap(values)
    m = max(freq.values())
    lst = []
    for k in freq:
        if freq[k] == m:
            lst.append(k)
    return (lst, m)



def main():

    print('============= Exercise 1.5.6 =============\n\n\n')

    lst = np.random.binomial(1000,.5, 10000)

    print mode(lst)
    print mode([1,1,1,1,2,2,2,2,4,5,6,7,8,0])

if __name__ == '__main__':
    main()