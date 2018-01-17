"""
Class for Loan as required in exersize 2.1.5
Author: Shilo Wilson

5)	To demonstrate understanding of static-level methods, do the following:
a.	Create a static-level method in Loan called monthlyRate. This should return the monthly interest rate for a passed-in annual rate.
b.	Create another static-level method that does the opposite (returns an annual rate for a passed-in monthly rate).
c.	Test the static-level method in main.
d.	Modify all the Loan methods that rely on the rate to utilize the static-level rate functions.
e.	What are the benefits of static-level methods? When are they useful?


"""
class Loan(object):

    def __init__(self, term, rate, face):
        self._term = term
        self._rate = rate
        self._face = face

    @property
    def term(self):
        return(self._term)

    @property
    def rate(self):
        return(self._rate)

    @property
    def face(self):
        return(self._face)

    @term.setter
    def term(self,iterm):
        self._term = iterm

    @rate.setter
    def rate(self,irate):
        self._rate = irate

    @face.setter
    def face(self,iface):
        self._face = iface

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
        return self.calcMonthlyPmt(self._face, self._rate, self._term)

    def interestDue(self, period):
        """
        Computes the interest due at a given period
        :param period: int
        :return: Interest due at specific period
        """
        prev_bal = self.balance(period-1)
        return self.monthlyRate(self._rate) * prev_bal

    def principlaDue(self, period):
        """
        Returns the principal due at a given period
        :param period: int
        :return: Principal due at a specific period
        """
        return self.monthlyPayment() - self.interestDue(period)

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
        return self.calcBal(self._face, self._rate, self._term, period)
