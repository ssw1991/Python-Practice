"""
Author: Shilo Wilson

1) Modify your Timer class to use a logging statement (info level) instead of a print statement.

2) Modify your Timer class as follows:
    a. Add a class-level warnThreshold variable, which defaults to 1 minute.
    b. When printing the time taken, use a warn-level log statement instead of info-level if the time taken exceeds the
    warn threshold.

3) Add logging statements to your Loan class. This should consist of the following:
    a. Anytime an exception is thrown (i.e., when an incorrect Asset type is passed-into the initialization function),
    log an error prior to raising the exception.
    b. Debug-level logs which display interim steps of calculations and return values for the Loan functions.
    c. Info-level logs to display things like 't is greater than term' in the loan functions.
    d. At the point the exception is caught (in your main function) use logging.exception to display the exception in
    addition to a custom message.
    e. Add a warn log to the recursive versions of the waterfall functions (that they are expected to take a long time,
    so the explicit versions are recommended).

4) Play around with your Loan and Timer classes to trigger logging statements. Switch logging levels in your main code
to demonstrate how to turn on/off different levels of logging.

"""
# Creating Logger first so that when modules are imported their loggers are in heirarchy.
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel('INFO')


from Timer import Timer
import Loan.assets.Car
from Loan.assets.Car import Civic as Civic
from Loan.loan import FixedAutoLoan as AutoLoan
import logging





def main():




    logger.info('========== Level 4.2 All ==========')

    try:
        car_loan = AutoLoan(10000, 60, .055, 12000)
    except Exception as e:
        logger.exception(e.message)

    car_loan = AutoLoan(Civic(10000), 60, .055, 12000)
    car_loan.balanceRecursive(5, car_loan.face)
    # Should show info level log
    car_loan.balance(63)

    logger.setLevel('DEBUG')

    #Should not show info level log
    car_loan.balance(63)

    #Test Child Loggers
    logger.getChild('Loan.loan').debug('Test Message')
    logger.debug('Level: {}'.format(logger.getChild('Loan.loan').getEffectiveLevel()))

    logger.setLevel('INFO') # So final error message shows

    with Timer.Timer('My long Timer'):
        sum(i**4 for i in range(100000000))


if __name__ == '__main__':
    main()


