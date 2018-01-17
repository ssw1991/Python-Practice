from HouseBase import HouseBase as House


class VacationHome(House):

    def __init__(self, init):
        super(VacationHome, self).__init__(init)

    def yearlyDepreciation(self):
        return .01