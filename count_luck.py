import unittest

# https://www.hackerrank.com/challenges/count-luck


def countLuck(matrix, k):
    def valid_paths(i, j):
        return (
            ([], [[i - 1, j]])[valid_path(i - 1, j)]
            + ([], [[i + 1, j]])[valid_path(i + 1, j)]
            + ([], [[i, j - 1]])[valid_path(i, j - 1)]
            + ([], [[i, j + 1]])[valid_path(i, j + 1)]
        )

    m, n = len(matrix), len(matrix[0])
    valid_path = (
        lambda i, j: 0 <= i < m
        and 0 <= j < n
        and (matrix[i][j] == "." or matrix[i][j] == "*")
    )

    for i in range(m):
        matrix[i] = list(matrix[i])

    for i in range(m):
        try:
            j = matrix[i].index("M")
            break
        except:
            continue

    check_path = [([i, j], 0)]
    while check_path:
        (i, j), i_waves = check_path.pop()
        possible_paths = valid_paths(i, j)
        if matrix[i][j] == "*":
            return ("Oops!", "Impressed")[i_waves == k]
        matrix[i][j] = "X"
        if len(possible_paths) == 1:
            check_path += [(possible_paths[0], i_waves)]
        else:
            for coord in possible_paths:
                check_path += [(coord, i_waves + 1)]


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(
            countLuck([".X.X......X", ".X*.X.XXX.X", ".XX.X.XM...", "......XXXX."], 3),
            "Impressed",
        )

    def test_b(self):
        self.assertEqual(
            countLuck(["*.M", ".X."], 1),
            "Impressed",
        )

    def test_c(self):
        self.assertEqual(
            countLuck(["*..", "X.X", "..M"], 1),
            "Oops!",
        )


if __name__ == "__main__":
    unittest.main()
