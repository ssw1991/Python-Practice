from Car import Car as Car

class Civic(Car):

    def __init__(self, init):
        super(Civic, self).__init__(init)

    def yearlyDepreciation(self):
        return .08