# Refactored version of original lib.board
# Only the essentials.


class Board:
    def __init__(self, size:tuple(width, height)):
        self.w, self.h = size
        self.board = [["."] * self.w] * self.h
        
        # Remove if not used
        self.points = set()

    def plot(self, pos, icon):
        x, y = pos
        row = self.board[y].copy()
        row[x] = icon
        self.board[y] = row

        self.points.add(pos)

    def __str__(self):
        return "\n".join("".join(row) for row in self.board)

# exit()

if __name__ == "__main__":
    import unittest

    class TestBoard(unittest.TestCase):
        def setUp(self):
            self.board = Board((10, 10))

        def test_plot(self):
            self.board.plot((0, 1), "@")
            self.board.plot((5, 3), "@")
            print(self.board)

        def test_unplot(self):
            self.board.plot((5, 3), "@")
            self.board.plot((5, 4), "@")
            print(self.board)
    
    unittest.main()