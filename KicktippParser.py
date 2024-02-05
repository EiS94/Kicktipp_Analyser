import re

import requests
from bs4 import BeautifulSoup
import tqdm

from Bet import Bet
from Matchday import Matchday
from Player import Player
from Result import Result
from Season import Season


def parse_season(community_name, ruleset=None):
    if ruleset is None:
        ruleset = get_default_ruleset()

    season = Season()
    for i in tqdm.tqdm(range(1, 35)):
        season.add_matchday(parse_matchday(community_name, i, ruleset))

    season.players.sort(key=lambda x: x.get_total_saison_points(), reverse=True)

    return season


def parse_matchday(community_name, matchday_number, ruleset=None):
    if ruleset is None:
        ruleset = get_default_ruleset()

    url = f"https://www.kicktipp.de/{community_name}/tippuebersicht?spieltagIndex={matchday_number}"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", {"id": "ranking"})

        results = []

        # get official results of all matchday matches
        head = table.find("thead")
        for row in head.findAll("th"):
            counter = 0
            home_name, away_name = "", ""
            # get club names
            for club in row.findAll("div", {"class": "headerbox"}):
                if counter == 0:
                    home_name = club.text
                if counter == 1:
                    away_name = club.text
                counter += 1

            if home_name != "" and away_name != "":
                # get goals
                try:
                    home_goals = int(row.find("span", {"class": {"kicktipp-heim"}}).encode_contents().decode())
                    away_goals = int(row.find("span", {"class": {"kicktipp-gast"}}).encode_contents().decode())
                    # add result to the results list
                    results.append(Result(home_name, away_name, home_goals, away_goals))
                except ValueError:
                    # this Error can occur if a match of the matchday is not already played
                    continue
        # get players with bets
        players = []

        body = table.find("tbody")
        for row in body.findAll("tr"):
            player_name = row.find("div", {"class": "mg_name"})
            if player_name is not None:
                player_name = player_name.encode_contents().decode()
            else:
                continue
            player_bets = row.findAll("td", {"class": re.compile("nw . ereignis ereignis\\d")})
            player_bets_list = [Bet(-1, -1) for _ in range(9)]
            for result in player_bets:
                try:
                    bet_string = re.match(r"\d{1,2}:\d{1,2}", result.encode_contents().decode()).group().split(":")
                    match_number = int(re.search(r"nw . ereignis ereignis(\d)", result.__str__()).group(1))
                    player_bets_list[match_number] = (Bet(int(bet_string[0]), int(bet_string[1])))
                except AttributeError:
                    continue

            player = Player(player_name)
            player.bets = player_bets_list
            players.append(player)

        # calculate points per player
        for player in players:
            for i in range(len(results)):
                player.bets[i].calculate_points(results[i], ruleset)

        return Matchday(matchday_number, players, results)


def get_default_ruleset():
    ruleset = {
        "home": {
            "tendency": 2,
            "goal difference": 3,
            "result": 4
        },
        "draw": {
            "tendency": 2,
            "result": 4
        },
        "away": {
            "tendency": 2,
            "goal difference": 3,
            "result": 4
        }
    }
    return ruleset
