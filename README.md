# Maintenance Tracker RESTful API #

[![Build Status](https://travis-ci.org/Ayeeta/Maintenance_TrackerRESTful_API.svg?branch=develop)](https://travis-ci.org/Ayeeta/Maintenance_TrackerRESTful_API)


A set of API end points as defined below

* GET /api/v1/users/requests - Fetch all the requests  

* GET /api/v1/users/requests/repair - Fetch all repair requests 

* GET /api/v1/users/requests/maintenance - Fetch all maintenance requests 

* POST /api/v1/users/<user_id>/requests/repair - Create a repair request. 

* POST /api/v1/users/<user_id>/requests/maintenance - Create a maintenance request.

* PUT /api/v1/users/<user_id>/requests/repair/<prob_id> - Modify a repair request. 

* PUT /api/v1/users/<user_id>/requests/maintenance/<prob_id> - Modify a maintenance request. 



## Pre-requisites ##

* Python
* Flask

### Getting Started ###

* Clone repository
* Install `pip install -r requirements.txt`

### Running tests ###

`nosetests`
`postman` -To test the API end points

### Author ###

Elijah Ayeeta
