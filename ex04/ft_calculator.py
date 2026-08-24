class calculator:
    """Class for calculating dot product of two vectors,
    vector addition and substraction"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]):
        """Performs and prints
        dot product of two vectors"""
        result = 0
        for i in range(len(V1)):
            result = result + V1[i] * V2[i]
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]):
        """Performs and print addition of two vectors"""
        vector = [a + b for a, b in zip(V1, V2)]
        print(f"Add vector is : {vector}")

    @staticmethod
    def sub_vec(V1: list[float], V2: list[float]):
        """Performs and prints
        substraction of two vectors"""
        vector = [a - b for a, b in zip(V1, V2)]
        print(f"Sub vector is : {vector}")
