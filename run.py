from flask import Flask, jsonify, request, make_response




app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def return_all_requests():
    pass

@app.route('/', methods = ['GET','POST'])
def create_repair_request():
    pass

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