from abstract_class import *


class Bicycle(Rider):

    def __init__(self):
        self.ride = "Human powered, not enclosed"
        self.riders = "1 or 2 if tandem or a daredevil"

    def ride(self):
        return self.ride

    def riders(self):
        return self.riders

    def __str__(self):
        return str(self.ride(), "\n", self.riders())

    def __repr__(self):
        return str(self.ride(), "\n", self.riders())


class Motorcycle(Rider):

    def __init__(self):
        self.ride = "Engine powered, not enclosed"
        self.riders = "1 or 2"

    def ride(self):
        return self.ride

    def riders(self):
        return self.riders

    def __str__(self):
        return str(self.ride(), "\n", self.riders())

    def __repr__(self):
        return str(self.ride(), "\n", self.riders())


class Car(Rider):

    def __init__(self):
        self.ride = "Engine powered, enclosed"
        self.riders = "1 plus comfortably"

    def ride(self):
        return self.ride

    def riders(self):
        return self.riders

    def __str__(self):
        return f"{self.ride()}\n{self.riders()}"

    def __repr__(self):
        return f"{self.ride()}\n{self.riders()}"

    def display(self):
        return f"{self.ride()}\n{self.riders()}"
