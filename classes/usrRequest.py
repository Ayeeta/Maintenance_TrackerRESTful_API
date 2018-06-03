class UserRequest(object):
    def __init__(self):
        self.repairlist = [{'user_id':'u24','date':'12/05/2018','prob_id':0,'Title':'sony','Prob_desc':'Screen Crack'}]
        self.maintenancelist =[{'user_id':'u24','date':'12/05/2018','prob_id':1,'Title':'Toshiba','Prob_desc':'Antivirus reinstall'}]        
        #self.pos = 0

    def repair_req(self,user_id, date, prob_id, title, desc):
        #self.pos =+ 1
        newReq = {'user_id':user_id,'date':date,'prob_id':prob_id, 'Title':title, 'Prob_desc':desc}
        self.repairlist.append(newReq)
        return newReq

    def maintenance_req(self,user_id, date, prob_id, title, desc):
        #self.pos =+ 1
        newReq = {'user_id':user_id,'date':date,'prob_id':prob_id, 'Title':title, 'Prob_desc':desc}
        self.maintenancelist.append(newReq)
        return newReq

    def getAll(self):
        return {'repair':self.repairlist, 'maintenance':self.maintenancelist}
        
    
    def repairAll(self):
        return self.repairlist
    
    def maintenanceAll(self):
        return self.maintenancelist

    def editRepair(self,user_id, prob_id, item_name, prob_desc):
        for req in self.repairlist:
            if int(prob_id) == req['prob_id'] and user_id == req['user_id']:
                req['Title'] = item_name
                req['Prob_desc'] = prob_desc
                return req

    def editMaintenance(self,user_id, prob_id, item_name, prob_desc):
        for req in self.maintenancelist:
            if int(prob_id) == req['prob_id']:
                req['Title'] = item_name
                req['Prob_desc'] = prob_desc
                return req