from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Vehicle:
    slot_id: int
    registration_number: str
    driver_age: int


class ParkingLot:
    def __init__(self, slots_count: int):
        """
        slots_count : The maximum number of vehicles that can be parked.
        vacated_slots: List of the slots which are vacated
        vehicles: List of vehicles that are present in the parking lot.
        """
        self.slots_count: int = slots_count
        self.vacated_slots: List[int] = []
        self.vehicles: List[Vehicle] = []
        print(f"Created parking of {self.slots_count} slots")

    def park(self, rgn_number: str, age: int):
        """
        Park the cars into the parking lot. 
        If there is any vacate slot, the priority is given to that slot
        else the car is parked at the last slot availalbe
        """
        if self.full():
            print("Parking lot is full")
        elif self.get_slot_from_rgn(rgn_number):
            print(f"Car with vehicle registration number {rgn_number} is already parked.")
        else:
            if self.vacated_slots:
                vehicle = Vehicle(slot_id=self.vacated_slots[0], registration_number=rgn_number, driver_age=age)
                self.vehicles.append(vehicle)
                self.vacated_slots.pop(0)
            else:
                vehicle = Vehicle(slot_id=len(self.vehicles) + 1, registration_number=rgn_number, driver_age=age)
                self.vehicles.append(vehicle)
            print(
                f'Car with vehicle registration number "{vehicle.registration_number}" has been parked at slot number {vehicle.slot_id}'
            )

    def full(self) -> bool:
        """
        Checks if parking lot is full
        """
        return len(self.vehicles) == self.slots_count

    def empty(self) -> bool:
        """
        Checks if parking lot is empty
        """
        return len(self.vehicles) == 0

    def get_slots_from_age(self, age: int) -> List[int]:
        """
        Returns all the slots from age
        """
        res = [vehicle.slot_id for vehicle in self.vehicles if vehicle.driver_age == age]
        return res

    def get_slot_from_rgn(self, rgn_number: str) -> Optional[int]:
        """
        Returns the slots from the registration number
        """
        vehicles = list(filter(lambda vehicle: vehicle.registration_number == rgn_number, self.vehicles))
        if vehicles:
            return vehicles[0].slot_id

    def vacate(self, slot_number: int):
        """
        Vactes the slot with the slot number. 
        If the slot number is not valid print the error msg
        """
        error_msg = "Please provide the valid slot number to vacate the car"
        if self.slots_count < slot_number:
            print(error_msg)
            return
        removed_vehicle = None
        vehicle_index = None
        for index, vehicle in enumerate(self.vehicles):
            if vehicle.slot_id == slot_number:
                removed_vehicle = vehicle
                vehicle_index = index
                break
        if removed_vehicle:
            self.vehicles.pop(vehicle_index)
            self.vacated_slots.append(removed_vehicle.slot_id)
            print(
                f'Slot number {slot_number} vacated, the car with vehicle registration number "{removed_vehicle.registration_number}" left the space, the driver of the car was of age {removed_vehicle.driver_age}'
            )
        else:
            print("Slot already vacant")

    def get_rgn_number_from_age(self, age: int) -> List[str]:
        res = [vehicle.registration_number for vehicle in self.vehicles if vehicle.driver_age == age]
        return res

