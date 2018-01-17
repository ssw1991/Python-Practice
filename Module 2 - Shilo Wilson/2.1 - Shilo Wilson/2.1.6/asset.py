"""
Author: Shilo Wilson

6)	Create a class called Asset. This class will represent the Asset covered by the loan. The class should do the following:
a.	Save an initial asset value upon object initialization (i.e. the initial value of a car).
b.	Create a method that returns a yearly depreciation rate (i.e., 10%).
c.	Create a method that calculates the monthly depreciation rate, from the yearly depreciation rate.
d.	Create a method that returns the current value of the asset, for a given period. This is the initial value times total depreciation. Total depreciation at time t can be calculated as:
    (1 - monthlyDepr)^t
"""

class Asset(object):

    def __init__(self, initval):
        self._initialvalue = initval

    @property
    def initialvalue(self):
        return self._initialvalue

    @initialvalue.setter
    def initialvalue(self, i_initval):
        self._initialvalue = i_initval

    @staticmethod
    def yearlyDepreciation():
        """
        This part is a little unclear,  it seems more logical that each asset
        would have a different depreciation rate.  However, based on the assignment
        I thought this would best be a static method as it doesnt depend on the class
        its self.
        """
        return .10

    @staticmethod
    def monthlyDepriciation():
        return Asset.yearlyDepreciation() / 12

    def currentvalue(self, period):
        return self._initialvalue * (1 - self.monthlyDepriciation())**period
