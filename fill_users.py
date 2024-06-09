import sqlite3
from users import users_data

# Connect to the SQLite database
conn = sqlite3.connect("people.db")
cursor = conn.cursor()

# Insert data into the table
for user in users_data:
    cursor.execute("INSERT INTO userz (user_id, username, password, auth_level) VALUES (?, ?, ?, ?)", 
               (user ["user_id"],user ["username"], user ["password"], user ["auth_level"]))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted successfully.")
