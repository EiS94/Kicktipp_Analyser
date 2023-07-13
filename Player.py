class Player:

    def __init__(self, name):
        self.name = name
        self.points = []
        self.bonus_points = 0
        self.bets = []
        self.matchday_points = []

    def get_total_matchday_points(self, bonus=True):
        total_points = 0
        for bet in self.bets:
            total_points += bet.points
        if bonus:
            return total_points + self.bonus_points
        else:
            return total_points

    def get_total_saison_points(self, bonus=True):
        if bonus:
            return sum(self.matchday_points) + self.bonus_points
        else:
            return sum(self.matchday_points)

    def add_points(self, points):
        self.points.append(points)

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return f"{self.name} -> {self.get_total_matchday_points()} Spieltagspunkte -> Gesamt: {self.get_total_saison_points()} Punkte"

    def __repr__(self):
        return self.__str__()
