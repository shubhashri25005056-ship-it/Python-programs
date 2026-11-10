
# Import functions from our user-defined package
from tablebook_pkg import (
    check_slot,
    make_booking,
    cancel_booking,
    display_bookings
)

# List to store all restaurant reservations
bookings = []


# Main program
while True:

    print("\n===================================")
    print("     RESTAURANT TABLE BOOKING")
    print("===================================")
    print("1. Check Table Availability")
    print("2. Make a Reservation")
    print("3. Cancel a Reservation")
    print("4. Display All Reservations")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    try:

        # Option 1: Check table availability
        if choice == "1":

            date = input("Enter date (DD-MM-YYYY): ")
            time = input("Enter time (HH:MM): ")
            guests = int(input("Enter number of guests: "))

            table = check_slot(date, time, bookings, guests)

            if table is not None:
                print("\nTable", table, "is available!")
            else:
                print("\nSorry! No suitable table is available.")

        # Option 2: Make a reservation
        elif choice == "2":

            name = input("Enter customer name: ")
            date = input("Enter date (DD-MM-YYYY): ")
            time = input("Enter time (HH:MM): ")
            guests = int(input("Enter number of guests: "))

            booking = make_booking(
                name, date, time, guests, bookings
            )

            if booking:
                print("\nReservation Successful!")
                print("Booking ID:", booking["booking_id"])
                print("Customer Name:", booking["name"])
                print("Date:", booking["date"])
                print("Time:", booking["time"])
                print("Number of Guests:", booking["guests"])
                print("Table Number:", booking["table_no"])

            else:
                print("\nSorry! No suitable table is available.")

        # Option 3: Cancel a reservation
        elif choice == "3":

            booking_id = int(input("Enter Booking ID: "))

            if cancel_booking(booking_id, bookings):
                print("\nReservation cancelled successfully.")
            else:
                print("\nBooking ID not found.")

        # Option 4: Display all reservations
        elif choice == "4":

            all_bookings = display_bookings(bookings)

            if not all_bookings:
                print("\nNo reservations found.")

            else:
                print("\n========== RESERVATION DETAILS ==========")

                for booking in all_bookings:
                    print("-----------------------------------------")
                    print("Booking ID:", booking["booking_id"])
                    print("Customer:", booking["name"])
                    print("Date:", booking["date"])
                    print("Time:", booking["time"])
                    print("Guests:", booking["guests"])
                    print("Table Number:", booking["table_no"])

        # Option 5: Exit the program
        elif choice == "5":

            print("\nThank you for using our booking system!")
            break

        # Invalid menu choice
        else:
            print("\nInvalid choice! Please select between 1 and 5.")

    except ValueError as error:
        print("\nInvalid input:", error)
