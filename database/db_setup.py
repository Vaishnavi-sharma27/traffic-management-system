import sqlite3

conn = sqlite3.connect("database/traffic.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehicles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_no TEXT,
    lane TEXT,
    vehicle_type TEXT,
    entry_time TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS signals(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lane TEXT,
    green_time INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ambulance_logs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lane TEXT,
    timestamp TEXT
)
""")

conn.commit()
conn.close()

print("Database Created")