class Result:

    def __init__(self, home_name, away_name, home_goals, away_goals):
        self.home_name = home_name
        self.away_name = away_name
        self.home_goals = home_goals
        self.away_goals = away_goals

    def __eq__(self, other):
        return self.home_name == other.home_name and self.away_name == other.away_name

    def __hash__(self):
        return hash((self.away_name, self.home_name))

    def __str__(self):
        return f"{self.home_name} {self.home_goals}:{self.away_goals} {self.away_name}"
