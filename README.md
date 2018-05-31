# Maintenance Tracker RESTful API #

[![Build Status](https://travis-ci.org/Ayeeta/Maintenance_TrackerRESTful_API.svg?branch=develop)](https://travis-ci.org/Ayeeta/Maintenance_TrackerRESTful_API)


A set of API end points as defined below

* GET/users/requests - Fetch all the requests of a logged in user 

* GET /users/requests/<requestId>  - Fetch a request that belongs to a logged in user 

* GET /users/requests/repair - Fetch all repair requests 

* GET /users/requests/maintenance - Fetch all maintenance requests 

* POST /users/requests - Create a request. 

* PUT /users/requests/<requestId> - Modify a request. 



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
