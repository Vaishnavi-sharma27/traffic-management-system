import sqlite3
from config import DATABASE_PATH


class DatabaseManager:

    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.connection.cursor()

    def add_vehicle(self, vehicle_no, lane, vehicle_type, entry_time):

        self.cursor.execute(
            """
            INSERT INTO vehicles
            (vehicle_no,lane,vehicle_type,entry_time)
            VALUES (?,?,?,?)
            """,
            (vehicle_no, lane, vehicle_type, entry_time)
        )

        self.connection.commit()

    def get_all_vehicles(self):

        self.cursor.execute(
            "SELECT * FROM vehicles"
        )

        return self.cursor.fetchall()

    def close(self):
        self.connection.close()