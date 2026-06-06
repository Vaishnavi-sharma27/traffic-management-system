import tkinter as tk
from controllers.smart_controller import SmartController


class Dashboard:

    def __init__(self):

        self.controller = SmartController()

        # Dummy Data (Testing)
        self.controller.update_lane("A", 5)
        self.controller.update_lane("B", 10)
        self.controller.update_lane("C", 15)
        self.controller.update_lane("D", 20)

        self.root = tk.Tk()

        self.root.title("Smart Traffic Management System")

        self.root.geometry("1200x900")
        self.root.state("zoomed")

        self.root.configure(bg="#f0f0f0")

        self.create_widgets()

        self.update_dashboard()

        self.root.mainloop()

    def create_widgets(self):

        self.heading = tk.Label(
            self.root,
            text="SMART TRAFFIC MANAGEMENT SYSTEM",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0"
        )

        self.heading.pack(pady=10)

        self.cards_frame = tk.Frame(
            self.root,
            bg="#f0f0f0"
        )

        self.cards_frame.pack(pady=20)

        self.lane_a = self.create_lane_card(
            self.cards_frame,
            "LANE A",
            0,
            0
        )

        self.lane_b = self.create_lane_card(
            self.cards_frame,
            "LANE B",
            0,
            1
        )

        self.lane_c = self.create_lane_card(
            self.cards_frame,
            "LANE C",
            1,
            0
        )

        self.lane_d = self.create_lane_card(
            self.cards_frame,
            "LANE D",
            1,
            1
        )

        self.active_lane_label = tk.Label(
            self.root,
            text="Active Lane : None",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0"
        )

        self.active_lane_label.pack(pady=20)
        self.system_status = tk.Label(
             self.root,
             text="System Status : RUNNING",
             font=("Arial", 14, "bold"),
             fg="green",
             bg="#f0f0f0"
        )

        self.system_status.pack(pady=5)

        self.detection_status = tk.Label(
             self.root,
             text="Detection Status : ACTIVE",
             font=("Arial", 14, "bold"),
             fg="blue",
            bg="#f0f0f0"
        )

        self.detection_status.pack(pady=5)
        self.emergency_label = tk.Label(
            self.root,
            text="Emergency Status : OFF",
            font=("Arial", 16),
            bg="#f0f0f0"
        )

        self.emergency_label.pack(pady=10)

        self.button_frame = tk.Frame(
            self.root,
            bg="#f0f0f0"
        )
        print("BUTTON FRAME CREATED")
        self.button_frame.pack(pady=20)

        self.ambulance_btn = tk.Button(
            self.button_frame,
            text="Activate Ambulance Lane B",
            command=self.activate_ambulance,
            width=25,
            height=2
        )

        self.ambulance_btn.grid(
            row=0,
            column=0,
            padx=10
        )

        self.reset_btn = tk.Button(
            self.button_frame,
            text="Reset Emergency",
            command=self.reset_emergency,
            width=25,
            height=2
        )

        self.reset_btn.grid(
            row=0,
            column=1,
            padx=10
        )

    def create_lane_card(
        self,
        parent,
        lane_name,
        row,
        column
    ):

        frame = tk.Frame(
            parent,
            width=220,
            height=110,
            bd=2,
            relief="solid",
            bg="white"
        )

        frame.grid(
            row=row,
            column=column,
            padx=10,
            pady=10
        )

        frame.grid_propagate(False)

        title = tk.Label(
            frame,
            text=lane_name,
            font=("Arial", 16, "bold"),
            bg="white"
        )

        title.pack(pady=5)

        count_label = tk.Label(
            frame,
            text="Vehicles : 0",
            font=("Arial", 14),
            bg="white"
        )

        count_label.pack(pady=2)

        signal_label = tk.Label(
            frame,
            text="Signal : RED",
            font=("Arial", 14, "bold"),
            bg="white"
        )

        signal_label.pack(pady=2)

        return {
            "frame": frame,
            "count": count_label,
            "signal": signal_label
        }

    def update_dashboard(self):

        lanes = self.controller.signal_controller.get_all_lanes()

        self.lane_a["count"].config(
            text=f"Vehicles : {lanes.get('A',0)}"
        )

        self.lane_b["count"].config(
            text=f"Vehicles : {lanes.get('B',0)}"
        )

        self.lane_c["count"].config(
            text=f"Vehicles : {lanes.get('C',0)}"
        )

        self.lane_d["count"].config(
            text=f"Vehicles : {lanes.get('D',0)}"
        )

        active_lane = self.controller.get_active_lane()

        self.active_lane_label.config(
            text=f"Active Lane : {active_lane}"
        )

        self.reset_signals()
        self.lane_a["frame"].config(bg="white")
        self.lane_b["frame"].config(bg="white")
        self.lane_c["frame"].config(bg="white")
        self.lane_d["frame"].config(bg="white")

        if active_lane == "A":
            self.lane_a["frame"].config(bg="lightgreen")
            self.lane_a["signal"].config(
                text="Signal : GREEN",
                fg="green"
            )

        elif active_lane == "B":
            self.lane_b["frame"].config(bg="lightgreen")
            self.lane_b["signal"].config(
                text="Signal : GREEN",
                fg="green"
            )

        elif active_lane == "C":
            self.lane_c["frame"].config(bg="lightgreen")
            self.lane_c["signal"].config(
                text="Signal : GREEN",
                fg="green"
            )

        elif active_lane == "D":
            self.lane_d["frame"].config(bg="lightgreen")
            self.lane_d["signal"].config( 
                text="Signal : GREEN",
                fg="green"
               
            )

    def reset_signals(self):
          
        self.lane_a["signal"].config(
            text="Signal : RED",
            fg="red"
             
        )
        
        self.lane_b["signal"].config(
            text="Signal : RED",
            fg="red"
        )

        self.lane_c["signal"].config(
            text="Signal : RED",
            fg="red"
        )

        self.lane_d["signal"].config(
            text="Signal : RED",
            fg="red"
        )

    def activate_ambulance(self):

        self.controller.activate_ambulance("B")

        self.emergency_label.config(
            text="Emergency Status : ON"
        )

        self.update_dashboard()

    def reset_emergency(self):

        self.controller.emergency_controller.deactivate_emergency()

        self.emergency_label.config(
            text="Emergency Status : OFF"
        )

        self.update_dashboard()


Dashboard()