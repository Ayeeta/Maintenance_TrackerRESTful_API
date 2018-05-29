import unittest
import json
from run import app

class TDApiEndpoint(unittest.TestCase):

    def setUp(self):
        self.testEndpts = app.test_client(self)
        self.userRequests = [{'id':'maintenance',
                            'item_name':'Sony Vaio',
                            'problem_desc':'anti virus out of date'}]

    def test_all_user_requests(self):
        result = self.testEndpts.get('/user_requests/', data=self.userRequests)
        self.assertEqual(result.status_code, 200)
        

    

    
    

    
