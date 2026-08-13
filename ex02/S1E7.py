from S1E9 import Character


class Baratheon(Character):
    "Representing Baratheon"
    def __init__(self, first_name, is_alive=True):
        """Constructor for Baratheon"""
        print("Start init Baratheon.__init__()")
        super().__init__(first_name, is_alive=is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hair = "dark"
        print("End init Baratheon.__init__()")

    def __repr__(self):
        """String representation of Baratheon"""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hair})"

    def __str__(self):
        """Actual representation of Baratheon"""
        return self.__repr__()

    def die(self):
        """Overrides abstract method from the base class
        and updates is_alive to False"""
        self.is_alive = False


class Lannister(Character):
    """Representing Lannister"""
    def __init__(self, first_name, is_alive=True):
        """Constructor for Lannister"""
        print('Start init Lannister.__init__()')
        super().__init__(first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.eyes = "green"
        self.hair = "light"
        print('End init Lannister.__init__()')

    def __repr__(self):
        """String representation of Lannister"""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hair})"

    def __str__(self):
        """Actual representation of Lannister"""
        return self.__repr__()

    def die(self):
        """Overrides abstract method from the base class
        and updates is_alive to False"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Custom constructor for Lannister"""
        return cls(first_name, is_alive)
