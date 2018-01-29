import logging
logger = logging.getLogger('__main__.{}'.format(__name__))
from asset import Asset as Asset


class Car(Asset):

    def __init__(self, init):

        super(Car, self).__init__(init)

    def __str__(self):
        return 'Car'


class Civic(Car):
    def __init__(self, init):
        super(Civic, self).__init__(init)

    def yearlyDepreciation(self):
        return .08

    def __str__(self):
        return 'Civic'

class Lexus(Car):

    def __init__(self, init):
        super(Lexus, self).__init__(init)

    def yearlyDepreciation(self):
        return .04

    def __str__(self):
        return 'Lexus'