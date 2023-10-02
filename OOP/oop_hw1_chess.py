from abc import abstractmethod, ABC


class ChessPiece(ABC):
    def __init__(self, color: str, position: tuple):
        self.color = color
        self.position = position

    def change_color(self):
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"

    def change_position(self, new_position):
        if self._is_valid_position(new_position):
            self.position = new_position
        else:
            raise ValueError('Invalid position')

    def _is_valid_position(self, position):
        x, y = position
        return 0 <= x <= 7 and 0 <= y <= 7

    @abstractmethod
    def can_move_to(self, position):
        pass

    def __str__(self):
        return f"{self.color} figure is at position {self.position}"


class Pawn(ChessPiece):
    def can_move_to(self, position):
        diff_x = position[0] - self.position[0]
        diff_y = position[1] - self.position[1]

        if self.color == "white":
            return diff_x == 1 and diff_y == 0
        else:
            return diff_x == -1 and diff_y == 0


class Knight(ChessPiece):
    def can_move_to(self, position):
        diff_x = abs(position[0] - self.position[0])
        diff_y = abs(position[1] - self.position[1])

        return (diff_x, diff_y) in [(2, 1), (1, 2)]


class Bishop(ChessPiece):
    def can_move_to(self, position):
        diff_x = abs(position[0] - self.position[0])
        diff_y = abs(position[1] - self.position[1])
        return diff_x == diff_y


class Rook(ChessPiece):
    def can_move_to(self, position):
        diff_x = abs(position[0] - self.position[0])
        diff_y = abs(position[1] - self.position[1])
        return diff_x == 0 or diff_y == 0


class Queen(ChessPiece):
    def can_move_to(self, position):
        diff_x = abs(position[0] - self.position[0])
        diff_y = abs(position[1] - self.position[1])
        return diff_x == diff_y or diff_x == 0 or diff_y == 0


class King(ChessPiece):
    def can_move_to(self, position):
        diff_x = abs(position[0] - self.position[0])
        diff_y = abs(position[1] - self.position[1])
        return diff_x <= 1 and diff_y <= 1




pawn = Pawn('white', (1, 3))
print(pawn.position)

pawn.change_position((2, 3))
print(pawn.position)


knight = Knight('black', (3, 3))
print(knight.can_move_to((5, 4)))

bishop = Bishop('white', (2, 2))
print(bishop.can_move_to((4, 4)))
print(bishop.can_move_to((2, 4)))
