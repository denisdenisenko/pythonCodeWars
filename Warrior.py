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
        if self._level >= 1 and self.level < 10:
            self._rank = self.__all_possible_achievements[0]
        elif self._level >= 10 and self.level < 19:
            self._rank = self.__all_possible_achievements[1]
        elif self._level >= 20 and self.level < 29:
            self._rank = self.__all_possible_achievements[2]
        elif self._level >= 30 and self.level < 39:
            self._rank = self.__all_possible_achievements[3]
        elif self._level >= 40 and self.level < 49:
            self._rank = self.__all_possible_achievements[4]
        elif self._level >= 50 and self.level < 59:
            self._rank = self.__all_possible_achievements[5]
        elif self._level >= 60 and self.level < 69:
            self._rank = self.__all_possible_achievements[6]
        elif self._level >= 70 and self.level < 79:
            self._rank = self.__all_possible_achievements[7]
        elif self._level >= 80 and self.level < 89:
            self._rank = self.__all_possible_achievements[8]
        elif self._level >= 90 and self.level < 99:
            self._rank = self.__all_possible_achievements[9]
        elif self._level == 100:
            self._rank = self.__all_possible_achievements[10]
