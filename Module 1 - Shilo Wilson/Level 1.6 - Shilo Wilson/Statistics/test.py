# coding=utf-8
"""
Name:  Shilo S Wilson

Exercise: 1.6.2

Create a package

"""

import estimators
from estimators.summary.summary.variance import variance as variance
from estimators.summary.summary.mean import mean as mean
from estimators.summary.summary_func import summary_sample as sampsum
import estimators.output as output
import estimators.args.summary.functions as argSum
import estimators.args.output
def main():

    print('============= Exercise 1.6.2 =============\n\n\n')

    a = mean([1, 2, 3])
    print a
    a = variance([1,2,3])
    print a
    print sampsum([1,2,3])
    output.output([1,2,3])
    print argSum.mean(1,2,3)
    print argSum.variance_sample(1,2,3)
    estimators.args.output.output(1,2,3)

if __name__ == '__main__':
    main()




