from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character"""
    def __init__(self, first_name, is_alive=True):
        """Constructor for Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Method to change health state of the charater.
        Should be implemented by subclasses"""
        pass


class Stark(Character):
    """Class representing a Stark character"""
    def die(self):
        """Overrides abstract method from the base class
        and updates is_alive to False"""
        self.is_alive = False
