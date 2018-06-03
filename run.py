from flask import Flask, jsonify, request, make_response
from classes.usrRequest import UserRequest

app = Flask(__name__)
usr = UserRequest()

@app.route('/v1/users/requests', methods = ['GET'])
def return_all_requests():
    return jsonify(usr.getAll())

@app.route('/v1/users/requests/repair', methods = ['GET'])
def return_repair_all():
    return jsonify(usr.repairAll())

@app.route('/v1/users/requests/maintenance', methods = ['GET'])
def return_maintenance_all():
    return jsonify(usr.maintenanceAll())


@app.route('/v1/users/<user_id>/requests/repair', methods = ['POST'])
def create_repair_request(user_id):
    par = request.get_json()      
    usr.repair_req(user_id,par['date'],par['Title'], par['Prob_desc'])
    return jsonify(usr.repairlist)

@app.route('/v1/users/<user_id>/requests/maintenance', methods = ['POST'])
def create_maintenance_request(user_id):
    par = request.get_json()
    if user_id not in usr.maintenancelist:
        usr.maintenance_req(user_id,par['date'],par['Title'], par['Prob_desc'])
    return jsonify(usr.maintenancelist)

@app.route('/v1/users/<user_id>/requests/repair/<prob_id>', methods = ['PUT'])
def modify_repair_req(user_id, prob_id):
    par = request.get_json()
    usr.editRepair(user_id,prob_id, par['Title'], par['Prob_desc'])
    return jsonify(usr.repairlist)    

@app.route('/v1/users/<user_id>/requests/maintenance/<prob_id>', methods = ['PUT'])
def modify_maintenance_req(user_id, prob_id):
    par = request.get_json()
    #if user_id == par['user_id']:
    usr.editMaintenance(user_id,prob_id,par['Title'], par['Prob_desc'])
    return jsonify(usr.maintenancelist)


if __name__ == '__main__':
    app.run(debug=True)