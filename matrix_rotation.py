import unittest


def rotate(line, r):
    if r > len(line) - 1:
        r = (r % (len(line) - 1)) - 1

    res = []
    res[0:r] = line[len(line) - r:]
    res[r:] = line[0:len(line) - r]
    return res


def matrixRotation(matrix, r):
    start_x = 0
    start_y = 0

    len_x = len(matrix)
    len_y = len(matrix[0])
    lines = list()

    for offset in range(0, min(len_x, len_y) // 2):

        line = list()

        for i in range(start_x + offset, len_x - offset):
            line.append(matrix[i][0 + offset])

        for j in range(start_y + 1 + offset, len_y - offset):
            line.append(matrix[len_x - 1 - offset][j])

        for i in range(len_x - 2 - offset, start_x - 1 + offset, -1):
            line.append(matrix[i][len_y - 1 - offset])

        for j in range(len_y - 2 - offset, start_y + offset, -1):
            line.append(matrix[0 + offset][j])

        lines.append(line)

    for i in range(0, len(lines)):
        m = r % len(lines[i])
        lines[i] = rotate(lines[i], m)

    for offset in range(0, min(len_x, len_y) // 2):

        ind = 0

        for i in range(start_x + offset, len_x - offset):
            matrix[i][0 + offset] = lines[0 + offset][ind]
            ind += 1

        for j in range(start_y + 1 + offset, len_y - offset):
            matrix[len_x - 1 - offset][j] = lines[0 + offset][ind]
            ind += 1

        for i in range(len_x - 2 - offset, start_x - 1 + offset, -1):
            matrix[i][len_y - 1 - offset] = lines[0 + offset][ind]
            ind += 1

        for j in range(len_y - 2 - offset, start_y + offset, -1):
            matrix[0 + offset][j] = lines[0 + offset][ind]
            ind += 1

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()

    return matrix


class TestStringMethods(unittest.TestCase):

    def test_rotate_a(self):
        self.assertEqual(rotate(
            [1, 2, 3, 4], 2),
            [3, 4, 1, 2, ])

    def test_rotate_b(self):
        self.assertEqual(rotate(
            [1, 2, 3, 4], 3),
            [2, 3, 4, 1])

    def test_rotate_c(self):
        self.assertEqual(rotate(
            [1, 2, 3, 4], 4),
            [1, 2, 3, 4])

    def test_rotate_d(self):
        self.assertEqual(rotate(
            [1, 2, 3, 4], 5),
            [4, 1, 2, 3, ])

    def test_a(self):
        self.assertEqual(matrixRotation([
            [1, 2, 3, 4],
            [12, 1, 2, 5],
            [11, 4, 3, 6],
            [10, 9, 8, 7]
        ], 2), [
            [3, 4, 5, 6],
            [2, 3, 4, 7],
            [1, 2, 1, 8],
            [12, 11, 10, 9]
        ])

    def test_b(self):
        self.assertEqual(matrixRotation([
            [1, 22, 21, 20, 19, 18, 17],
            [2, 23, 36, 35, 34, 33, 16],
            [3, 24, 37, 42, 41, 32, 15],
            [4, 25, 38, 39, 40, 31, 14],
            [5, 26, 27, 28, 29, 30, 13],
            [6, 7, 8, 9, 10, 11, 12]
        ], 1), [
            [22, 21, 20, 19, 18, 17, 16],
            [1, 36, 35, 34, 33, 32, 15],
            [2, 23, 42, 41, 40, 31, 14],
            [3, 24, 37, 38, 39, 30, 13],
            [4, 25, 26, 27, 28, 29, 12],
            [5, 6, 7, 8, 9, 10, 11]
        ])

    def test_c(self):
        self.assertEqual(matrixRotation(
            [
                [9718805, 60013003, 5103628, 85388216, 21884498, 38021292, 73470430, 31785927],
                [69999937, 71783860, 10329789, 96382322, 71055337, 30247265, 96087879, 93754371],
                [79943507, 75398396, 38446081, 34699742, 1408833, 51189, 17741775, 53195748],
                [79354991, 26629304, 86523163, 67042516, 54688734, 54630910, 6967117, 90198864],
                [84146680, 27762534, 6331115, 5932542, 29446517, 15654690, 92837327, 91644840],
                [58623600, 69622764, 2218936, 58592832, 49558405, 17112485, 38615864, 32720798],
                [49469904, 5270000, 32589026, 56425665, 23544383, 90502426, 63729346, 35319547],
                [20888810, 97945481, 85669747, 88915819, 96642353, 42430633, 47265349, 89653362],
                [55349226, 10844931, 25289229, 90786953, 22590518, 54702481, 71197978, 50410021],
                [9392211, 31297360, 27353496, 56239301, 7071172, 61983443, 86544343, 43779176]
            ], 40),
            [
                [93754371, 53195748, 90198864, 91644840, 32720798, 35319547, 89653362, 50410021],
                [31785927, 25289229, 10844931, 97945481, 5270000, 69622764, 27762534, 43779176],
                [73470430, 90786953, 42430633, 96642353, 88915819, 85669747, 26629304, 86544343],
                [38021292, 22590518, 90502426, 67042516, 54688734, 32589026, 75398396, 61983443],
                [21884498, 54702481, 17112485, 5932542, 29446517, 2218936, 71783860, 7071172],
                [85388216, 71197978, 15654690, 58592832, 49558405, 6331115, 10329789, 56239301],
                [5103628, 47265349, 54630910, 56425665, 23544383, 86523163, 96382322, 27353496],
                [60013003, 63729346, 51189, 1408833, 34699742, 38446081, 71055337, 31297360],
                [9718805, 38615864, 92837327, 6967117, 17741775, 96087879, 30247265, 9392211],
                [69999937, 79943507, 79354991, 84146680, 58623600, 49469904, 20888810, 55349226]
            ])

        if __name__ == '__main__':
            unittest.main()
