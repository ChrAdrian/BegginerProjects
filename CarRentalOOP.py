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
        return now

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
        return now

