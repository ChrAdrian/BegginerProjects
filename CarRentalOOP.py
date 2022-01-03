# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : car rental project using OOP


import datetime


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

        if rental_time != 0 and rental_basis != 0 and number_of_cars != 0:
            self.stock += number_of_cars
            time = datetime.datetime.now()
            rental_period = time - rental_time

            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rental_period.seconds / 3600) * 5 * number_of_cars

            # daily bill calculation
            elif rentalBasis == 2:
                bill = round(rental_period.days) * 20 * number_of_cars

            # weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rental_period.days / 7) * 60 * number_of_cars

            # family discount calculation
            if (3 <= number_of_cars <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7
                print("The total cost would be ${}".format(bill))
                return bill

            else:
                print("You are not found in our registry.")
                return None