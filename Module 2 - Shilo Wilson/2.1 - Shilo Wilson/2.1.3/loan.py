"""
Class for Loan as required in exersize 2.1.3
Author: Shilo Wilson

3)	Interest due at time T on a loan depends on the outstanding balance. Principal due is the monthly payment less the i
nterest due. Conceptually, these are recursive calculations as one can determine the interest/principal due at time T if one knows the balance at time T-1 (which, in turn, can be determined if one knows the balance at time T-2).

For each of the below functions, implement two versions: A recursive version (per the above statement) and a version that
uses the formulas provided in the slides:
a.	The interest amount due at a given period (interestDue).
b.	The principal amount due at a given period (principalDue).
c.	The balance of the loan at a given period (balance).
Use your Timer class to time each version of each function; what do you observe? What happens as the time period increases?

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
    def term(self, iterm):
        self._term = iterm

    @rate.setter
    def rate(self,irate):
        self._rate = irate

    @face.setter
    def face(self,iface):
        self._face = iface

    def monthlyPayment(self, period = 0):  #period optional because it is a dummy variable

        """
        rP/(1-(1+r)^-N

        :return: The monthly payment of the Loan
        """

        return (self._rate / 12) * self._face / (1-(1+self._rate/12)**(-1*self._term))

    def interestDue(self, period):
        """
        Computes the interest due at a given period
        :param period: int
        :return: Interest due at specific period
        """
        prev_bal = self.balance(period-1)
        return (self._rate / 12) * prev_bal

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
        return self._face*(1+self._rate / 12)**period - self.monthlyPayment()*(((1+self._rate / 12) ** period-1)/(self._rate / 12))

    def interestDueRecursive(self, period, balance):
        """
        Returns interest due at a given period using recursion
        """
        if period == 1:
            return self._rate / 12 * balance
        else:
            period -= 1
            interest = self._rate / 12 * balance
            balance = balance - self.monthlyPayment() + interest
            return self.interestDueRecursive(period, balance)


    def principalDueRecursive(self, period, balance):
        """
        Returns principal due at a given period using recursion
        """
        if period == 1:
            return self.monthlyPayment() - (self._rate / 12 * balance)
        else:
            period -= 1
            interest = self._rate / 12 *balance
            balance = balance - self.monthlyPayment() + interest
            return self.principalDueRecursive(period, balance)

    def balanceRecursive(self, period, balance):
        """
        Returns balance due at a given period using recursion
        """
        if period == 0:
            return max(balance, 0.0)  # This takes care of the rounding issue on last payment (I was getting 3*10e-7)
        else:
            period -= 1
            interest = self._rate / 12 * balance
            balance = balance - self.monthlyPayment() + interest
            return self.balanceRecursive(period, balance)