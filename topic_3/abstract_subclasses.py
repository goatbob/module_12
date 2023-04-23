"""
program: abstract_subclasses.py
author: kyle godwin
last date modified: 11 april 2023

Subclasses Bicycle, Motorcycle, and Car
of abstract base class Rider.
"""

from topic_3.abstract_class import Rider


class Bicycle(Rider):
    """Bicycle subclass of Rider base class"""

    def __init__(self):
        self.ride_str = "Human powered, not enclosed"
        self.riders_str = "1 or 2 if tandem or a daredevil"

    def ride(self):  # overwrite ride abstract function
        return self.ride_str

    def riders(self):  # overwrite riders abstract function
        return self.riders_str

    def __str__(self):  # string representation
        return f"{self.ride()}\n{self.riders()}"

    def __repr__(self):  # repr representation
        return f"{self.ride()}\n{self.riders()}"


class Motorcycle(Rider):
    """Motorcycle subclass of Rider base class"""

    def __init__(self):
        self.ride_str = "Engine powered, not enclosed"
        self.riders_str = "1 or 2"

    def ride(self):  # overwrite ride abstract function
        return self.ride_str

    def riders(self):  # overwrite riders abstract function
        return self.riders_str

    def __str__(self):  # string representation
        return f"{self.ride()}\n{self.riders()}"

    def __repr__(self):  # repr representation
        return f"{self.ride()}\n{self.riders()}"


class Car(Rider):
    """Car subclass of Rider base class"""

    def __init__(self):
        self.ride_str = "Engine powered, enclosed"
        self.riders_str = "1 plus comfortably"

    def ride(self):  # overwrite ride abstract function
        return self.ride_str

    def riders(self):  # overwrite riders abstract function
        return self.riders_str

    def __str__(self):  # string representation
        return f"{self.ride()}\n{self.riders()}"

    def __repr__(self):  # repr representation
        return f"{self.ride()}\n{self.riders()}"

    def display(self):
        return f"{self.ride()}\n{self.riders()}"


if __name__ == "__main__":
    b = Bicycle()
    print(str(b))
    print(b.ride())
    del b

    m = Motorcycle()
    print(str(m))
    print(m.riders())
    del m

    c = Car()
    print(str(c))
    print(c.display())
    del c
