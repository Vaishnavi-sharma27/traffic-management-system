# print(" Traffic Management System")

# from database.db_manager import DatabaseManager

# db = DatabaseManager()

# vehicles = db.get_all_vehicles()

# for vehicle in vehicles:
#     print(vehicle)

# db.close()

#from gui.dashboard_old import Dashboard

#print("SMART TRAFFIC MANAGEMENT SYSTEM STARTING...")

#Dashboard()
#from gui.dashboard_old import Dashboard


#if __name__ == "__main__":
 #   Dashboard()

import threading

from gui.dashboard_old import Dashboard
from ai.vehicle_detector import start_detection


if __name__ == "__main__":

    detector_thread = threading.Thread(
        target=start_detection,
        daemon=True
    )

    detector_thread.start()

    Dashboard()