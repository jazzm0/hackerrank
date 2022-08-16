import unittest


# https://www.hackerrank.com/challenges/grid-challenge/

def gridChallenge(grid):
    n = len(grid)
    for i in range(n):
        grid[i] = sorted(grid[i])

    for i in range(n - 1):
        for j in range(len(grid[i])):
            if grid[i][j] > grid[i + 1][j]:
                return 'NO'
    return 'YES'


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']), 'YES')

    def test_b(self):
        self.assertEqual(gridChallenge(['uxf', 'vof', 'hmp']), 'NO')

    def test_c(self):
        self.assertEqual(gridChallenge(['ppp', 'ypp', 'wyw']), 'YES')

    def test_d(self):
        self.assertEqual(gridChallenge([
            'vzzrxgrnvpyjotknhbkiiifbiuwcpvmfapjxntw',
            'pisviqkjniiwmyshjknxlpksbsdrhspmyvvduzs',
            'aobisvvwgybnimvybokglhspetkanqleddgedot',
            'rezemaxkxecxwimxaeczghyrnyjvolfxtsaafvw',
            'ndwpbvwjiqyrmxpvguzngmbbwjvetbzjnztgoonv',
            'kjpzezwjlpmcduyuestpojisaqtuzogmkkpqwuvv',
            'coboywgjbwdxzgcrydxvufuqmytavfvnangydcd',
            'vlupqopswxwcdniowxnqxclnafbytnokpsxlvdvv',
            'osrxkmpxetcgvujgrssfdhnomxogwfjsyvabifv',
            'dusxcvzragkjrskllgrwnfmikyiwfslyzrvtqfa',
            'spxwiblilwbussklwfutvicmzkafkwjcfzqjkzh',
            'fkohggspbbfvudtqgjpjuvywzxsdwwmmknigfuk',
            'hkplzjrshzabtkjowvqxxiilujkkgbfmxexbebx',
            'wzkccnyjhaubiiilpktcwkpnxoxxiufypqeqqky',
            'sntrbgbdyitfnamzevypgaowqizgaedcdboqxaw',
            'xslgigeifaqqzvqjcnoqxqdovpfbszvmfrjhmqt',
            'kakeviomxlknqmocskoteeyrskvkkshezjllmyv',
            'pekogeckvoxrzmufdijhbdztktsavvzyrlaxpvn',
            'pfdeemegondceocgdeexavdbaruhtivxdxgvasx',
            'hdllduyljbjgjifowdecegdmwuuynznggoimtoh',
            'rjpbtxshbohnvrpuyogrriwapvjgupiumsinxry',
            'kzypvfegsllncdoldpbhyhxwnxkqokppnkltdgq',
            'cldnrmfywtadiuktaqyqudihncxlzeabveoetek',
            'ztzmrjqpgbrjildvjccaftrmdcgysegdtoojjwk',
            'bofksxvfhtcfhrgfsshpiwqrlqggbfqklllziky',
            'seyuhbroajuqjxqkyhqvlleqdwmfgsgebaxsvpq',
            'hltpxpuaxsibtkpoqialowvkdlkbyhakbefzgzn',
            'fvkyzegsdfawenripawinuvdlhvwwrleqwtygcs',
            'dugyunxtuzbgdnjpanaugtdvoemczinalxvtygl',
            'dyizgkfpbhhabdfrkepzruaiwgpgxtdfnendnhl',
            'feckqnckvsulwuvfoopnnyyhqdxmwxjrawkwxsv',
            'xqmnthpkodufmwzpoczvenzxehrdqqpzgnnqkdd',
            'qhmtpvgwnqeztvffmnrihwfqdsdkljvanccmsyg',
            'dwupgfksdevslhkdrcmytdpafyijgjbfssyouza',
            'endhjybrgxkbpglsfrvsqvbikfwcxnjtvyntofj',
            'ipyowznudnfjiqmpsivlwmauyexkrnsxntddcrs',
            'ygvaslfhmlxcggqsemzcuwhnrljejhwkshmuxmw',
            'ephqftahxlrjoclovgirvwdfclqtpubzpsllcsc',
            'nwdjeczlgdjeziimhkatazntvjcywwpefbjzjyw']), 'NO')


if __name__ == '__main__':
    unittest.main()
