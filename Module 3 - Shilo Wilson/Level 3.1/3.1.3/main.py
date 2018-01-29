"""
Author: Shilo Wilson

 Create a regular function (called reconcileLists) that takes two separate lists as its parameters. In this example,
 List 1 represents risk valuations per trade (i.e. Delta) from Risk System A and List 2 has the same from Risk System B.
 The purpose of this function is to reconcile the two lists and report the differences between the two systems.
 To this end, it should return a list of True or False values, corresponding to each value in the lists (True means they
 match at index, False means they don't match at index).
Test the reconcileLists function with different lists of values (
lists should be of at least length ten). Note that the
assumption is that both lists are the same length (report an error otherwise).
"""


def reconcileList(l1, l2):
    """
    Returns a list of booleans indicating whether l1[n] = l2[n]
    If l1 and l2 are different lengths, raises an exception
    :param l1: List
    :param l2: List
    :return: List
    """
    if len(l1) != len(l2):
        raise Exception('The length of the input arguments do not match!')
    return map(lambda (x, y): x == y, zip(l1, l2))


def main():
    print('========== Exercise 3.1.3 ==========')

    l1 = [1, 3, 5, 6, 3, 4, 5, 7, 5, 2, 3, 5]
    l2 = [1, 4, 5, 6, 9, 4, 5, 7, 5, 2, 3, 5]
    l3 = [1, 4, 5]

    try:
        print reconcileList(l1, l2)
    except Exception as e:
        print e.args
        
    try:
        print reconcileList(l1, l3)
    except Exception as e:
        print e.args

if __name__ == '__main__':
    main()