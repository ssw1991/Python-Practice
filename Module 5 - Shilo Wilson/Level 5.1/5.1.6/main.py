"""
Author: Shilo Wilson

7) Create a program which does the following:
a. Gives the user a choice of two options: (1) Add Loan, (2) Write file and exit. i. If user enters '1', prompt the
user for the type of Loan, its asset name/value, its face amount, rate, and term. Each prompt should occur one after the
other. After the last prompt, save the entry into a Loan object, notify the user that the loan has been recorded, and
return to the main menu. ii. If user enters '2', loop through all the entered loans and write them to a file. The file
 should be in extension .csv. To do this properly, each sub-entry (loan type, asset name, asset value, amount, rate, and
 term) should be separate by a comma. Each loan should be separated by a newline.
 b. To verify that your generated .csv is a valid .csv file, try opening it in Excel once it has been generated. You
 should see four columns and the number of rows should reflect the number of loans.

8) As a follow-up, create a third option: (3) Read loan .csv file. This option should:
a. Ask the user to enter a file path of the loan .csv file.
b. Load the .csv file into Loan objects. c. Add an additional (fourth) option to display the WAR and WAM of all the
loans.
"""

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel('WARN')
import Loan.loan as loan
from Loan.assets.Car import Civic as Civic
import datetime


def main():
    print '========== Exercise 5.1.6 =========='

    start = datetime.date(2017, 01, 15)
    end = datetime.date(2022, 01, 15)
    car = Civic(20000)
    myLoan = loan.FixedAutoLoan(car, start, end, .055, 22354.46)

    print ('My Loans term is {} months'.format(myLoan.term))

if __name__ == '__main__':
    main()