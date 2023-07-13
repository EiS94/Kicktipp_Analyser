class Saison:

    def __init__(self):
        self.matchdays = []
        self.players = []

    def add_matchday(self, matchday):
        self.matchdays.append(matchday)
        if len(self.players) == 0:
            self.players = matchday.players

        for player in self.players:
            for md_player in matchday.players:
                if player == md_player:
                    player.matchday_points.append(md_player.get_total_matchday_points())

    def pretty_print(self):
        output = "┌".ljust(16, "─") + "┬"
        for i in range(34):
            output += "────┬"

        output += "─────┐\n│ Name          │"
        for i in range(1, 35):
            output += " " + str(i).rjust(2) + " │"
        output += " GES │"

        output += "\n├".ljust(17, "─") + "┼"
        for i in range(34):
            output += "────┼"
        output += "─────┤\n│ "
        for player in self.players:
            output += player.name.ljust(14) + "│ "
            for points in player.matchday_points:
                output += str(points).rjust(2) + " │ "

            output += str(player.get_total_saison_points()) + " │\n│ "
        return output[:-2]
