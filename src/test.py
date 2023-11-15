import unittest
from routes import app
from models.models import PlayerStats
from flask import json

class TestPlayerStats(unittest.TestCase):

    def setUp(self):
        self.player_stats = PlayerStats("Marko Mijailovic", "SG")

    def test_add_apperances(self):
        for i in range(3):
            self.player_stats.add_appearance(i+5, i+10, i+3, i+5, i+1, i+2, i+7, i+1, i+4, i+2, i+3)
        self.assertEqual(self.player_stats.appearances, 3)
        self.assertEqual(self.player_stats.ftm, 18)

    def test_calculate_averages(self):
        for i in range(3):
            self.player_stats.add_appearance(i+5, i+10, i+3, i+5, i+1, i+2, i+7, i+1, i+4, i+2, i+3)
        self.player_stats.calculate_averages()
        self.assertAlmostEqual(self.player_stats.ftm, 6.0)


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_player_stats(self):
        response = self.app.get('/stats/player/Pili Nkruma')  
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['playerName'], 'Pili Nkruma')
        # Add assertions to check the correctness of the response

    def test_get_player_stats_not_found(self):
        response = self.app.get('/stats/player/NonExistingPlayer')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Player not found')

if __name__ == '__main__':
    unittest.main()