import unittest


def reduce(letter, positive):
    positive[letter] = positive.get(letter) - 1

    if positive[letter] == 0:
        positive.pop(letter)


def steadyGene(gene):
    char_count = {}
    good_value = len(gene) // 4

    for i in range(len(gene)):
        char_count[gene[i]] = char_count.get(gene[i], 0) + 1

    deviations = {}

    for k, v in char_count.items():
        if v > good_value:
            deviations[k] = abs(v - good_value)

    if len(deviations) == 0:
        return 0

    min_length = len(gene)

    i = 0

    while i < len(gene):
        if gene[i] in deviations:
            c_deviations = deviations.copy()
            reduce(gene[i], c_deviations)
            current_length = 1
            for j in range(i + 1, len(gene)):
                if len(c_deviations) == 0:
                    break

                current_length = current_length + 1

                if gene[j] in c_deviations:
                    reduce(gene[j], c_deviations)

            if len(c_deviations) == 0:
                min_length = min(current_length, min_length)
                i += min_length
        i += 1
    return min_length


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(steadyGene('AAGTGCCT'), 0)

    def test_b(self):
        self.assertEqual(steadyGene('AAGTAGCT'), 1)

    def test_c(self):
        self.assertEqual(steadyGene('GAAATAAA'), 5)

    def test_d(self):
        self.assertEqual(steadyGene('TTGTATAGAAGATAGG'), 5)


if __name__ == '__main__':
    unittest.main()
