from abc import abstractmethod


class ChessPiece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def change_color(self):
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"

    def change_position(self, *args):
        if len(args) == 2:
            x, y = args
        else:
            x, y = args[0]

        if self._is_valid_position(x, y):
            self.position = (x, y)
        else:
            print("Invalid position")

    def _is_valid_position(self, x, y):
        return 0 <= x <= 7 and 0 <= y <= 7

    def __str__(self):
        return f"{self.color} figure is at position {self.position}"

    @abstractmethod
    def is_valid_move(self, x, y):
        pass
