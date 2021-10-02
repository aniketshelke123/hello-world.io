# Following software is used by an employee of a "Bus Tour Booking Company". The computer operator sitting
# for ticket booking.
import random
import pprint
#from twilio.rest import Client
all_booked_tickets = []
all_bus = []
all_driver = []
name_of_buses = ["shalimar", "Khurana", "shivneri", "shiv-shahi", "neeta-bus"]


class TicketBooking:
    customer_name = None
    customer_mob = None
    aboard = None
    destination = None
    ticket_no = None
    date_of_travel = None

    def accept_customer_info(self):
        self.customer_name = input("Enter name of customer: ")
        self.customer_mob = input("Enter customer mobile number: ")
        self.aboard = input("Enter the place of aboard: ")
        self.destination = input("Enter the place of Destination: ")
        self.date_of_travel = input("Enter the date of travel: ")
        self.ticket_no = random.randint(100, 1000)
        self.bus_name = random.choice(name_of_buses)


class Bus:
    bus_name = None
    bus_reg_no = None
    bus_ac_non_ac = None
    sleeper_non_sleeper = None

    def bus_info(self):
        self.bus_name = input("Enter name of bus: ")
        self.bus_reg_no = input("Enter bus registration number: ")
        self.bus_ac_non_ac = input("Enter weather bus is ac or non-ac: ")
        self.sleeper_non_sleeper = input("Enter weather bus is sleeper or no-sleeper: ")


class Driver:
    driver_name = None
    driver_mob = None
    driver_experience = None

    def driver_info(self):
        self.driver_name = input("Enter the name of the driver: ")
        self.driver_mob = input("Enter Driver's mobile number: ")
        self.driver_experience = input("Enter driver's experience: ")


def book_ticket():
    b1 = TicketBooking()
    b1.accept_customer_info()
    all_booked_tickets.append(b1)
    print('=' * 30 + '\n')
    print(">>>  Ticket Booked...!!!")
    print("ticket no. is: ", b1.ticket_no)
    print("Your bus name is: ", b1.bus_name)
    print('\n' + '=' * 30)


def cancel_ticket():
    print('=' * 30 + '\n')
    customer_name = input("Enter name of customer: ")
    for name in all_booked_tickets:
        if name.customer_name == customer_name: # check cust_name in all_booked_tickets = []
            print(f'name = {name.customer_name}, || ticket_no = {name.ticket_no}')
            print("\n>>> Ticket has been cancelled....!!!")
            all_booked_tickets.remove(name)
            break
    else:
        print(">>> No Passenger by this name")
    print('\n' + '=' * 30)


def seat_availability():
    print('=' * 20 + '\n')
    if len(all_booked_tickets) <= 1:
        print(">>> Seat is available....!!!")
    else:
        print(">>> No seat available...!!")
    print('\n' + '=' * 30)


def passenger_details():
    print('=' * 30 + '\n')
    date = input("Enter the date of travel: ")
    for name in all_booked_tickets:
        if name.date_of_travel == date:
            pprint.pprint(f'ticket.no = {name.ticket_no} || name = {name.customer_name} || mob.no = {name.customer_mob}'
                                f' || origin = {name.aboard} || destination = {name.destination} || bus_name = {name.bus_name}')
    print('\n' + '=' * 30)


def send_remainder():
    # account_sid = "AC637c30642ae5835c32fec20938064650"
    # auth_token = "f67e0fd99943a14bcdf8a99c9b3c1c79"
    # client = Client(account_sid, auth_token)
    #
    # message = client.messages \
    #     .create(
    #         body='This is reminder message from library , kindly return the book within 2 days',
    #         from_='+13367153420',
    #         to='+919423873496'
    #     )
    # print(message.sid)
    pass


def add_new_bus():
    b1 = Bus()
    b1.bus_info()
    all_bus.append(b1)
    print('=' * 30 + '\n')
    print(">>>  New bus added successfully...!!!")
    print('\n' + '=' * 30)


def add_new_driver():
    d1 = Driver()
    d1.driver_info()
    all_driver.append(d1)
    print('=' * 30 + '\n')
    print(">>> New driver added....!!!")
    print('\n' + '=' * 30)


while True:

    print("1 - Book Ticket")
    print("2 - Cancel Ticket")
    print("3 - Check Seat availability")
    print("4 - Print All passenger's details on particular date")
    print("5 - Send remainder SMS (about bus departure, before 1 hour)")
    print("6 - Add new Bus")
    print("7 - Add new Driver")
    print("* - Exit")
    ch = input("Enter your choice: ")

    if ch == "1":
        book_ticket()
    elif ch == "2":
        cancel_ticket()
    elif ch == "3":
        seat_availability()
    elif ch == "4":
        passenger_details()
    elif ch == "5":
        #send_remainder()
        pass
    elif ch == "6":
        add_new_bus()
    elif ch == "7":
        add_new_driver()
    elif ch == "*":
        print("Successfully existed...!!!")
        exit(0)
