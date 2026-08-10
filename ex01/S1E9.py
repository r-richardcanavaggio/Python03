from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character"""
    def __init__(self, first_name, is_alive=True,
                 family_name="", eyes="", hairs=""):
        """Constructor for Character"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    @abstractmethod
    def die(self):
        """Method to change health state of the charater.
        Should be implemented by subclasses"""
        pass
