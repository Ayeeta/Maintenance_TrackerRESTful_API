from flask import Flask, jsonify, request, make_response
from classes.usrRequest import UserRequest

app = Flask(__name__)
usr = UserRequest()

@app.route('/users/requests', methods = ['GET'])
def return_all_requests():
    return jsonify(usr.getAll())

@app.route('/users/requests/repair', methods = ['GET'])
def return_repair_all():
    return jsonify(usr.repairAll())

@app.route('/users/requests/maintenance', methods = ['GET'])
def return_maintenance_all():
    return jsonify(usr.maintenanceAll())


@app.route('/users/requests/repair', methods = ['POST'])
def create_repair_request():
    par = request.get_json()      
    usr.repair_req(par['Title'], par['Prob_desc'])
    return jsonify(usr.repairlist)
     



@app.route('/users/requests', methods = ['POST'])
def create_maintenance_request():
    pass

@app.route('/users/requests/requestID', methods = ['PUT'])
def modify_repair_req():
    pass

@app.route('/users/requests/requestID', methods = ['PUT'])
def modify_maintenance_req():
    pass


if __name__ == '__main__':
    app.run(debug=True)