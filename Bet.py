class Bet:

    def __init__(self, home_goals, away_goals):
        self.home_goals = home_goals
        self.away_goals = away_goals
        self.won = False
        self.points = 0

    def calculate_points(self, result, ruleset):
        # eliminate not placed bets
        if self.home_goals == -1 and self.away_goals == -1:
            return

        # home
        if result.home_goals > result.away_goals:
            if self.home_goals > self.away_goals:
                # result
                if self.home_goals == result.home_goals and self.away_goals == result.away_goals:
                    self.won = True
                    self.points = ruleset["home"]["result"]
                # goal difference
                elif self.home_goals - self.away_goals == result.home_goals - result.away_goals:
                    self.won = True
                    self.points = ruleset["home"]["goal difference"]
                # tendency
                else:
                    self.won = True
                    self.points = ruleset["home"]["tendency"]
        # away
        elif result.home_goals < result.away_goals:
            if self.home_goals < self.away_goals:
                # result
                if self.home_goals == result.home_goals and self.away_goals == result.away_goals:
                    self.won = True
                    self.points = ruleset["away"]["result"]
                # goal difference
                elif self.home_goals - self.away_goals == result.home_goals - result.away_goals:
                    self.won = True
                    self.points = ruleset["away"]["goal difference"]
                # tendency
                else:
                    self.won = True
                    self.points = ruleset["away"]["tendency"]
        # draw
        else:
            if self.home_goals == self.away_goals:
                # result
                if self.home_goals == result.home_goals and self.away_goals == result.away_goals:
                    self.won = True
                    self.points = ruleset["draw"]["result"]
                # tendency
                else:
                    self.won = True
                    self.points = ruleset["draw"]["tendency"]

    def __str__(self):
        return f"{self.home_goals}:{self.away_goals} -> {self.points} Punkte"

    def __repr__(self):
        return self.__str__()
