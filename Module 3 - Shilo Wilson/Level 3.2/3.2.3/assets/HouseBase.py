from asset import Asset as Asset

class HouseBase(Asset):

    def __init__(self, init):
        super(HouseBase, self).__init__(init)

class PrimaryHome(HouseBase):

    def __init__(self, init):
        super(PrimaryHome, self).__init__(init)

    def yearlyDepreciation(self):
        return .02

class VacationHome(HouseBase):

    def __init__(self, init):
        super(VacationHome, self).__init__(init)

    def yearlyDepreciation(self):
        return .01