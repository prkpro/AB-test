# Yara 
PROCESS FOLLOWED:
1. Extracting and Cleaning the csv data.
	a) Checked for Non-numeric(lat,lng) value in user_location
	b) Removed rows Nan values
2. Loading the raw data to the PostgreSQL server.
3. Derived a Staging table for both "user_location" and "world_cities" (with derived geometry column).
4. Queries and Stored closest city with distance to DER_Nearest_distance (This will fulfill Task 1.3 and Task 1.4).
5. Grouped all users along with nearest city and corresponding
distance.
6. Queried and stored histogram.

IN THE REPO:
1. Queries Folder
	Queries.sql (Task 1.3 and 1.4)(Task 2)
2. Queries Output
	STG_User_locations(limit 100).csv
	STG_World_Cities.csv
	Minium_distance_for_each_location(limit 100).csv
	Minium_distance_for_each_user(limit 100).csv
	Histogram_on_distance.csv
3. Yara_data
	user_location.csv
	world_cities.csv
4. app.py (Task 4)
5. main.py (Task 1.1 and 1.2)
6. readme.md
7. Requirement.txt (Auto generated)

STEPS : 

1. cd to the directory where requirements.txt is located
2. activate your virtualenv
3. run: "pip install -r requirements.txt"
4. run: "python main.py"
5. open SQL Shell(psql) run: "Queries.sql"
6. run: "flask run"