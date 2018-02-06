import random



class player(object):

    def __init__(self, strategy):
        """
        Strategy is 1 of player switches, else 0
        :param strategy:
        """
        self._strat = strategy
        self._choice = None

    @property
    def strat(self):
        return self._strat

    @property
    def choice(self):
        return self._choice

    def choose(self, doors):
        self._choice = random.choice(doors)

    @choice.setter
    def choice(self, ichoice):
        self._choice = ichoice




class game(object):

    def __init__(self, player, doors):
        self._doors = doors
        self._player = player
        self._prize = random.choice(self.doors)

    def __call__(self):
        return self.playGame()

    @property
    def prize(self):
        return self._prize

    @property
    def doors(self):
        return self._doors

    def playGame(self):
        """
        Returns the outcome of the game
        :return:
        """
        self._player.choose(self.doors)
        playerChoice = self._player.choice
        # Host chooses a door which the player did not choose, and does not have the prize
        new_door= random.choice([i for i in self.doors if i != self.prize and i != playerChoice])

        # if the player strat is to change, the player will choose a door that they have not selected,
        # and that the host did not select.
        if not self._player.strat:
            return self._player.choice == self.prize
        else:
            self._player.choice = random.choice([i for i in self.doors if i != new_door and i != playerChoice])

        # return if the players choice is correct
        return self._player.choice == self.prize
