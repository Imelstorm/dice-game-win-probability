
class WrongKForDiceError(ValueError):

    def __init__(self, min_value: int, max_value: int):
        self.__min_value = min_value
        self.__max_value = max_value

    def __repr__(self):
        return f"k should be between {self.__min_value} and {self.__max_value}"
