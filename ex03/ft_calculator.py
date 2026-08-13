class calculator:
    """Class that defines basic arithmetic functions"""
    def __init__(self, vector):
        """Constructor for calculator"""
        self.vector = vector

    def __repr__(self):
        """String representation of calculator"""
        return self.vector.__str__()

    def __str__(self):
        """Actual representation"""
        return self.__repr__()

    def __add__(self, object) -> None:
        """Add operator"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiplication operator"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Substraction operator"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divison operator, checks for 0"""
        if object != 0:
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        else:
            print('Division by zero')
