import unittest
import string


# https://www.hackerrank.com/challenges/weighted-uniform-string

def weightedUniformStrings(s, queries):
    values = {}
    weights = set()
    answers = list()

    for i in range(len(string.ascii_lowercase)):
        values[string.ascii_lowercase[i]] = i + 1

    actual_element = s[0]
    actual_value = values[s[0]]
    weights.add(actual_value)

    for i in range(1, len(s)):
        if s[i] == actual_element:
            actual_value += values[s[i]]
        else:
            actual_element = s[i]
            actual_value = values[s[i]]

        weights.add(actual_value)

    for q in queries:
        if q in weights:
            answers.append('Yes')
        else:
            answers.append('No')

    return answers


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(weightedUniformStrings("abbcccdddd", [1, 7, 5, 4, 15]), ['Yes', 'No', 'No', 'Yes', 'No'])


if __name__ == '__main__':
    unittest.main()
