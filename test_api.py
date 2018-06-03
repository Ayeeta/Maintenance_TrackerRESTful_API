import unittest
import json
from run import app

class TestAPIEndPoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
    

    def test_get_all_requests_returns_correct_message(self):
        result = self.app.get('/api/v1/users/requests')
        self.assertEqual(result.status_code, 200)

    def test_get_all_repair_requests(self):
        result = self.app.get('/api/v1/users/requests/repair')
        self.assertEqual(result.status_code, 200)

    def test_get_all_maintenance_requests(self):
        result = self.app.get('/api/v1/users/requests/maintenance')
        self.assertEqual(result.status_code, 200)

    def test_post_repair_bad_request(self):
        result = self.app.post('/api/v1/users/<user_id>/requests/repair', data={
                                                                         "user_id":"1",
                                                                         "date":"12/03/2018",
                                                                          "prob_id":"1",
                                                                          "Title":"sony",
                                                                          "Prob_desc":"peoble"
                                                                          }, content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_post_maintenance_bad_request(self):
        result = self.app.post('/api/v1/users/<user_id>/requests/maintenance', data={
                                                                                      "user_id":"1",
                                                                                      "date":"12/03/2018",
                                                                                      "prob_id":"1",
                                                                                      "Title":"sony",
                                                                                      "Prob_desc":"peoble"
                                                                                    }, content_type='application/json')
        self.assertEqual(result.status_code, 400)

    