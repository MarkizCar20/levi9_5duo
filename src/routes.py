from flask import Flask
from flask_restful import Resource, Api
from models.models import PlayerStats
import csv

players_stats_dict = {}

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

for player_name, player_stats in players_stats_dict.items():
    print(f"Player: {player_name}")
    print(f"Position: {player_stats.position}")
    print(f"Average FTM: {player_stats.ftm}")
    print(f"Average FTA: {player_stats.fta}")
    print(f"Average Two-Pointers Made: {player_stats.twopm}")
    print(f"Average Two-Pointers Attempted: {player_stats.twopa}")
    print(f"Average Three-Pointers Made: {player_stats.threepm}")
    print(f"Average Three-Pointers Attempted: {player_stats.threepa}")
    print(f"Average Rebounds: {player_stats.reb}")
    print(f"Average Blocks: {player_stats.blk}")
    print(f"Average Assists: {player_stats.ast}")
    print(f"Average Steals: {player_stats.stl}")
    print(f"Average Turnovers: {player_stats.tov}")
    print("-" * 20)



app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return { 'hello':'world' }

class PlayerStatistics(Resource):
    def get(self, player_name):
        return { 'data' : 'player_one'}

api.add_resource(HelloWorld, '/')
api.add_resource(PlayerStatistics, '/stats/player/<string:player_name>')