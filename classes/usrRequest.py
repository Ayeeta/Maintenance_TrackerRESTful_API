class UserRequest(object):
    def __init__(self):
        self.repairlist = [{'prob_id':0,'Title':'sony','Prob_desc':'Screen Crack'}]
        self.maintenancelist =[{'prob_id':1,'Title':'Toshiba','Prob_desc':'Antivirus reinstall'}]        
        self.pos.counter = 0

    def repair_req(self, title, desc):
        self.pos =+ 1
        newReq = {'prob_id':self.pos, 'Title':title, 'Prob_desc':desc}
        self.repairlist.append(newReq)
        return newReq

    def maintenance_req(self, title, desc):
        self.pos =+ 1
        newReq = {'prob_id':self.pos, 'Title':title, 'Prob_desc':desc}
        self.maintenancelist.append(newReq)
        return newReq

    def getAll(self):
        return {'repair':self.repairlist, 'maintenance':self.maintenancelist}
        
    
    def repairAll(self):
        return self.repairlist
    
    def maintenanceAll(self):
        return self.maintenancelist

    def editRepair(self, prob_id, item_name, prob_desc):
        for req in self.repairlist:
            if int(prob_id) == req['prob_id']:
                req['Title'] = item_name
                req['prob_desc'] = prob_desc
                return req

    def editMaintenance(self, prob_id, item_name, prob_desc):
        for req in self.maintenancelist:
            if int(prob_id) == req['prob_id']:
                req['Title'] = item_name
                req['prob_desc'] = prob_desc
                return req