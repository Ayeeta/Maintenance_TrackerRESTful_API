from flask import Flask, jsonify, request, make_response
from classes.usrRequest import UserRequest

app = Flask(__name__)
usr = UserRequest()

@app.route('/requestAll', methods = ['GET'])
def return_all_requests():
    return jsonify(usr.getAll())

@app.route('/repair-all', methods = ['GET'])
def return_repair_all():
    return jsonify(usr.repairAll())

@app.route('/maintenance-all', methods = ['GET'])
def return_maintenance_all():
    return jsonify(usr.maintenanceAll())


@app.route('/create_repair', methods = ['POST'])
def create_repair_request():
    test = request.get_json()
    
    test2 = {'prob_id':0,'Title':test['Title'],'Prob_desc':test['Prob_desc']}
    usr.repairlist.append(test2)
    return jsonify(usr.repairlist)
     



@app.route('/', methods = ['GET','POST'])
def create_maintenance_request():
    pass

@app.route('/', methods = ['GET', 'POST'])
def modify_repair_req():
    pass

@app.route('/', methods = ['GET', 'POST'])
def modify_maintenance_req():
    pass


if __name__ == '__main__':
    app.run(debug=True)