import unittest


def bigSorting(unsorted):
    unsorted.sort(key=int)
    return unsorted


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(bigSorting(
            [
                '1',
                '2',
                '100',
                '12303479849857341718340192371',
                '3084193741082937',
                '3084193741082938',
                '111',
                '200']
        ), [
            '1',
            '2',
            '100',
            '111',
            '200',
            '3084193741082937',
            '3084193741082938',
            '12303479849857341718340192371'
        ])


if __name__ == '__main__':
    unittest.main()
