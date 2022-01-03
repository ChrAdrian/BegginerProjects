# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : car rental project using OOP


from datetime import datetime, timedelta


class CarRental:
    def __init__(self, stock=0):
        self.stock = stock

    def display_stock(self):
        print("The numbers of cars in stock is: {}".format(self.stock))
        return slef.stock

    def rent_car_by_hour(self, nr_of_cars):
        if nr_of_cars < 0:
            print("The number of cars should be positive!")
            return None
        elif n > self.stock:
            print("Sorry, we currently have {} cars available!".format(self.stock))
            return None
        else:
            time = datetime.datetime.now()
            print("You have rented a number of {} cars starting at {} hours".format(nr_of_cars, time.hour))
            self.stock -= nr_of_cars
        return time

    def rent_car_by_day(self, nr_of_cars):
        if nr_of_cars < 0:
            print("The number of cars should be positive!")
            return None
        elif n > self.stock:
            print("Sorry, we currently have {} cars available!".format(self.stock))
            return None
        else:
            time = datetime.datetime.now()
            print("You have rented a number of {} cars on daily basis today starting at {} hours".format(nr_of_cars, time))
            self.stock -= nr_of_cars
        return time

    def rent_car_by_week(self, nr_of_cars):
        if nr_of_cars < 0:
            print("The number of cars should be positive!")
            return None
        elif n > self.stock:
            print("Sorry, we currently have {} cars available!".format(self.stock))
            return None
        else:
            time = datetime.datetime.now()
            print("You have rented a number of {} cars on weekly basis today starting at {} hours".format(nr_of_cars, time))
            self.stock -= nr_of_cars
        return time

    def return_car(self, request):
        rental_time, rental_basis, number_of_cars = request
        bill = 0

        if rental_time and rental_basis and number_of_cars:
            self.stock += number_of_cars
            time = datetime.now()
            rental_period = time - rental_time

            # hourly bill calculation
            if rental_basis == 1:
                bill = round(rental_period.seconds / 3600) * 5 * number_of_cars

            # daily bill calculation
            elif rental_basis == 2:
                bill = round(rental_period.days) * 20 * number_of_cars

            # weekly bill calculation
            elif rental_basis == 3:
                bill = round(rental_period.days / 7) * 60 * number_of_cars

            # family discount calculation
            if 3 <= number_of_cars <= 5:
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7
                print("The total cost would be ${}".format(bill))
                return bill

        else:
            print("You are not found in our registry.")
            return None


class Customer:
    def __init__(self):
        self.cars = 0
        self.rental_basis = 0
        self.rental_time = 0
        self.bill = 0

    def request_car(self):
        cars = input("How many cars would you like to rent?")

        # implement logic for invalid input
        try:
            cars = int(cars)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        if cars < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.cars = cars
        return self.cars

    def return_car(self):
        if self.rental_basis and self.rental_time and self.cars:
            return self.rental_time, self.rental_basis, self.cars
        else:
            return 0, 0, 0


customer = Customer()
customer.rental_basis = 1
customer.cars = 0
customer.rental_time = 0
print(customer.return_car())

now = datetime.now()
customer.rental_time = now
customer.rental_basis = 1
customer.cars = 4
print(customer.return_car())
