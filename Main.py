import KicktippParser

community_name = input("Für welche Tipprunde sollen die Punkte mit anderen Regeln berechnet werden?\n")
print("\nFestlegung der Punkteregeln:")

home_tendency = int(input("Punkte für die richtige Tendenz bei Heimsieg?\n"))
home_goal_difference = int(input("Punkte für richtige Tordifferenz bei Heimsieg?\n"))
home_result = int(input("Punkte für das richtige Ergebnis bei Heimsieg?\n"))

draw_tendency = int(input("Punkte für richtige Tendenz bei Unentschieden?\n"))
draw_result = int(input("Punkte für das richtige Ergebnis bei Unentschieden?\n"))

away_tendency = int(input("Punkte für die richtige Tendenz bei Auswärtssieg?\n"))
away_goal_difference = int(input("Punkte für richtige Tordifferenz bei Auswärtssieg?\n"))
away_result = int(input("Punkte für das richtige Ergebnis bei Auswärtssieg?\n"))

ruleset = {
    "home": {
        "tendency": home_tendency,
        "goal difference": home_goal_difference,
        "result": home_result
    },
    "draw": {
        "tendency": draw_tendency,
        "result": draw_result
    },
    "away": {
        "tendency": away_tendency,
        "goal difference": away_goal_difference,
        "result": away_result
    }
}

print("\nStarting analyzing community...")
print("Load results and bets for all matchdays...")
season = KicktippParser.parse_season(community_name, ruleset)

print("Pretty print results with given ruleset\n")
print(season.pretty_print())

input("\nZum Beenden Enter drücken.")
