"""
Class for Loan as required in exersize 2.1.4
Author: Shilo Wilson

4)	To demonstrate understanding of class-level methods, do the following:
a.	Implement a class-level method called calcMonthlyPmt, in the Loan base class. This should calculate a monthly payment based on three parameters: face, rate, and term.
b.	Create a class-level function, in the Loan base class, which calculates the balance (calcBalance). Input parameters should be face, rate, term, period.
c.	Test the class-level methods in main.
d.	Modify the object-level methods for monthlyPayment and balance to delegate to the class-level methods.
e.	Test the object-level methods to ensure they still work correctly.
f.	What are the benefits of class-level methods? When are they useful?


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

    @classmethod
    def calcMonthlyPmt(cls, face, rate, term):
        return (rate / 12) * face / (1-(1+rate/12)**(-1*term))

    @classmethod
    def calcBal(cls, face, rate, term, period):
        return face * (1 + rate/ 12) ** period - cls.calcMonthlyPmt(face, rate, term) * (((1 + rate /12 ) ** period - 1) / (rate/12))

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
        return(self._rate/12 * prev_bal)

    def principlaDue(self, period):
        """
        Returns the principal due at a given period
        :param period: int
        :return: Principal due at a specific period
        """
        return(self.monthlyPayment() - self.interestDue(period))


    def totalPayments(self):
        """
        Computes the total payments made of the life of the loan
        """
        return(self.monthlyPayment() * self._term)

    def totalInterest(self):
        """
        Computes the total interest paid over the life of the loan
        """
        return(self.totalPayments() - self._face)

    def balance(self, period):
        """
        Returns the balance at given time period by below formula
        P(1+r)^n - pmt[ ((1+r)^n - 1)/r

        :return: Balance remaining at period n
        """
        return self.calcBal(self._face, self._rate, self._term, period)
