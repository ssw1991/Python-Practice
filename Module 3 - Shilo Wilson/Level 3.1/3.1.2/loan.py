"""
Class for Loan as required in exersize 2.2.1
Author: Shilo Wilson
"""
from assets.asset import Asset as Asset
from assets.Car.Car import Car as Car


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
    def rate(self, period = 0):
        return self.getRate(period)

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
        return self.calcMonthlyPmt(self._face, self.getRate(period), self._term)

    def interestDue(self, period):
        """
        Computes the interest due at a given period
        :param period: int
        :return: Interest due at specific period
        """
        prev_bal = self.balance(max(0,period-1))
        return self.monthlyRate(self.getRate(period)) * prev_bal

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
        return self.calcBal(self._face, self.getRate(period), self._term, period)

    def recoveryValue(self, period):
        return .6 * self.asset.currentvalue(period)

    def equity(self, period):
        return self.asset.currentvalue(period) - self.balance(period)


class FixedRateLoan(Loan):

    def __init__(self, asset, term, rate, face):
        super(FixedRateLoan, self).__init__(asset, term, rate, face)

    def getRate(self, period = 0):
        return self._rate


class VariableRateLoan(Loan):

    def __init__(self, asset, term, rateDict, face):
        self._rateDict = rateDict
        super(VariableRateLoan, self).__init__(asset, term, None, face)

    @property
    def rateDict(self):
        return self._rateDict

    @rateDict.setter
    def rateDict(self, irateDict):
        self._rateDict = irateDict

    def getRate(self, period = 0):
        key = max([i for i in self._rateDict if i <= period])
        return self._rateDict[key]


class FixedAutoLoan(FixedRateLoan):

    def __init__(self, asset, term, rate, face):
        if isinstance(asset, Car):
            super(FixedAutoLoan, self).__init__(asset,term, rate, face)
        else:
            print('Need a car for an AutoLoan')


    def __str__(self):
        """
        To make testing function calls eaiser
        """
        return 'Auto Loan for {} at {} for {} months, with payment of {}'.format(self.face, self.rate, self.term, self.monthlyPayment())


class LoanPool(object):

    def __init__(self, loans):
        self._loans = loans

    @property
    def loans(self):
        return self._loans

    @loans.setter
    def loans(self, iloans):
        self._loans = iloans

    def totalPrincipal(self):
        return sum([i.face for i in self.loans])

    def totalBalance(self,period):
        return sum([i.balance(period) for i in self.loans if period <= i.term])

    def aggregateInfo(self,period):
        principal = sum([i.principalDue(period) for i in self.loans if period <= i.term])
        interest = sum([i.interestDue(period) for i in self.loans if period <= i.term])
        totalPayment = sum([i.monthlyPayment(period) for i in self.loans if period <= i.term])
        return {'principal': principal, 'interest': interest, 'Payments due': totalPayment}

    def active(self,period):
        return len([i for i in self.loans if period <= i.term])

    def WAR(self):
        """
        Computes the weighted average rate
        :param mortgage_tuples: Loan object
        :return: Weighted average rate
        """
        return reduce(lambda prev, x: prev + float(x.face) * x.rate, self._loans,0) / self.totalBalance(0)

    def WAM(self):
        """
        Computes the weighted average maturity
        :return: Weighted average maturity
        """

        return reduce(lambda prev, x: prev + float(x.face) * x.term, self._loans,0) / self.totalBalance(0)
