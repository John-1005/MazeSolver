import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )

        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_maze_9x13(self):
        num_cols = 9
        num_rows = 13
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2._cells),
            num_cols
        )

        self.assertEqual(
            len(m2._cells[0]),
            num_rows
        )



    def test_maze_13x9(self):
        num_cols = 13
        num_rows = 9
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m3._cells),
            num_cols
        )

        self.assertEqual(
            len(m3._cells[0]),
            num_rows
        )


    def test_large_maze(self):
        num_cols = 1000
        num_rows = 1000
        m4 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m4._cells),
            num_cols
        )

        self.assertEqual(
            len(m4._cells[0]),
            num_rows
        )




if __name__ == "__main__":
    unittest.main()
