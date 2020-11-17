# clutch_project

A python API using Flask to convert an address to geospatial data and identify the state.

Run these commands from a terminal in the app folder.

docker-compose up -d --build

*** Note: this is only for windows machines ***
docker cp d:\us_geolocator_project\src\us_data.sql postgis:/scripts/

docker exec -it postgis bash

psql -h localhost -p 5432 -d gis -U docker -f us_data.sql

exit
