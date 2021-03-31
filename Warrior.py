class Warrior:
    __all_possible_achievements = ["Pushover", "Novice", "Fighter",
                                 "Warrior", "Veteran", "Sage", "Elite",
                                 "Conqueror", "Champion", "Master", "Greatest"]

    def __init__(self):
        self._level = 1
        self._experience = 100
        self._rank = "Pushover"
        self._achievements = []

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if (self.level + value) >= 100:
            self._level = 100
            print("You are master now, and reached lvl 100")
        self._level = self._level + value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = self._experience + value

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self):
        if self._level > 1 and self.level < 10:
            self._rank = self.__all_possible_achievements[0]