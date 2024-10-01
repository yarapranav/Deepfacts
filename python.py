import json
import psycopg2  # Import psycopg2 for PostgreSQL

# Load the JSON data from file
with open('geonames.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Connect to a PostgreSQL database
conn = psycopg2.connect(
    dbname='DeepFacts',  # Replace with your database name
    user='postgres',    # Replace with your username
    password='admin123', # Replace with your password
    host='localhost',        # Replace with your host (usually localhost)
    port='5432'              # Default PostgreSQL port
)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS places (
    id SERIAL PRIMARY KEY,
    toponymName TEXT,
    population INTEGER
)
''')

# Iterate through the data and insert the required fields into SQL
for item in data.get('geonames', []):
    toponymName = item.get('toponymName')
    population = item.get('population', 0)  # Default to 0 if not present
    cursor.execute('''
    INSERT INTO places (toponymName, population) VALUES (%s, %s)
    ''', (toponymName, population))

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully!")
