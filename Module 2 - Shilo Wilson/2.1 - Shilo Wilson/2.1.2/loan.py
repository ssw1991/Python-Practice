"""
Author: Shilo Wilson
Class for Loan

2)	Create a basic Loan class exactly as demonstrated in the lecture (including the setter/getter property methods). Then, extend it with methods that return the following (refer to the slides for any necessary formulas):
a.	The monthly payment amount of the Loan (monthlyPayment). Even though monthlyPayment is likely to be equal for all months, you should still define this with a dummy ‘period’ parameter, since it’s possible some loan types will have a monthly payment dependent on the period.
b.	The total payments of the Loan (totalPayments). This is principal plus interest.
c.	The total interest of the Loan (totalInterest).


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

    def monthlyPayment(self, period = 0):  #period optional because it is a dummy variable
        """
        rP/(1-(1+r)^-N

        :return:
        """
        return (self._rate / 12) * self._face / (1-(1+(self._rate / 12))**(-1*self._term))

    def interestDue(self, period):
        prev_bal = self.balance(period-1)
        return (self._rate / 12) * prev_bal

    def principlaDue(self, period):
        return self.monthlyPayment() - self.interestDue(period)

    def totalPayments(self):
        return self.monthlyPayment() * self._term

    def totalInterest(self):
        return self.totalPayments() - self._face

    def balance(self, period):
        """
        P(1+r)^n - pmt[ ((1+r)^n - 1)/r

        :return:
        """
        return self._face*(1+self._rate / 12)**period - self.monthlyPayment()*(((1+self._rate / 12)**period-1) / (self._rate / 12))

