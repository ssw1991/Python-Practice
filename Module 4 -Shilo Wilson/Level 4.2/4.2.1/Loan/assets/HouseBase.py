import logging
logger = logging.getLogger('__main__.{}'.format(__name__))
from asset import Asset as Asset


class HouseBase(Asset):

    def __init__(self, init):
        super(HouseBase, self).__init__(init)

    def __str__(self):
        return 'House'


class PrimaryHome(HouseBase):

    def __init__(self, init):
        super(PrimaryHome, self).__init__(init)

    def yearlyDepreciation(self):
        return .02

    def __str__(self):
        return 'Primary Home'


class VacationHome(HouseBase):

    def __init__(self, init):
        super(VacationHome, self).__init__(init)

    def yearlyDepreciation(self):
        return .01

    def __str__(self):
        return 'Vacation Home'