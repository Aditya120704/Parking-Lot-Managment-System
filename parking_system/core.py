class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.parking_slots = []  # Stack for parked vehicles
        self.waitlist = []  # Queue for waitlisted vehicles

    def park_vehicle(self, vehicle_number):
        if len(self.parking_slots) < self.capacity:
            self.parking_slots.append(vehicle_number)
            return f"Vehicle {vehicle_number} parked."
        else:
            self.waitlist.append(vehicle_number)
            return f"Parking full! Vehicle {vehicle_number} added to the waitlist."

    def remove_vehicle(self, vehicle_number):
        if vehicle_number in self.parking_slots:
            self.parking_slots.remove(vehicle_number)
            message = f"Vehicle {vehicle_number} removed from the parking lot."
            if self.waitlist:
                next_vehicle = self.waitlist.pop(0)
                self.parking_slots.append(next_vehicle)
                message += f" Vehicle {next_vehicle} from waitlist is now parked."
            return message
        else:
            return f"Vehicle {vehicle_number} not found in the parking lot."

    def get_status(self):
        return {
            "capacity": self.capacity,
            "occupied": len(self.parking_slots),
            "available": self.capacity - len(self.parking_slots),
            "parked_vehicles": self.parking_slots,
            "waitlisted_vehicles": self.waitlist
        }
