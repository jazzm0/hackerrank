import unittest


def abbreviation(a, b):
    if a == b:
        return "YES"
    elif len(b) == 0 and a.islower():
        return "YES"
    elif len(a) < len(b):
        return "NO"
    elif len(b) == 0 and any(x.isupper() for x in a):
        return "NO"
    elif a.isupper() and a != b:
        return "NO"
    elif a[0] == b[0]:
        return abbreviation(a[1:], b[1:])
    elif a[0].islower():
        if abbreviation(a[0].capitalize() + a[1:], b) == "YES" or abbreviation(a[1:], b) == "YES":
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(abbreviation("AbcDE", "ABDE"), "YES")

    def test_b(self):
        self.assertEqual(abbreviation("daBcd", "ABC"), "YES")

    def test_c(self):
        self.assertEqual(abbreviation("AbcDE", "AFDE"), "NO")

    def test_d(self):
        self.assertEqual(abbreviation("beFgH", "EFG"), "NO")

    def test_e(self):
        self.assertEqual(abbreviation("AfPZN", "APZNC"), "NO")

    def test_f(self):
        self.assertEqual(abbreviation(
            "RDWPJPAMKGRIWAPBZSYWALDBLDOFLWIQPMPLEMCJXKAENTLVYMSJNRJAQQPWAGVcGOHEWQYZDJRAXZOYDMNZJVUSJGKKKSYNCSFWKVNHOGVYULALKEBUNZHERDDOFCYWBUCJGbvqlddfazmmohcewjg",
            "RDPJPAMKGRIWAPBZSYWALDBLOFWIQPMPLEMCJXKAENTLVYMJNRJAQQPWAGVGOHEWQYZDJRAXZOYDMNZJVUSJGKKKSYNCSFWKVNHOGVYULALKEBUNZHERDOFCYWBUCJG"),
            "NO")

    def test_g(self):
        self.assertEqual(abbreviation("MBQEVZPBjcbswirgrmkkfvfvcpiukuxlnxkkenqp", "MBQEVZP"), "NO")

    def test_h(self):
        self.assertEqual(abbreviation(
            "DINVMKSOfsVQByBnCWNKPRFRKMhFRSkNQRBVNTIKNBXRSXdADOSeNDcLWFCERZOLQjEZCEPKXPCYKCVKALNxBADQBFDQUpdqunpelxauyyrwtjpkwoxlrrqbjtxlkvkcajhpqhqeitafcsjxwtttzyhzvh",
            "DINVMKSOVQBBCWNKPRFRKMFRSNQRBVNTIKNBXRSXADOSNDLWFCERZOLQEZCEPKXPCYKCVKALNBADQBFDQU"), "YES")

    def test_i(self):
        self.assertEqual(abbreviation(
            "RMPRWOBYTSjXGVJQPDQEHTWXMOGcHVWKATSWLBWPJBQTYKVHKMFKCYVVJXGLUEZTLSXChGBCAOAMiFEAPPAGWeMXXQAQTFCZGXKOGZLLUWTZDOYVWHIJZEIDOSHPwFWHYXCIZKTjKKVKQNDXMTCCBQMAGVCDPZOXHPSEQYthuqclzletakrqbzmaohadpog",
            "RMPRWOBYTSXGVJQPDQEHTWXMOGHVWKATSWLBWPJBQTYKVHKMFKCYVVJXGLUEZTLSXCGBCAOAMFEAPPAGWMXXQAQTFCZGXKOGZLLUWTZDOYVWHIJZEIDOSHPFWHYXCIZKTKKVKQNDXMTCCBQMAGVCDPZOXHPSEQY"),
            "YES")

    def test_j(self):
        self.assertEqual(abbreviation(
            "BFZZVHdQYHQEMNEFFRFJTQmNWHFVXRXlGTFNBqWQmyOWYWSTDSTMJRYHjBNTEWADLgHVgGIRGKFQSeCXNFNaIFAXOiQORUDROaNoJPXWZXIAABZKSZYFTDDTRGZXVZZNWNRHMvSTGEQCYAJSFvbqivjuqvuzafvwwifnrlcxgbjmigkms",
            "BFZZVHQYHQEMNEFFRFJTQNWHFVXRXGTFNBWQOWYWSTDSTMJRYHBNTEWADLHVGIRGKFQSCXNFNIFAXOQORUDRONJPXWZXIAABZKSZYFTDDTRGZXVZZNWNRHMSTGEQCYAJSF"),
            "YES")

    def test_l(self):
        self.assertEqual(abbreviation("aaaaaa", "A"), "YES")


if __name__ == '__main__':
    unittest.main()
