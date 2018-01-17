from HouseBase import HouseBase as House


class PrimaryHome(House):

    def __init__(self, init):
        super(PrimaryHome, self).__init__(init)

    def yearlyDepreciation(self):
        return .02