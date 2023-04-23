"""
program: abstract_class.py
author: kyle godwin
last date modified: 11 april 2023

Abstract base class Rider with
ride and riders functions.
"""

from abc import ABC, abstractmethod


class Rider(ABC):

    @abstractmethod
    def ride(self):  # ride function
        pass

    @abstractmethod
    def riders(self):  # riders function
        pass

    