from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character"""
    family_name = str
    eyes = str
    hair = str

    def __init__(self, first_name, is_alive=True):
        """Constructor for Character"""
        print('Start init Character.__init__()')
        self.first_name = first_name
        self.is_alive = is_alive
        print('End init Character.__init__()')

    @abstractmethod
    def die(self):
        """Method to change health state of the charater.
        Should be implemented by subclasses"""
        pass
