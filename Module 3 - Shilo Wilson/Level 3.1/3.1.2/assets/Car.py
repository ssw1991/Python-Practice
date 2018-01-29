from asset import Asset as Asset

class Car(Asset):

    def __init__(self, init):
        super(Car, self).__init__(init)


class Civic(Car):

    def __init__(self, init):
        super(Civic, self).__init__(init)

    def yearlyDepreciation(self):
        return .08


class Lexus(Car):

    def __init__(self, init):
        super(Lexus, self).__init__(init)

    def yearlyDepreciation(self):
        return .04