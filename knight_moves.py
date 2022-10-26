import unittest


# https://www.hackerrank.com/challenges/knightl-on-chessboard

def knight(a, b, location, n):
    next_locations = set()
    if location[0] + a < n and location[1] + b < n:
        next_locations.add((location[0] + a, location[1] + b))
        next_locations.add((location[1] + b, location[0] + a))

    if location[0] + a < n and location[1] - b >= 0:
        next_locations.add((location[0] + a, location[1] - b))
        next_locations.add((location[1] - b, location[0] + a))

    if location[0] - a >= 0 and location[1] + b < n:
        next_locations.add((location[0] - a, location[1] + b))
        next_locations.add((location[1] + b, location[0] - a))

    if location[0] - a >= 0 and location[1] - b >= 0:
        next_locations.add((location[0] - a, location[1] - b))
        next_locations.add((location[1] - b, location[0] - a))

    return next_locations


def knightlOnAChessboard(n):
    start = (0, 0)
    end = (n - 1, n - 1)
    overall_result = []

    for a in range(1, n):
        result = []

        for b in range(1, n):

            visited_locations = {start}
            new_locations = knight(a, b, start, n)
            length = 1

            while len(new_locations) != 0:
                all_new_locations = set()

                for location in new_locations:

                    visited_locations.add(location)
                    temp_new_locations = knight(a, b, location, n)

                    for temp in temp_new_locations:
                        if temp not in visited_locations:
                            all_new_locations.add(temp)

                if end in visited_locations:
                    result.append(length)
                    break

                if len(all_new_locations) == 0:
                    result.append(-1)
                    break

                length += 1
                new_locations = all_new_locations

        overall_result.append(result)
    return overall_result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(knightlOnAChessboard(5), [[4, 4, 2, 8],
                                                   [4, 2, 4, 4],
                                                   [2, 4, -1, -1],
                                                   [8, 4, -1, 1]])

    def test_b(self):
        self.assertEqual(knight(1, 2, (2, 2), 5), {(0, 1), (3, 4), (4, 3), (0, 3), (1, 4), (3, 0), (1, 0), (4, 1)})


if __name__ == '__main__':
    unittest.main()
