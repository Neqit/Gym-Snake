import unittest
from grid import Grid
import numpy as np

class GridTests(unittest.TestCase):

    grid_size = [30,30]
    unit_size = 10

    def grid_Initialization_Test(self):
        grid = Grid(self.grid_size, self.unit_size)
        expected_grid = np.array((self.grid_size[1]*self.unit_size,self.grid_size[0]*self.unit_size, 3), dtype=np.uint8)
        expected_size = [300,300,3]
        self.assertTrue(np.array_equal(grid.grid, expected_grid))
        self.assertTrue(np.array_equal(grid.grid.shape, expected_size))

    def unit_size_Initialization_Test(self):
        grid = Grid(self.grid_size, self.unit_size)
        self.assertTrue(grid.unit_size == self.unit_size)

    def color_Initialization_Test(self):
        grid = Grid(self.grid_size, self.unit_size)
        expected_color = np.array([0,255,0], dtype=np.uint8)
        for i in range(grid.grid.shape[0]):
            for j in range(grid.grid.shape[1]):
                self.assertTrue(np.array_equal(grid.grid[i,j,:],expected_color))

    def color_of_Color_Test(self):
        grid = Grid(self.grid_size, self.unit_size)
        expected_color = np.array([0,255,0], dtype=np.uint8)
        self.assertTrue(np.array_equal(grid.color_of([0,0]),expected_color))

    def color_of_Coordinate_Test(self):
        grid = Grid(self.grid_size, self.unit_size)
        coord = [3,2]
        expected_color = np.array([0,0,0], dtype=np.uint8)
        grid.grid[coord[1]*self.unit_size,coord[0]*self.unit_size,:] = expected_color
        self.assertTrue(np.array_equal(grid.color_of(coord),expected_color))

    def draw_Positive_Test(self):
        grid = Grid(self.grid_size, self.unit_size)
        expected_color = np.array([0,0,0], dtype=np.uint8)
        coord = [3,2]
        grid.draw(coord, expected_color)
        for i in range(grid.grid.shape[0]):
            for j in range(grid.grid.shape[1]):
                if i >= coord[1] and i < coord[1]+grid.unit_size and j >= coord[0] and j < coord[0]+grid.unit_size:
                    self.assertTrue(np.array_equal(grid.grid[i,j,:],expected_color))
                else:
                    self.assertFalse(np.array_equal(grid.grid[i,j,:],expected_color2))

    def draw__Negative_Test(self):
        grid = Grid(self.grid_size, self.unit_size)
        expected_color = grid.SPACE_COLOR
        coord = [3,2]
        grid.draw(coord, expected_color)
        for i in range(grid.grid.shape[0]):
            for j in range(grid.grid.shape[1]):
                if i >= coord[1] and i < coord[1]+grid.unit_size and j >= coord[0] and j < coord[0]+grid.unit_size:
                    self.assertFalse(np.array_equal(grid.grid[i,j,:],expected_color))
                else:
                    self.assertTrue(np.array_equal(grid.grid[i,j,:],expected_color2))

    def draw_snake_Positive_Test(self):
        grid = Grid(self.grid_size, self.unit_size)
        snake_size = 3
        head_coord = [10,10]
        snake = Snake(head_coord, snake_size)
        grid.draw_snake(snake, grid.HEAD_COLOR)

        expected_colors = np.array([grid.HEAD_COLOR] + [grid.BODY_COLOR]*2, dtype=np.uint8)
        expected_coords = np.array([[10,10], [10,9], [10,8]])
        for coord,color in zip(expected_coords, expected_colors):
            self.assertTrue(np.array_equal(grid.color_of(coord), color))

    def draw_snake_Negative_Test(self):
        grid = Grid(self.grid_size, self.unit_size)
        snake_size = 3
        head_coord = [10,10]
        snake = Snake(head_coord, snake_size)
        grid.draw_snake(snake, grid.HEAD_COLOR)

        expected_color = grid.SPACE_COLOR
        expected_coords = [(10,10), (10,9), (10,8)]
        for i,j in range(grid.grid_size[0],grid.grid_size[1]):
            if (i,j) == expected_coords[0] or (i,j) == expected_coords[1] or (i,j) == expected_coords[2]:
                self.assertFalse(np.array_equal(grid.color_of(coord), expected_color))
            else:
                self.assertTrue(np.array_equal(grid.color_of(coord), expected_color))


if __name__ == "__main__":
    unittest.main()