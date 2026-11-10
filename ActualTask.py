
from datetime import datetime

# Available restaurant tables and their seating capacities
TABLE_CAPACITIES = {
    1: 2,
    2: 2,
    3: 4,
    4: 4,
    5: 6
}


# Function 1: Check table availability
def check_slot(booking_date, booking_time, bookings, guests=1):

    # Validate date and time formats
    datetime.strptime(booking_date, "%d-%m-%Y")
    datetime.strptime(booking_time, "%H:%M")

    if not isinstance(guests, int) or isinstance(guests, bool) or guests < 1 or guests > 6:
        raise ValueError("Guest count must be between 1 and 6.")

    booked_tables = []

    for booking in bookings:
        if (booking["date"] == booking_date and
                booking["time"] == booking_time):
            booked_tables.append(booking["table_no"])

    for table_no, capacity in TABLE_CAPACITIES.items():
        if capacity >= guests and table_no not in booked_tables:
            return table_no

    return None


# Function 2: Make a restaurant reservation
def make_booking(name, booking_date, booking_time, guests, bookings):

    if not name.strip():
        raise ValueError("Customer name cannot be empty.")

    if not isinstance(guests, int) or isinstance(guests, bool) or guests < 1 or guests > 6:
        raise ValueError("Guests must be between 1 and 6.")

    table_no = check_slot(booking_date, booking_time, bookings, guests)

    if table_no is None:
        return None

    booking_id = max(
        [b["booking_id"] for b in bookings],
        default=1000
    ) + 1

    new_booking = {
        "booking_id": booking_id,
        "name": name.strip(),
        "date": booking_date,
        "time": booking_time,
        "guests": guests,
        "table_no": table_no
    }

    bookings.append(new_booking)

    return new_booking

# Function 3: Cancel an existing reservation
def cancel_booking(booking_id, bookings):

    for booking in bookings:
        if booking["booking_id"] == booking_id:
            bookings.remove(booking)
            return True

    return False

# Function 4: Display all reservations
def display_bookings(bookings):

    return sorted(
        bookings,
        key=lambda b: (
            datetime.strptime(b["date"], "%d-%m-%Y"),
            b["time"]
        )
    )
