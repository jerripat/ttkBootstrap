import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('presidents.db')
cursor = conn.cursor()

# Drop existing Presidents table
cursor.execute("DROP TABLE IF EXISTS Presidents")

# Create Presidents table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Presidents (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    inauguration_date TEXT,
                    inaugYear INTEGER,
                    endDate TEXT,
                    termEnd INTEGER,
                    vice_president TEXT
                  )''')

# Open and read from the text file
with open('presidents.txt', 'r') as file:
    presidential_data = file.readlines()

# Insert data into the database using a for loop
for line in presidential_data:
    data = line.strip().split(',')
    cursor.execute('''INSERT INTO Presidents (name, inauguration_date, inaugYear, endDate, termEnd, vice_president)
                      VALUES (?, ?, ?, ?, ?, ?)''', data)

# Commit changes and close connection
conn.commit()
conn.close()
