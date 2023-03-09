import mysql.connector

# Set up a connection to the MySQL database with incorrect credentials
cnx = mysql.connector.connect(user='wrongusername', password='wrongpassword',
                              hot='host',
                              database='wrongdatabase')

# Create a cursor object to interact with the database
cursor = cnx.cursor()

# Execute an invalid SQL query to retrieve all student records from a non-existent table
query = "SELECT * FROM non_existent_table"
cursor.execute(query)

# Fetch the results of the query from the cursor object
student_records = cursor.fetchall()

# Print out the student records retrieved from the database
for student in student_records:
    print(student)

# Close the cursor and connection
cursor.close()
cnx.close()
