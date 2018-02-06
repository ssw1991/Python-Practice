"""
Author: Shilo Wilson


"""
from assets.asset import Asset as Asset
from assets.Car import Car as Car
import logging
from math import floor
from Utilities.utilities import memoize
from Utilities.Timer.Timer import Timer as Timer
logger = logging.getLogger('__main__.{}'.format(__name__))


class Loan(object):

    def __init__(self, asset, start, end, rate, face):
        if isinstance(asset, Asset):
            self._start = start
            self._end = end
            self._term = self.toTerm(start, end)
            self._rate = rate
            self._face = face
            self._asset = asset
        else:
            logger.error('Incorrect type for Asset')
            raise TypeError('Loan must contain an Asset')

    def to_dict(self):
        raise NotImplementedError

    @property
    def term(self):
        return self._term
    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def rate(self, period = 0):
        return self.getRate(period)

    @property
    def face(self):
        return self._face

    @property
    def asset(self):
        return self._asset

    @end.setter
    def end(self, iend):
        self._end = iend

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
        logger.debug('calcMonthly payment called with rate {}'.format(cls.monthlyRate(rate)))
        return (cls.monthlyRate(rate)) * face / (1-(1+cls.monthlyRate(rate))**(-1*term))

    @classmethod
    def calcBal(cls, face, rate, term, period):
        logger.debug('calcBal payment called with rate {}'.format(cls.monthlyRate(rate)))
        return face * (1 + cls.monthlyRate(rate)) ** period - cls.calcMonthlyPmt(face, rate, term) * (((1 + cls.monthlyRate(rate)) ** period - 1) / (rate/12))

    @staticmethod
    def toTerm(start, end):
        """
          Computes the term in months based on days
          a month on average has 30.41667 days
          """

        return floor((end - start).days / 30.41667)

    def monthlyPayment(self, period = 0):  # period optional because it is a dummy variable

        """
        rP/(1-(1+r)^-N

        :return: The monthly payment of the Loan
        """
        if period > self._term:
            logger.info('Passed in period is greater than the term')
        logger.debug('Monthy payment called with period {}'.format(period))
        return self.calcMonthlyPmt(self._face, self.getRate(period), self._term)

    def interestDue(self, period):
        """
        Computes the interest due at a given period
        :param period: int
        :return: Interest due at specific period
        """
        if period > self._term:
            logger.info('Passed in period is greater than the term')
        prev_bal = self.balance(max(0,period-1))
        return self.monthlyRate(self.getRate(period)) * prev_bal

    def principalDue(self, period):
        """
        Returns the principal due at a given period
        :param period: int
        :return: Principal due at a specific period
        """
        if period > self._term:
            logger.info('Passed in period is greater than the term')
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
        if period > self._term:
            logger.info('Passed in period is greater than the term')
        return self.calcBal(self._face, self.getRate(period), self._term, period)

    def recoveryValue(self, period):
        return .6 * self.asset.currentvalue(period)

    def equity(self, period):
        return self.asset.currentvalue(period) - self.balance(period)

    @memoize
    def interestDueRecursive(self, period, balance):
        """
        Returns interest due at a given period using recursion
        """
        logger.warn('Recursive function being used, consider using direct computation')
        if period == 1:
            return self._rate / 12 * balance
        else:
            period -= 1
            interest = self._rate / 12 * balance
            balance = balance - self.monthlyPayment() + interest
            return self.interestDueRecursive(period, balance)

    @memoize
    def principalDueRecursive(self, period, balance):
        """
        Returns principal due at a given period using recursion
        """
        logger.warn('Recursive function being used, consider using direct computation')
        if period == 1:
            return self.monthlyPayment() - (self._rate / 12 * balance)
        else:
            period -= 1
            interest = self._rate / 12 * balance
            balance = balance - self.monthlyPayment() + interest
            return self.principalDueRecursive(period, balance)

    @memoize
    def balanceRecursive(self, period, balance):
        """
        Returns balance due at a given period using recursion
        """
        logger.warn('Recursive function being used, consider using direct computation')
        if period == 0:
            return max(balance, 0.0)  # This takes care of the rounding issue on last payment (I was getting 3*10e-7)
        else:
            period -= 1
            interest = self._rate / 12 * balance
            balance = balance - self.monthlyPayment(period) + interest
            return self.balanceRecursive(period, balance)


class FixedRateLoan(Loan):

    def __init__(self, asset, start, end, rate, face):
        super(FixedRateLoan, self).__init__(asset, start, end, rate, face)

    def getRate(self, period = 0):
        return self._rate

    def to_dict(self):
        return {'Type': 'Fixed Rate Loan', 'Asset': str(self.asset),
                'Asset Value': self.asset.initialvalue, 'Face': self.face, 'Rate': self.rate, 'Term': self.term}


class VariableRateLoan(Loan):

    def __init__(self, asset, start, end, rateDict, face):
        self._rateDict = rateDict
        super(VariableRateLoan, self).__init__(asset, start, end, None, face)

    def to_dict(self):
        return {'Type': 'Variable Rate Loan', 'Asset': str(self.asset),
                'Asset Value': self.asset.initialvalue, 'Face': self.face, 'Rate': self.rateDict, 'Term': self.term}

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

    def __init__(self, asset, start, end, rate, face):
        if isinstance(asset, Car):
            super(FixedAutoLoan, self).__init__(asset, start, end, rate, face)
        else:
            logger.error('Incorrect type for asset.Car')
            raise TypeError('Need a car for an AutoLoan')

    def to_dict(self):
        return {'Type': 'Fixed Rate Auto Loan', 'Asset': str(self.asset),
                'Asset Value': self.asset.initialvalue,  'Face': self.face, 'Rate': self.rate,'Term': self.term}

    def __str__(self):
        """
        To make testing function calls eaiser
        """
        return 'Auto Loan for {} at {} for {} months, with payment of {}'.format(self.face, self.rate, self.term, self.monthlyPayment())


class LoanPool(object):

    def __init__(self, loans):
        if not all(isinstance(i, Loan) for i in loans):
            logger.error('All loans must contain asset')
            raise TypeError('List of Loans must all be loans')
        self._loans = loans

    def __iter__(self):
        return iter(self._loans)


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
