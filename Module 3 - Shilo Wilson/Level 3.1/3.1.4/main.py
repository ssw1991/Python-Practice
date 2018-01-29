"""
Author: Shilo Wilson
4) To incorporate lambda into the previous exercise, do the following:
    a. Create a breakAbsolute stored lambda which takes two values and an epsilon parameter. This lambda should 'return'
    True if the two values are not within epsilon of each other.
    b. Create a breakRelative stored lambda which takes two values and a percent parameter. This lambda should 'return'
    True if the percent difference between the two values exceeds percent.
    c. Create a breakAbsRelative function which takes two values and a percent parameter. This should return True if the
    percent difference between the absolute values of the two values exceeds percent.
    d. Modify the reconcileLists function to take a third parameter, called breakFn (this represents a passed-in
    function or lambda).
    The reconcileLists function should utilize the passed-in breakFn function to build the True/False list. You will
    need to use functools.partial to specify the parameter of the breakFn function (i.e., epsilon or percent).
    e. Test reconcileLists with different lists of values (should be large lists of numbers) and with each of the above
    break* functions.
"""
from functools import partial

def reconcileList(l1, l2, brkFn):
    """
    Returns a list of booleans indicating whether l1[n] = l2[n]
    If l1 and l2 are different lengths, raises an exception
    :param l1: List
    :param l2: List
    :param brkFn: Partial function with difference parameter set
    :return: List
    """
    if len(l1) != len(l2):
        raise Exception('The length of the input arguments do not match!')
    return map(lambda (x, y): brkFn(x, y), zip(l1, l2))


breakAbsolute = lambda x, y, z: abs(x - y) < z
# For breakRelative, to be consistant I will always use minimum as base for % change
# For relative function, must be careful of integer division
breakRelative = lambda x, y, z: abs((max(x, y) - min(x, y)) / min(x, y)) < z
breakAbsRelative = lambda x, y, z: (max(abs(x), abs(y)) - min(abs(x), abs(y))) / min(abs(x), abs(y)) < z


breakAbs_5 = partial(breakAbsolute, z=5)
breakRel_5 = partial(breakRelative, z=.05)
breakAbsRel_5 = partial(breakAbsRelative, z=.05)


def main():
    print('========== Exercise 3.1.4 ==========')

    l1 = [100., 300., 500., 600., 300., 400., 500., 700., 500., 200., 300., 500.]
    l2 = [100., 315., 502., 600., 314., 479., -503., 734., 525., 200., 306., 504.]
    l3 = [1, 4, 5]

    print('Testing Break Absolute at 5: {}'.format(reconcileList(l1, l2, breakAbs_5)))
    print('Testing Break relative at 5 percent: {}'.format(reconcileList(l1, l2, breakRel_5)))
    print('Testing Break absolute relative at 5 percent: {}'.format(reconcileList(l1, l2, breakAbsRel_5)))


if __name__ == '__main__':
    main()