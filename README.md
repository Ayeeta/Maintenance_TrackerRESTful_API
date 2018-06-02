# Maintenance Tracker RESTful API #

[![Build Status](https://travis-ci.org/Ayeeta/Maintenance_TrackerRESTful_API.svg?branch=develop)](https://travis-ci.org/Ayeeta/Maintenance_TrackerRESTful_API)


A set of API end points as defined below

* GET/users/requests - Fetch all the requests  

* GET /users/requests/repair - Fetch all repair requests 

* GET /users/requests/maintenance - Fetch all maintenance requests 

* POST /users/requests/repair - Create a repair request. 

* POST /users/requests/maintenance - Create a maintenance request.

* PUT /users/requests/repair/<post_id> - Modify a repair request. 

* PUT /users/requests/maintenance/<post_id> - Modify a maintenance request. 



## Pre-requisites ##

* Python
* Flask

### Getting Started ###

* Clone repository
* Install `pip install -r requirements.txt`

### Running tests ###

`nosetests`

### Authors ###

Elijah Ayeeta
