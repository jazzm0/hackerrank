import unittest


# https://www.hackerrank.com/challenges/ncr-table/


def solve(n):
    modulus = 10 ** 9
    modulo_result = [0] * (n + 1)
    result, modulo_result[0] = 1, 1
    for r in range(1, n + 1):
        result = ((result * (n - r + 1)) // r)
        modulo_result[r] = result % modulus
    return modulo_result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(solve(2), [1, 2, 1])

    def test_b(self):
        self.assertEqual(solve(4), [1, 4, 6, 4, 1])

    def test_c(self):
        self.assertEqual(solve(229),
                         [1, 229, 26106, 1975354, 111607501, 22337545, 500601680, 233453520, 228335180, 829119420,
                          240627240, 154305960, 303224940, 523062460, 784392240, 242955440, 249529010, 479392890,
                          979516260, 614627940, 953593370, 728619730, 252404720, 271642480, 248264620, 235769884,
                          3732936, 583621704, 424699436, 736709884, 244732560, 119412240, 176363235, 598289615,
                          743081310, 568595870, 452988855, 146671595, 372656480, 722497120, 931861320, 783458280,
                          935479920, 393831280, 755741320, 329158760, 316635040, 339238560, 661279540, 769216260,
                          569178536, 36920744, 395613316, 57048244, 704453536, 332352160, 282665640, 489493960,
                          899878640, 421682160, 694766120, 170745480, 236858720, 516752480, 152826745, 618714045,
                          810137930, 418693770, 938652805, 856856545, 672814960, 267289840, 392108260, 213164340,
                          935859960, 734110584, 66487236, 534708404, 913790736, 797245584, 494835470, 305314630,
                          965689820, 601884380, 641370470, 741161390, 473572560, 640469840, 419849060, 912345140,
                          308092440, 492580760, 738871140, 927154260, 511627440, 727049520, 577339955, 533878495,
                          617060830, 250858270, 426115751, 415533979, 90081856, 470295104, 589011376, 82156400,
                          567805600, 503178400, 438775600, 817356400, 164388800, 734795200, 95587800, 523750200,
                          532938800, 532938800, 523750200, 95587800, 734795200, 164388800, 817356400, 438775600,
                          503178400, 567805600, 82156400, 589011376, 470295104, 90081856, 415533979, 426115751,
                          250858270, 617060830, 533878495, 577339955, 727049520, 511627440, 927154260, 738871140,
                          492580760, 308092440, 912345140, 419849060, 640469840, 473572560, 741161390, 641370470,
                          601884380, 965689820, 305314630, 494835470, 797245584, 913790736, 534708404, 66487236,
                          734110584, 935859960, 213164340, 392108260, 267289840, 672814960, 856856545, 938652805,
                          418693770, 810137930, 618714045, 152826745, 516752480, 236858720, 170745480, 694766120,
                          421682160, 899878640, 489493960, 282665640, 332352160, 704453536, 57048244, 395613316,
                          36920744, 569178536, 769216260, 661279540, 339238560, 316635040, 329158760, 755741320,
                          393831280, 935479920, 783458280, 931861320, 722497120, 372656480, 146671595, 452988855,
                          568595870, 743081310, 598289615, 176363235, 119412240, 244732560, 736709884, 424699436,
                          583621704, 3732936, 235769884, 248264620, 271642480, 252404720, 728619730, 953593370,
                          614627940, 979516260, 479392890, 249529010, 242955440, 784392240, 523062460, 303224940,
                          154305960, 240627240, 829119420, 228335180, 233453520, 500601680, 22337545, 111607501,
                          1975354, 26106, 229, 1])


if __name__ == '__main__':
    unittest.main()