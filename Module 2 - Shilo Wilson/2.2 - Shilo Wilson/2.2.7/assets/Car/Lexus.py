from Car import Car as Car


class Lexus(Car):

    def __init__(self, init):
        super(Lexus, self).__init__(init)

    def yearlyDepreciation(self):
        return .04