
import re

RATES = {"bike": 10, "car": 30, "truck": 60}

TIME_PATTERN = re.compile(r"^(?:[01][0-9]|2[0-3]):[0-5][0-9]$")


def minutes_parked(times):
    # Check input type
    if not isinstance(times, str):
        raise TypeError("Time interval must be a string")

    # Check interval structure
    parts = times.strip().split("-")

    if len(parts) != 2:
        raise ValueError("Time interval must contain one '-'")

    entry, exit_time = parts[0].strip(), parts[1].strip()

    # Validate time format and ranges
    if not TIME_PATTERN.fullmatch(entry):
        raise ValueError("Invalid entry time")

    if not TIME_PATTERN.fullmatch(exit_time):
        raise ValueError("Invalid exit time")

    # Convert times into minutes
    h1, m1 = map(int, entry.split(":"))
    h2, m2 = map(int, exit_time.split(":"))

    entry_minutes = h1 * 60 + m1
    exit_minutes = h2 * 60 + m2

    # Reject negative parking duration
    if exit_minutes < entry_minutes:
        raise ValueError("Exit time cannot be earlier than entry time")

    return exit_minutes - entry_minutes


def hourly_rate(vehicle):
    # Check input type
    if not isinstance(vehicle, str):
        raise TypeError("Vehicle type must be a string")

    vehicle = vehicle.strip().lower()

    # Validate vehicle type
    if vehicle not in RATES:
        raise ValueError("Unknown vehicle type")

    return RATES[vehicle]


def format_plate(plate):
    # Check input type
    if not isinstance(plate, str):
        raise TypeError("Number plate must be a string")

    # Validate registration number
    if len(plate) != 10:
        raise ValueError("Number plate must contain exactly 10 characters")

    if not plate.isascii() or not plate.isalnum():
        raise ValueError("Number plate must contain only ASCII letters and digits")

    p = plate.upper()

    return p[:2] + " " + p[2:4] + " " + p[4:6] + " " + p[6:10]


def main():
    print("==== Running minutes_parked ====")
    user_input = input("Enter entry and exit time (e.g. 09:30-11:45): ")
    result = minutes_parked(user_input)
    print("Minutes Parked:", result)

    print("\n==== Running hourly_rate ====")
    user_input = input("Enter vehicle type (bike/car/truck): ")
    result = hourly_rate(user_input)
    print("Hourly Rate:", result)

    print("\n==== Running format_plate ====")
    user_input = input("Enter a number plate (e.g. ka01ab1234): ")
    result = format_plate(user_input)
    print("Formatted Plate:", result)


if __name__ == "__main__":
    main()

