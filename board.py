import random

class Board:

    def __init__(self):
        """Initialize cells of game board"""
        # x -> 1     computer has won
        # 0 -> -1    user has won
        self.cells = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def has_winner(self):
        """
        Check if game has winner
        """
        for i in range(3):
            our_sum = 0
            for j in range(3):
                our_sum += self.cells[i][j]     #рух по горизонталі
            if our_sum == 3:
                return 1
            if our_sum == -3:
                return -1

        for j in range(3):
            our_sum = 0
            for i in range(3):
                our_sum += self.cells[i][j]     #рух по вертикалі
            if our_sum == 3:
                return 1
            if our_sum == -3:
                return -1

        our_sum = self.cells[0][0] + self.cells[1][1] + self.cells[2][2]   #рух по діагоналі
        if our_sum == 3:
            return 1
        if our_sum == -3:
            return -1

        our_sum = self.cells[0][2] + self.cells[1][1] + self.cells[2][0]   #рух по діагоналі
        if our_sum == 3:
            return 1
        if our_sum == -3:
            return -1

        return 0

    def make_random_move(self):
        """Make random move if we still have move"""
        if self.still_have_move():
            list_of_moves = []
            for i in range(3):
                for j in range(3):
                    if self.cells[i][j] == 0:
                        list_of_moves.append((i, j))

            return random.choice(list_of_moves)
        else:
            return "No moves left"
    
    def still_have_move(self):
        """
        Check if we still have move and return True if we do, otherwise return False
        """
        c = 0
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] == 0:
                    c += 1
                    
        return c != 0

    def set_value(self, tuple, item):
        """Set value by given coordinates"""
        if self.cells[tuple[0]][tuple[1]] != 0:
            return None
        else:
            self.cells[tuple[0]][tuple[1]] = item
            return self.cells

    def __str__(self):
        return "\n".join([" ".join([str(i) for i in lst]) for lst in self.cells])