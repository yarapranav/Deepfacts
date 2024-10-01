# Deepfacts
1. Create a file named geonames.json in your project directory and paste the JSON data into it.
2. The data will be read and inserted into your PostgreSQL database using the Python script.
3. Ensure the PostgreSQL database DeepFacts and the places table are created as per the Python script.
4. Run the first Python script to load the data into PostgreSQL.
5. Use the second Python script to query and display the data.
6. You can also display the data in psql command line using commands
Server [localhost]:
Database [postgres]: DeepFacts
Port [5432]:
Username [postgres]:
psql (16.3)
DeepFacts=# SELECT * FROM places;
7. This will display the data in table format
8.  id  |    toponymname     | population
-----+--------------------+------------
   1 | Delhi              |   10927986
   2 | Mumbai             |   12691836
   3 | Kolkata            |    4631392
   4 | Hyder─üb─üd          |    6809970
   5 | Bengaluru          |    8443675
   6 | Chennai            |    4681087
   7 | Ahmedabad          |    6357693
   8 | New Delhi          |     317797
   9 | Pune               |    3124458
  10 | Surat              |    4591246
  11 | Dehra D┼½n          |     522081
  12 | Chand─½garh         |     960787
  13 | Jaipur             |    2711758
  14 | Bhubaneswar        |     837000
  15 | Bhop─ül             |    1599914
  16 | Lucknow            |    2472011
  17 | Kanpur             |    2823249
  18 | Puducherry         |     657209
  19 | Patna              |    1599920
  20 | Ranchi             |    1120374
  21 | Raipur             |     679995
  22 | Thiruvananthapuram |     784153
  23 | Srinagar           |     975857
  24 | Amritsar           |    1092450
  25 | Durgapur           |     518872
  26 | Dhanbad            |    1196214
  27 | Cuttack            |     580000
-- More  --
