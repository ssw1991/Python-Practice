"""
Author: Shilo Wilson

5) The previous exercise presents a good use-case for functools.partial:
    a. Create a partial called reconcileListsBreakAbsolute (which uses the breakAbsolute function). Test this comprehensively.
    b. Create similar partial functions for each of the break* functions in the previous exercise
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
    print('========== Exercise 3.1.5 ==========')

    print('Testing when equal')
    a = 6
    b = 6

    print('Testing absolute difference: {}'.format(breakAbs_5(a, b)))
    print('Testing relative difference: {}'.format(breakRel_5(a, b)))
    print('Testing absolute relative difference: {}'.format(breakAbsRel_5(a, b)))

    print('Testing at breakpoint')
    a = 100
    b = 105

    print('Testing absolute difference: {}'.format(breakAbs_5(a, b)))
    print('Testing relative difference: {}'.format(breakRel_5(a, b)))
    print('Testing absolute relative difference: {}'.format(breakAbsRel_5(a, b)))

    print('Testing inside breakpoint')
    a = 100
    b = 104

    print('Testing absolute difference: {}'.format(breakAbs_5(a, b)))
    print('Testing relative difference: {}'.format(breakRel_5(a, b)))
    print('Testing absolute relative difference: {}'.format(breakAbsRel_5(a, -1*b)))

    print('Testing at outside')
    a = 100
    b = 106

    print('Testing absolute difference: {}'.format(breakAbs_5(a, b)))
    print('Testing relative difference: {}'.format(breakRel_5(a, b)))
    print('Testing absolute relative difference: {}'.format(breakAbsRel_5(a, -1*b)))

    print('Testing with 0, I except this to throw an error on percent change.  Because of this '
          'I think these functions should be written with def instead of lambda')
    a = 100
    b = 0
    try:
        print('Testing absolute difference: {}'.format(breakAbs_5(a, b)))
    except Exception as e:
        print(e.message)
    try:
        print('Testing relative difference: {}'.format(breakRel_5(a, b)))
    except Exception as e:
        print(e.message)
    try:
        print('Testing absolute relative difference: {}'.format(breakAbsRel_5(a, b)))
    except Exception as e:
        print(e.message)


if __name__ == '__main__':
    main()