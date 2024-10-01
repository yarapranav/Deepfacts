import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname='DeepFacts',  # Replace with your database name
    user='postgres',  # Replace with your username
    password='admin123',  # Replace with your password
    host='localhost',  # Replace with your host (usually localhost)
    port='5432'             # Default PostgreSQL port
)
cursor = conn.cursor()

# Execute a query to fetch data
cursor.execute('SELECT * FROM places;')  # Query to get all data from the table
rows = cursor.fetchall()  # Fetch all rows from the executed query

# Print the fetched data
if rows:
    for row in rows:
        print(row)
else:
    print("No data found!")

# Close the cursor and connection
cursor.close()
conn.close()
