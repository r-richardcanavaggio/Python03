from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing Kings"""
    def __init__(self, first_name, is_alive=True):
        """Constructor for King"""
        print('Start init King.__init__()')
        super().__init__(first_name, is_alive=is_alive)
        print('End init King.__init__()')

    def set_eyes(self, eye_color):
        """Set eye color of instanced King"""
        self.eyes = eye_color

    def set_hairs(self, hair_color):
        """Set hair color of instanced King"""
        self.hair = hair_color

    def get_eyes(self) -> str:
        """Returns eye color of instanced King"""
        return self.eyes

    def get_hairs(self) -> str:
        """Returns hair color of instanced King"""
        return self.hair
