import sqlite3

# Connect to the SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('pool_matches.db')

# Create a cursor object
cursor = conn.cursor()

# Create the matches table
cursor.execute('''
CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player1 TEXT NOT NULL,
    player2 TEXT NOT NULL,
    winner TEXT NOT NULL
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()
