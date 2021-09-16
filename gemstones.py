import unittest
from collections import Counter


# https://www.hackerrank.com/challenges/gem-stones


def gemstones(arr):
    counter_list = []
    common_keys = set()
    minimum_count = {}

    for i in range(len(arr)):
        character_count = Counter(arr[i])
        counter_list.append(character_count)
        if len(common_keys) == 0:
            common_keys = character_count.keys()
        else:
            common_keys = common_keys & character_count.keys()
            if len(common_keys) == 0:
                return 0

    for i in range(len(counter_list)):
        for k, v in counter_list[i].items():
            if k in common_keys:
                if k in minimum_count:
                    if minimum_count[k] > v:
                        minimum_count[k] = v
                else:
                    minimum_count[k] = v

    s = 0
    for v in minimum_count.values():
        s += v
    return s


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(gemstones(['abc', 'abc', 'bc']), 2)

    def test_b(self):
        self.assertEqual(gemstones(['abcdde', 'baccd', 'eeabg']), 2)

    def test_c(self):
        self.assertEqual(gemstones(['basdfj', 'asdlkjfdjsa', 'bnafvfnsd', 'oafhdlasd']), 4)

    def test_d(self):
        self.assertEqual(
            gemstones(['molbapydxfbsbwqrrsmkebhxnphikeywkxoldawbojksdlfoqwrqjmkcylacxfdyclepprhbndmgocrdzcgr',
                       'nlxchmhckrzrykxjxjpckaavztepfbizoqh',
                       'kncchsgsraxnotgdgovptowzghodwqideluywpwmqbqbtanqs',
                       'nieqzi',
                       'worxpvczg',
                       'nsxuyycyhfecp',
                       'scegvdydyapvchvtqpbqexsszpvtaooklvzoyjackwsbualovxzpqszjwnaosvggwqdbeimckcphayglqqpiwldihhtwwrcxc'
                       ]), 0)


if __name__ == '__main__':
    unittest.main()
