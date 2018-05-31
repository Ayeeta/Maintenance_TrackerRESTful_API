from run import app
import unittest
import json
import sys

class TDDEndPoints(unittest.TestCase):

    def test_returns_all(self):
        testClient = app.test_client(self)
        response = testClient.get('http://127.0.0.1:5000/requestAll')
        self.assertEqual(response.status_code, 200)

    def test_returns_all_repair_requests(self):
        testClient = app.test_client(self)
        response = testClient.get('http://127.0.0.1:5000/repair-all')
        self.assertEqual(response.status_code, 200)

    def test_returns_all_maintenance_requests(self):
        testClient = app.test_client(self)
        response = testClient.get('http://127.0.0.1:5000/maintenance-all')
        self.assertEqual(response.status_code, 200)


