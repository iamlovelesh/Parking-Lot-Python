import sys
import os
from utils import is_empty, validate_slot_cmd, process_cmd
from parkingLot import ParkingLot


def main():
    if not os.path.exists("input.txt"):
        raise Exception("Please create the input.txt file.")
    sys.stdin = open("input.txt", "r")
    if is_empty("input.txt"):
        return
    cmd = input()
    cmd = cmd.split()
    if validate_slot_cmd(cmd):
        slots_count = int(cmd[1])

    p = ParkingLot(slots_count)
    while True:
        try:
            cmd = input()
            process_cmd(p, cmd)
        except EOFError:
            break

if __name__ == "__main__":
    main()

