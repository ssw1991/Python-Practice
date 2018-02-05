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
import Loan
import Utilities.menu_driver as menu


def main():
    print '========== 4.3.7 - 4.3.8 =========='

    cont = 1
    loanpool = []
    while cont:

        """
        Guide user through menu based on input
        """
        print('Select an Option\n'
              '1) Add Loan\n'
              '2) Write Loans to file\n'
              '3) Read Loan\n'
              '4) Display WAR and WAM\n'
              '0) Exit')

        try:
            input = int(raw_input('Enter Selection: '))
            if not (0 <= input <= 4):
                raise ValueError
        except ValueError as e:
            logger.warn( 'Invalid selection, selection must be 0 - 4')
            continue

        if input == 0:
            cont = 0
            continue

        if input == 1:
            loan = menu.add_loan()
            if loan:
                loanpool.append(loan)
        elif input == 2:
            if len(loanpool) > 0:
                fp = raw_input('Enter a filepath: ')
                menu.write_to_file(fp, loanpool)
            else:
                logger.warn('No Loans to write')
        elif input == 3:
            raw_input('Enter File path')
            try:
                loanpool = menu.read_loan(fp)
            except Exception as e:
                logger.exception(e.message)

        elif input == 4:
            if len(loanpool) == 0:
                logger.exception('No loans')
            else:
                loans = Loan.loan.LoanPool(loanpool)
                print ('WAR is {}'.format(loans.WAR()))
                print ('WAM is {}'.format(loans.WAM()))

if __name__ == '__main__':
    main()