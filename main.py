print("Smart Traffic Management System")

from database.db_manager import DatabaseManager

db = DatabaseManager()

vehicles = db.get_all_vehicles()

for vehicle in vehicles:
    print(vehicle)

db.close()

