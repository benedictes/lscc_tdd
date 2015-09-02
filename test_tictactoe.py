import unittest
import tictactoe as ttt


class GridTest(unittest.TestCase):

    def test_emptyGrid_returnsNoWinner(self):
        grid = ttt.Grid()
        self.assertEqual(grid.getWinner(), 0)

    def test_emptyGrid_topLeft_returnsEmpty(self):
        grid = ttt.Grid()
        self.assertEqual(grid.getAt(0, 0), 0)

    def test_setAt_topLeft1_setsValue(self):
        grid = ttt.Grid()
        grid.setAt(0, 0, 1)
        self.assertEqual(grid.getAt(0, 0), 1)

    def test_setAt_twoValues_setsValues(self):
        grid = ttt.Grid()
        grid.setAt(0, 2, 1)
        grid.setAt(1, 1, 2)
        self.assertEqual(grid.getAt(0, 2), 1)

    def test_grid_3onDiagonal_returnsWinner(self):
        grid = ttt.Grid()
        grid.setAt(0, 0, 1)
        grid.setAt(1, 1, 1)
        grid.setAt(2, 2, 1)

        self.assertEqual(grid.getWinner(), 1)

    def test_grid_3onLastRow_returnsWinner(self):
        grid = ttt.Grid()
        grid.setAt(2, 0, 1)
        grid.setAt(2, 1, 1)
        grid.setAt(2, 2, 1)

        self.assertEqual(grid.getWinner(), 1)
