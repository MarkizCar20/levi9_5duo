from flask import Flask, jsonify, Response, make_response
from flask_restful import Resource, Api
from models.models import PlayerStats
import json
import csv

players_stats_dict = {}

#Opening csv file and creating stats for every player
with open('L9HomeworkChallengePlayersInput.csv', newline='') as f:
    reader = csv.reader(f)
    headers = next(reader)

    for row in reader:
        player_name = row[0]
        
        if player_name not in players_stats_dict:
            players_stats_dict[player_name] = PlayerStats(player_name, row[1])
        
        players_stats_dict[player_name].add_appearance(*row[2:])
    
for player_stats in players_stats_dict.values():
    player_stats.calculate_averages()

for player_stats in players_stats_dict.values():
    player_stats.calculate_advanced()

app = Flask(__name__)
api = Api(app)

def get_player_stats(player_name):
    if player_name in players_stats_dict:
        player = players_stats_dict[player_name]
    
        traditional_stats = {
            "freeThrows": {
                "attempts": f"{player.fta:.1f}",
                "made": f"{player.ftm:.1f}",
                "shootingPercentage": f"{player.ft_percent:.1f}"
            },
            "twoPoints": {
                "attempts": f"{player.twopa:.1f}",
                "made": f"{player.twopm:.1f}",
                "shootingPercentage": f"{player.twp_percent:.1f}"
            },
            "threePoints": {
                "attempts": f"{player.threepa:.1f}",
                "made": f"{player.threepm:.1f}",
                "shootingPercentage": f"{player.threep_percent:.1f}"
            },
            "points":f"{player.points:.1f}",
            "rebounds": f"{player.reb:.1f}",
            "blocks": f"{player.blk:.1f}",
            "assists": f"{player.ast:.1f}",
            "steals": f"{player.stl:.1f}",
            "turnovers": f"{player.tov:.1f}"
        }

        advanced_stats = {
            "valorization": f"{player.valor_index:.1f}",
            "effectiveFieldGoalPercentage": f"{player.eff_fg:.1f}",
            "trueShootingPercentage": f"{player.truesht_eff:.1f}",
            "hollingerAssistRatio": f"{player.holling_as:.1f}"
        }
        response = {
            "playerName": player_name,
            "gamesPlayed": player.appearances,
            "traditional": traditional_stats,
            "advanced": advanced_stats
        }

        response = make_response(json.dumps(response, indent=2), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        error_response = {
            "error":"Player not found"
        }
        response = make_response(json.dumps(error_response), 404)
        response.headers['Content-Type'] = 'application/json'
        return response


class PlayerStatistics(Resource):
    def get(self, player_name):
        return get_player_stats(player_name)

api.add_resource(PlayerStatistics, '/stats/player/<string:player_name>')