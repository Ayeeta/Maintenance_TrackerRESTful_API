import unittest
import json
from run import app
from app import User

class TDApiEndpoint(unittest.TestCase):

    def setUp(self):
       # self.testEndpts = app.test_client(self)
        
        self.user = User()
        self.user.apiRe = [{'id':'maintenance',
                           'item_name':'Sony vaio',
                           'problem_desc':'anti virus out of date'}]

   # def test_all_user_requests(self):
    #    result = self.testEndpts.get('/user_requests/', data=self.userRequests)
     #   self.assertEqual(result.status_code, 200)
        

    def test_user_get_method_returns_correct_message(self):
        result = self.user.get('id')
        for user in self.user.apiRe:
            if('id' == user['id']):
                self.assertEqual((user,200), result)
        self.assertEqual(result, ('User not found', 404))
    
    #def test_user_put_method_returns_tuple_message




    
    

    
