import unittest
import json
from run import app

class TDApiEndpoint(unittest.TestCase):

    def setUp(self):        
        self.user = User()
        self.user.apiRe = [{'id':'maintenance',
                           'item_name':'Sony vaio',
                           'problem_desc':'anti virus out of date'}]

          

    def test_maintenance_req_get_method_returns_correct_message(self):
        result = self.user.get('id')
        for user in self.user.apiRe:
            if('id' == user['id']):
                self.assertEqual((user,200), result)
        self.assertEqual(result, ('User not found', 404))
    
    def test_maintenance_request_post_method_returns_correct_message(self):
        result  = self.user.post('Toshiba')
        self.assertEqual(result, ('Created', 201)) 

    def test_maintenance_request_put_method_returns_correct_message(self):
        result = self.user.put('id')
        for user in self.user.apiRe:
            if('id'== user['id']):
                self.assertEqual(result, ('Success', 200))       
        

    def test_maintenance_request_delete_method_returns_correct_message(self):
        result = self.user.delete('id')
        self.assertEqual(result, ('Success', 200))




    
    

    
