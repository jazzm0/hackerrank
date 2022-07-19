import unittest


# https://www.hackerrank.com/challenges/connected-cell-in-a-grid

def fill_region(matrix, i, j, region_id):
    region_count = 0
    ind_i = i
    while ind_i < len(matrix):
        ind_j = 0
        while ind_j < len(matrix[0]):
            if matrix[ind_i][ind_j] == 1 and ((ind_i == i and ind_j == j)
              or (ind_j > 0 and matrix[ind_i][ind_j - 1] == region_id)  # left
              or (ind_i > 0 and ind_j > 0 and matrix[ind_i - 1][ind_j - 1] == region_id)  # up-left
              or (ind_i > 0 and matrix[ind_i - 1][ind_j] == region_id)  # up
              or (ind_i > 0 and ind_j + 1 < len(matrix[0]) and matrix[ind_i - 1][ind_j + 1] == region_id)  # up-right
              or (ind_j + 1 < len(matrix[0]) and (matrix[ind_i][ind_j + 1] == region_id))  # right
              or (ind_i + 1 < len(matrix) and ind_j + 1 < len(matrix[0]) and matrix[ind_i + 1][ind_j + 1] == region_id)  # down-right
              or (ind_i + 1 < len(matrix) and matrix[ind_i + 1][ind_j] == region_id)  # down
              or (ind_i + 1 < len(matrix) and ind_j > 0 and matrix[ind_i + 1][ind_j - 1] == region_id)  # down-left
            ):

                matrix[ind_i][ind_j] = region_id
                ind_j = 0
                ind_i = i
                region_count += 1
            else:
                ind_j += 1
        ind_i += 1
    return region_count


def connectedCell(matrix):
    region_id = 2
    max_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                current_count = fill_region(matrix, i, j, region_id)
                max_count = max(current_count, max_count)
                region_id += 1
    return max_count


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(connectedCell([[1, 1, 0],
                                        [1, 0, 0],
                                        [0, 0, 1]
                                        ]), 3)

    def test_b(self):
        self.assertEqual(connectedCell([[1, 1, 0, 0],
                                        [0, 1, 1, 0],
                                        [0, 0, 1, 0],
                                        [1, 0, 0, 0]]), 5)

    def test_c(self):
        self.assertEqual(connectedCell([[0, 0, 1, 1],
                                        [0, 0, 1, 0],
                                        [0, 1, 1, 0],
                                        [0, 1, 0, 0],
                                        [1, 1, 0, 0]]), 8)

    def test_d(self):
        self.assertEqual(connectedCell([[1, 1, 0, 0, 0],
                                        [0, 1, 1, 0, 0],
                                        [0, 0, 1, 0, 1],
                                        [1, 0, 0, 0, 1],
                                        [0, 1, 0, 1, 1]]), 5)

    def test_e(self):
        self.assertEqual(connectedCell([[0, 1, 1, 1, 1],
                                        [1, 0, 0, 0, 1],
                                        [1, 1, 0, 1, 0],
                                        [0, 1, 0, 1, 1],
                                        [0, 1, 1, 1, 0]]), 15)

    def test_f(self):
        self.assertEqual(connectedCell([[1, 1, 1, 0, 1],
                                        [0, 0, 1, 0, 0],
                                        [1, 1, 0, 1, 0],
                                        [0, 1, 1, 0, 0],
                                        [0, 0, 0, 0, 0],
                                        [0, 1, 0, 0, 0],
                                        [0, 0, 1, 1, 0]]), 9)

    def test_g(self):
        self.assertEqual(connectedCell([[0, 1, 0, 0, 0, 0, 1, 1, 0],
                                        [1, 1, 0, 0, 1, 0, 0, 0, 1],
                                        [0, 0, 0, 0, 1, 0, 1, 0, 0],
                                        [0, 1, 1, 1, 0, 1, 0, 1, 1],
                                        [0, 1, 1, 1, 0, 0, 1, 1, 0],
                                        [0, 1, 0, 1, 1, 0, 1, 1, 0],
                                        [0, 1, 0, 0, 1, 1, 0, 1, 1],
                                        [1, 0, 1, 1, 1, 1, 0, 0, 0],
                                        ]), 29)


if __name__ == '__main__':
    unittest.main()
