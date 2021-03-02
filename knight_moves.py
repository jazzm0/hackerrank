import unittest


class Cell:
    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist


def is_inside(x, y):
    if 0 <= x <= 7 and 0 <= y <= 7:
        return True
    return False


def solution(knightpos, targetpos):
    d = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    knightpos = (knightpos // 8, knightpos % 8)
    targetpos = (targetpos // 8, targetpos % 8)

    queue = [Cell(knightpos[0], knightpos[1], 0)]

    visited = [[False for _ in range(8)]
               for _ in range(8)]

    visited[knightpos[0]][knightpos[1]] = True

    while len(queue) > 0:

        t = queue[0]
        queue.pop(0)

        if (t.x == targetpos[0] and
                t.y == targetpos[1]):
            return t.dist

        for i in range(8):

            x = t.x + d[i][0]
            y = t.y + d[i][1]

            if is_inside(x, y) and not visited[x][y]:
                visited[x][y] = True
                queue.append(Cell(x, y, t.dist + 1))


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(solution(0, 1), 3)

    def test_b(self):
        self.assertEqual(solution(19, 36), 1)


if __name__ == '__main__':
    unittest.main()
