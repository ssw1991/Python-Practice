
from Loan.loan import FixedAutoLoan as AutoLoan
from Loan.mortgage import FixedRateMortgage as FixedMort
from Loan.loan import FixedRateLoan as FixedLoan
import Loan.assets.Car as Car
import Loan.assets.HouseBase as House

import csv
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

def add_loan():
    """
    This function takes user input and returns a loan.  Error handling from
    user errors are reported to user and they are repromted.   User may manually
    exit this function, in which case the return value is None
    :return:
    """
    try:
        """
        Retrieving user input for first menu
        """
        user_asset = int(raw_input('Select an Asset: \n'
                                   '1) Permanent Home \n'
                                   '2) Vacation Home \n'
                                   '3) Civic \n'
                                   '4) Lexus \n'
                                   '5) Other Car \n'
                                   '0) Return to Main \n'))
        if not (0 <= user_asset <= 5):
            """
            Test to ensure the input is valid
            """
            raise ValueError
        if user_asset == 0:
            """
            Test if user requested to exit
            """
            return None
    except ValueError as e:
        """
        Handle the value error if it was raised.
        """
        logger.warn('Invalid selection, selection must be 0 - 5')
        user_asset = 0
        add_loan()

    while user_asset:
        """
        As long as the user asset exist we need to get input (IE the user did not exit or enter incorrect value)
        """
        try:
            value = float(raw_input('Enter the Value'))
            if user_asset == 1:
                asset = House.PrimaryHome(value)
                user_asset = 0
            elif user_asset == 2:
                asset = House.VacationHome(value)
                user_asset = 0
            elif user_asset == 3:
                asset = Car.Civic(value)
                user_asset = 0
            elif user_asset == 4:
                asset = Car.Lexus(value)
                user_asset = 0
            elif user_asset == 5:
                asset = Car.Car(value)
                user_asset = 0

        except Exception as e:
            """
            This is raised if the input is not a numeric
            """
            logger.warn('Incorrect Input try again')
            continue
        try:
            face = float(raw_input('Enter the Loan Amount'))
        except Exception as e:
            logger.warn('Incorrect Input try again')
            continue
        try:
            rate = float(raw_input('Enter the rate'))
        except Exception as e:
            logger.warn('Incorrect Input try again')
            continue
        try:
            term = int(raw_input('Enter the term in months'))
        except Exception as e:
            logger.warn('Incorrect Input try again')
            continue

        if isinstance(asset, House.HouseBase):
            """
            Test the asset to determine appropriate loan
            """
            loan = FixedMort(asset, term, rate, face)
        elif isinstance(asset, Car.Car):
            loan = AutoLoan(asset, term, rate, face)
        else:
            loan = FixedLoan(asset, term, rate, face)
        if loan:
            print'Loan has been succesfully loaded'
        return (loan)


def load_asset(type, value):
    """
    This function is used to load the correct asset
    :param type:
    :param value:
    :return:
    """

    """
    Test the asset type to load correct asset
    """
    if type == 'Car':
        return (Car.Car(value))
    elif type == 'Civic':
        return Car.Civic(value)
    elif type == 'Lexus':
        return Car.Lexus(value)
    elif type == 'Primary Home':
        return House.PrimaryHome(value)
    elif type == 'Vacation Home':
        return House.VacationHome(value)
    elif type == 'House':
        return House.HouseBase(value)


def load_loan(loan_dict):
    """
    This function converts a loan dict into a loan object
    :param loan_dict:
    :return:
    """
    if loan_dict['Type'] == 'Fixed Rate Loan':
        loan = FixedLoan(load_asset(loan_dict['Asset'], float(loan_dict['Asset Value'])),
                         float(loan_dict['Term']), float(loan_dict['Rate']),
                         float(loan_dict['Face']))
    if loan_dict['Type'] == 'Fixed Rate Auto Loan':
        loan = AutoLoan(load_asset(loan_dict['Asset'], float(loan_dict['Asset Value'])),
                        float(loan_dict['Term']), float(loan_dict['Rate']),
                        float(loan_dict['Face']))
    if loan_dict['Type'] == 'Fixed Rate Mortgage':
        loan = FixedMort(load_asset(loan_dict['Asset'], float(loan_dict['Asset Value'])),
                         float(loan_dict['Term']), float(loan_dict['Rate']),
                         float(loan_dict['Face']))
    return (loan)


def read_loan(fp):
    """
    This function reads the specified file, and returns a list of loans
    :param fp:
    :return:
    """
    loanpool = []
    with open(fp) as infile:
        reader = csv.DictReader(infile)
        for i in reader:
            loanpool.append(load_loan(i))
    return (loanpool)


def write_to_file(fp, loanpool):
    """
    This function writes the loans to a file
    :param fp:
    :param loanpool:
    :return:
    """
    try:
        with open(fp, 'a') as outfile:
            fieldnames = loanpool[0].to_dict().keys()
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in loanpool:
                writer.writerow(i.to_dict())
    except:
        with open(fp, 'w+') as outfile:
            fieldnames = loanpool[0].to_dict().keys()
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in loanpool:
                writer.writerow(i.to_dict())