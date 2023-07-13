import KicktippParser

ruleset = {
    "home": {
        "tendency": 2,
        "goal difference": 3,
        "result": 5
    },
    "draw": {
        "tendency": 3,
        "result": 5
    },
    "away": {
        "tendency": 3,
        "goal difference": 4,
        "result": 6
    }
}

print("Load results and bets for all matchdays...")
saison = KicktippParser.parse_saison("sg-haerterei")

print("Pretty print results with given ruleset\n")
print(saison.pretty_print())