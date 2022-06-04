import os
import re
import commands
from parkingLot import ParkingLot


def is_empty(filepath: str) -> bool:
    """
    Check if the file is empty or not
    """
    check_file = os.stat(filepath).st_size
    if check_file == 0:
        return True
    else:
        return False


def is_numeric(ch) -> bool:
    """
    Checks if the character is numeric(i.e. integar >=0) or not
    """
    if isinstance(ch, str) and ch.isnumeric():
        return True
    else:
        return False


def validate_slot_cmd(cmd) -> bool:
    """
    Validates the slot creation command
    """
    if len(cmd) == 2 and cmd[0] == commands.CREATE_PARKING_LOT_CMD and is_numeric(cmd[1]):
        return True
    else:
        raise Exception("Please create the parking lot, before performing any other operation")


def validate_rgn(rgn_number: str) -> bool:
    """
    Validates the registration number
    """
    rgn_pattern = re.compile(r"[A-Z]{2}[--][0-9]{1,2}(?:-[A-Z])?(?:-[A-Z]*)?-[0-9]{4}")
    if re.fullmatch(rgn_pattern, rgn_number):
        return True
    else:
        return False


def validate_park_cmd(cmd) -> bool:
    """
    Validates the park command
    """
    if (
        len(cmd) == 4
        and cmd[0] == commands.PARK_CMD
        and cmd[2] == commands.DRIVER_AGE
        and is_numeric(cmd[3])
        and validate_rgn(cmd[1])
    ):
        return True
    else:
        return False


def validate_slot_frm_age(cmd) -> bool:
    """
    Validates the get slot from age command
    """
    if len(cmd) == 2 and cmd[0] == commands.SLOT_NUMBER_FROM_AGE and is_numeric(cmd[1]):
        return True
    else:
        return False


def validate_slot_from_rgn(cmd) -> bool:
    """
    Validates the get slot from registration command
    """
    if len(cmd) == 2 and cmd[0] == commands.SLOT_NUMBER_FROM_RGN and validate_rgn(cmd[1]):
        return True
    else:
        return False


def validate_leave(cmd) -> bool:
    """
    Validates the leave command
    """
    if len(cmd) == 2 and cmd[0] == commands.LEAVE and is_numeric(cmd[1]):
        return True
    else:
        return False


def validate_vehicle_frm_age(cmd) -> bool:
    """
    Validates the get vehicles from age command
    """
    if len(cmd) == 2 and cmd[0] == commands.VEHICLE_FROM_AGE and is_numeric(cmd[1]):
        return True
    else:
        return False


def process_cmd(p: ParkingLot, cmd: str):
    """
    Processes the command
    """
    cmd = cmd.split()
    if validate_park_cmd(cmd):
        p.park(cmd[1], int(cmd[3]))
    elif validate_slot_frm_age(cmd):
        slots = p.get_slots_from_age(int(cmd[1]))
        print(",".join(map(str, slots)))
    elif validate_slot_from_rgn(cmd):
        slot_num = p.get_slot_from_rgn(cmd[1])
        if slot_num:
            print(slot_num)
        else:
            print(f"Car with vehicle registration number {cmd[1]} is not parked in this parking lot.")
    elif validate_leave(cmd):
        p.vacate(int(cmd[1]))
    elif validate_vehicle_frm_age(cmd):
        rgn_numbers = p.get_rgn_number_from_age(int(cmd[1]))
        print(",".join(map(str, rgn_numbers)))
    else:
        print("Invalid Command")

