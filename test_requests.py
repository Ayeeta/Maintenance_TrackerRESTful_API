import unittest
from classes.usrRequest import *


class TDDUserRequest(unittest.TestCase):

    def setUp(self):
        self.user_req = UserRequest()
        self.user_req.repairlist = []
        self.user_req.maintenancelist = []

    def test_repair_req_appends_to_list(self):
        result = self.user_req.repair_req('sony', 'screen broken')        
        self.assertIn(result, self.user_req.repairlist)
    
    def test_maint_req_appends_to_list(self):
        result = self.user_req.maintenance_req('acer','reinstall avg')
        self.assertIn(result, self.user_req.maintenancelist)

    def test_get_all_returns_dict(self):
        result = self.user_req.getAll()
        self.assertIsInstance(result, dict)
    
    def test_get_repair_all_returns_list(self):
        result = self.user_req.repairAll()
        self.assertIsInstance(result, list)
    
    def test_get_maintenance_all_returns_list(self):
        result = self.user_req.maintenanceAll()
        self.assertIsInstance(result, list)

    def test_edit_repair_method(self):
        self.user_req.editRepair('1','sony','screen crack')
        self.repairlist = [{'prob_id':1, 'item_name':'sony','prob_desc':'screen brkse'}]
        for req in self.repairlist:
            if int('1') == req['prob_id']:
                req['item_name'] = 'sony'
                req['prob_desc'] = 'screen crack'
                self.assertIsInstance(req, dict)

    def test_edit_maintenance_method(self):
        self.user_req.editMaintenance('1','sony','screen crack')
        self.maintenancelist = [{'prob_id':1, 'item_name':'sony','prob_desc':'screen brkse'}]
        for req in self.maintenancelist:
            if int('1') == req['prob_id']:
                req['item_name'] = 'sony'
                req['prob_desc'] = 'screen crack'
                self.assertIsInstance(req, dict)

        
