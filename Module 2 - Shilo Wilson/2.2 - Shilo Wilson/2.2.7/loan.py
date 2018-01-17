"""
Class for Loan as required in exersize 2.2.1
Author: Shilo Wilson
"""
from assets.asset import Asset as Asset
class Loan(object):

    def __init__(self, asset, term, rate, face):
        if isinstance(asset, Asset):
            self._term = term
            self._rate = rate
            self._face = face
            self._asset = asset
        else:
            print('Not valid arguments')
            pass

    @property
    def term(self):
        return self._term

    @property
    def rate(self):
        return self.rate()

    @property
    def face(self):
        return self._face

    @property
    def asset(self):
        return self._asset

    @term.setter
    def term(self, iterm):
        self._term = iterm

    @rate.setter
    def rate(self, irate):
        self._rate = irate

    @face.setter
    def face(self,iface):
        self._face = iface

    @asset.setter
    def asset(self, iasset):
        self._asset = iasset

    @staticmethod
    def monthlyRate(annual):
        return annual / 12

    @staticmethod
    def annualRate(monthly):
        return monthly * 12

    @classmethod
    def calcMonthlyPmt(cls, face, rate, term):
        return (cls.monthlyRate(rate)) * face / (1-(1+cls.monthlyRate(rate))**(-1*term))

    @classmethod
    def calcBal(cls, face, rate, term, period):
        return face * (1 + cls.monthlyRate(rate)) ** period - cls.calcMonthlyPmt(face, rate, term) * (((1 + cls.monthlyRate(rate)) ** period - 1) / (rate/12))

    def monthlyPayment(self, period = 0):  # period optional because it is a dummy variable

        """
        rP/(1-(1+r)^-N

        :return: The monthly payment of the Loan
        """
        return self.calcMonthlyPmt(self._face, self.rate(period), self._term)

    def interestDue(self, period):
        """
        Computes the interest due at a given period
        :param period: int
        :return: Interest due at specific period
        """
        prev_bal = self.balance(max(0,period-1))
        return self.monthlyRate(self.rate(period)) * prev_bal

    def principalDue(self, period):
        """
        Returns the principal due at a given period
        :param period: int
        :return: Principal due at a specific period
        """
        return self.monthlyPayment(period) - self.interestDue(period)

    def totalPayments(self):
        """
        Computes the total payments made of the life of the loan
        """
        return self.monthlyPayment() * self._term

    def totalInterest(self):
        """
        Computes the total interest paid over the life of the loan
        """
        return self.totalPayments() - self._face

    def balance(self, period):
        """
        Returns the balance at given time period by below formula
        P(1+r)^n - pmt[ ((1+r)^n - 1)/r

        :return: Balance remaining at period n
        """
        return self.calcBal(self._face, self.rate(period), self._term, period)

    def recoveryValue(self, period):
        return .6 * self.asset.currentvalue(period)

    def equity(self, period):
        return self.asset.currentvalue(period) - self.balance(period)
