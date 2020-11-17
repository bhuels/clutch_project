# clutch_project

A python API using Flask to convert an address to geospatial data and identify the state.

Run these commands from a terminal from the same folder as the files are stored.
Folder name must be app to run correctly.

**************************************************************************************
*** Note: Before running you will need to open app.py and put in your personal     ***
***       Google Map API key.                                                      ***
**************************************************************************************

> docker-compose up -d --build

*** Note: this copy command only for windows machines to run this project you will ***
***       need to use local copy command.                                          ***
> docker cp d:\us_geolocator_project\app\us_data.sql app_db_1:/scripts/

> docker exec -it app_db_1 bash

> psql -h localhost -p 5432 -d gis -U docker -f us_data.sql
*** Note: You will need to enter the database password which is "docker".          ***

> exit

You will now be able to use Postman to query the webservice. You must use the syntax:

0.0.0.0:5000/findstate?address=<place address here>

I would suggest including the city for any street address that might be in multiple states.
