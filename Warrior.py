class Warrior:
    __all_possible_achievements = ["Pushover", "Novice", "Fighter",
                                   "Warrior", "Veteran", "Sage", "Elite",
                                   "Conqueror", "Champion", "Master", "Greatest"]

    __all_fights = ["Easy fight", "A good fight", "An intense fight"]

    def __init__(self):
        self._level = 1
        self._experience = 100
        self._rank = self.__all_possible_achievements[0]
        self._achievements = []

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if (self.level + value) >= 100:
            self._level = 100
            print("You are master now, and reached lvl 100")
            self._rank = self.__all_possible_achievements[10]
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

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        if value > 10000:
            print("Invlid value")
        elif self._experience + value > 10000:
            self._experience = 10000
            print("You've reached maximun Experience")
            self._rank = self.__all_possible_achievements[10]
        else:
            self._experience = self._experience + value

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, rank):
        if rank in self.__all_possible_achievements:
            self._rank = rank

        else:
            print("Invalid rank")
        pass

    def battle(self, enemy_rank):
        if 1 > enemy_rank > 100:
            return "Invalid level"
        elif (enemy_rank - self._rank) < 0:
            print("need to enter some logic here")
            pass
        pass

    print("helllo nadia")
    print("this is denis")
    print("good night")