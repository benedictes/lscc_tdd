import numpy as np


class Grid(object):

    def __init__(self):
        self.dim = 3
        self.cells = np.zeros([self.dim, self.dim])

    def getWinner(self):
        return self.cells[1, 1]

    def getAt(self, row, column):
        return(self.cells[row, column])

    def setAt(self, row, column, value):
        self.cells[row, column] = value
