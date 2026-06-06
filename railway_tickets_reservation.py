"""
 Train Ticket Booking System with PNR Number
A simple Python console-based project for beginners
"""

import random
import string
from datetime import datetime

# ─────────────────────────────────────────
#  In-memory "database" (dictionary)
# ─────────────────────────────────────────
bookings = {}  # pnr -> booking details

# ─────────────────────────────────────────
# 🚉 Available Trains
# ─────────────────────────────────────────
TRAINS = {
    "101": {"name": "Rajdhani Express",  "from": "Delhi",   "to": "Mumbai",    "fare": 1500},
    "102": {"name": "Shatabdi Express",  "from": "Chennai", "to": "Bangalore", "fare": 800},
    "103": {"name": "Duronto Express",   "from": "Kolkata", "to": "Delhi",     "fare": 1200},
    "104": {"name": "Godavari Express",  "from": "Vizag",   "to": "Hyderabad", "fare": 450},
}

# ─────────────────────────────────────────
#  PNR Generator
# ─────────────────────────────────────────
def generate_pnr():
    """Generate a unique 10-digit PNR number."""
    digits = ''.join(random.choices(string.digits, k=10))
    return digits

# ─────────────────────────────────────────
#  Show available trains
# ─────────────────────────────────────────
def show_trains():
    print("\n" + "=" * 55)
    print("         AVAILABLE TRAINS")
    print("=" * 55)
    print(f"{'No.':<6} {'Train Name':<22} {'From':<10} {'To':<12} {'Fare'}")
    print("-" * 55)
    for train_no, info in TRAINS.items():
        print(f"{train_no:<6} {info['name']:<22} {info['from']:<10} {info['to']:<12} ₹{info['fare']}")
    print("=" * 55)

# ─────────────────────────────────────────
#  Book a Ticket
# ─────────────────────────────────────────
def book_ticket():
    print("\n  BOOK TICKET")
    show_trains()

    train_no = input("\nEnter Train Number: ").strip()
    if train_no not in TRAINS:
        print(" Invalid train number!")
        return

    passenger_name = input("Enter Passenger Name   : ").strip()
    age            = input("Enter Age              : ").strip()
    seat_class     = input("Seat Class (SL/3A/2A/1A): ").strip().upper()

    if not passenger_name or not age.isdigit():
        print(" Invalid passenger details!")
        return

    # Generate PNR
    pnr = generate_pnr()
    booking_date = datetime.now().strftime("%d-%m-%Y %H:%M")
    train = TRAINS[train_no]

    # Save booking
    bookings[pnr] = {
        "pnr"           : pnr,
        "train_no"      : train_no,
        "train_name"    : train["name"],
        "from_station"  : train["from"],
        "to_station"    : train["to"],
        "passenger_name": passenger_name,
        "age"           : age,
        "seat_class"    : seat_class,
        "fare"          : train["fare"],
        "booking_date"  : booking_date,
        "status"        : "CONFIRMED",
    }

    # Print Ticket
    print("\n" + "=" * 50)
    print("     TICKET BOOKED SUCCESSFULLY!")
    print("=" * 50)
    print(f"  PNR Number     : {pnr}")
    print(f"  Train          : {train['name']} ({train_no})")
    print(f"  From → To      : {train['from']} → {train['to']}")
    print(f"  Passenger      : {passenger_name} (Age: {age})")
    print(f"  Seat Class     : {seat_class}")
    print(f"  Fare           : ₹{train['fare']}")
    print(f"  Booking Date   : {booking_date}")
    print(f"  Status         :  CONFIRMED")
    print("=" * 50)
    print("   Save your PNR to check status later!")

# ─────────────────────────────────────────
#  Check PNR Status
# ─────────────────────────────────────────
def check_pnr():
    print("\n  CHECK PNR STATUS")
    pnr = input("Enter PNR Number: ").strip()

    if pnr in bookings:
        b = bookings[pnr]
        print("\n" + "=" * 50)
        print("     PNR DETAILS")
        print("=" * 50)
        print(f"  PNR Number     : {b['pnr']}")
        print(f"  Train          : {b['train_name']} ({b['train_no']})")
        print(f"  From → To      : {b['from_station']} → {b['to_station']}")
        print(f"  Passenger      : {b['passenger_name']} (Age: {b['age']})")
        print(f"  Seat Class     : {b['seat_class']}")
        print(f"  Fare           : ₹{b['fare']}")
        print(f"  Booking Date   : {b['booking_date']}")
        print(f"  Status         : {b['status']}")
        print("=" * 50)
    else:
        print(" PNR not found! Please check the number.")

# ─────────────────────────────────────────
#  Cancel Ticket
# ─────────────────────────────────────────
def cancel_ticket():
    print("\n  CANCEL TICKET")
    pnr = input("Enter PNR Number to cancel: ").strip()

    if pnr in bookings:
        name = bookings[pnr]["passenger_name"]
        confirm = input(f"Cancel ticket for '{name}'? (yes/no): ").strip().lower()
        if confirm == "yes":
            bookings[pnr]["status"] = "CANCELLED"
            print(f" Ticket with PNR {pnr} has been CANCELLED.")
        else:
            print("Cancellation aborted.")
    else:
        print(" PNR not found!")

# ─────────────────────────────────────────
#  View All Bookings
# ─────────────────────────────────────────
def view_all_bookings():
    if not bookings:
        print("\n No bookings found.")
        return

    print("\n" + "=" * 70)
    print("     ALL BOOKINGS")
    print("=" * 70)
    print(f"{'PNR':<12} {'Name':<18} {'Train':<22} {'Status'}")
    print("-" * 70)
    for pnr, b in bookings.items():
        print(f"{b['pnr']:<12} {b['passenger_name']:<18} {b['train_name']:<22} {b['status']}")
    print("=" * 70)

# ─────────────────────────────────────────
#  Main Menu
# ─────────────────────────────────────────
def main():
    print("\n" + "=" * 50)
    print("    TRAIN TICKET BOOKING SYSTEM")
    print("=" * 50)

    while True:
        print("\n  MAIN MENU")
        print("  1. Book Ticket")
        print("  2. Check PNR Status")
        print("  3. Cancel Ticket")
        print("  4. View All Bookings")
        print("  5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            book_ticket()
        elif choice == "2":
            check_pnr()
        elif choice == "3":
            cancel_ticket()
        elif choice == "4":
            view_all_bookings()
        elif choice == "5":
            print("\n Thank you for using IRCTC Train Booking System. Goodbye!")
            break
        else:
            print(" Invalid choice! Enter 1-5.")

# ─────────────────────────────────────────
# ▶️ Run the program
# ─────────────────────────────────────────
if __name__ == "__main__":
    main()