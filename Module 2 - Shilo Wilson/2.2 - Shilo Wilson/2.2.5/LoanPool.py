"""
Author: Shilo Wilson
5)	Create a LoanPool class that can contain and operate on a pool of loans (composition). Provide the following functionality:
a.	A method to get the total loan principal.
b.	A method to get the total loan balance for a given period.
c.	Methods to get the aggregate principal, interest, and total payment due in a given period.
d.	A method that returns the number of 'active' loans. Active loans are loans that have a balance greater than zero.
e.	Methods to calculate the Weighted Average Maturity (WAM) and Weighted Average Rate (WAR) of the loans. You may port over the previously implemented global functions.
"""


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

        total_val = sum([float(i.face) for i in self.loans])
        war = 0
        for i in self.loans:
            war += (i.face * i.rate()) / total_val
        return war

    def WAM(self):
        """
        Computes the weighted average maturity
        :param mortgage_tuples: <list> [<tuple>(<int> amount,<float> rate, <term>
        :return: Weighted average maturity
        """

        total_val = sum([float(i.face) for i in self.loans])
        wam = 0
        for i in self.loans:
            wam += (i.face * float(i.term)) / total_val
        return wam