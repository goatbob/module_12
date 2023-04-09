from abc import ABC, abstractmethod

class Rider(ABC):

    @abstractmethod
    def ride(self):
        pass

    @abstractmethod
    def riders(self):
        pass
    