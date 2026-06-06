import tkinter as tk


class Dashboard:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Smart Traffic Management System")

        self.root.geometry("900x600")

        self.heading = tk.Label(
            self.root,
            text="SMART TRAFFIC MANAGEMENT SYSTEM",
            font=("Arial", 22, "bold")
        )

        self.heading.pack(pady=20)

        self.lane_a = tk.Label(
            self.root,
            text="Lane A : 15 Vehicles",
            font=("Arial", 16)
        )

        self.lane_a.pack(pady=10)

        self.lane_b = tk.Label(
            self.root,
            text="Lane B : 40 Vehicles",
            font=("Arial", 16)
        )

        self.lane_b.pack(pady=10)

        self.lane_c = tk.Label(
            self.root,
            text="Lane C : 25 Vehicles",
            font=("Arial", 16)
        )

        self.lane_c.pack(pady=10)

        self.lane_d = tk.Label(
            self.root,
            text="Lane D : 70 Vehicles",
            font=("Arial", 16)
        )

        self.lane_d.pack(pady=10)

        self.active_lane = tk.Label(
            self.root,
            text="Active Signal : Lane D",
            font=("Arial", 18, "bold")
        )

        self.active_lane.pack(pady=20)

        self.root.mainloop()


Dashboard()