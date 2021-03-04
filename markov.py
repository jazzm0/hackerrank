import unittest
from fractions import Fraction


def num_of_transients(m):
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] != 0:
                # this is not an all-zero row, try next one
                break
        else:
            return r


def decompose(m):
    t = num_of_transients(m)
    Q = []
    for r in range(t):
        qRow = []
        for c in range(t):
            qRow.append(m[r][c])
        Q.append(qRow)
    R = []
    for r in range(t):
        rRow = []
        for c in range(t, len(m[r])):
            rRow.append(m[r][c])
        R.append(rRow)
    return Q, R


def identity(t):
    m = []
    for i in range(t):
        r = []
        for j in range(t):
            r.append(int(i == j))
        m.append(r)
    return m


def isZero(m):
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] != 0:
                return False
    return True


def swap(m, i, j):
    n = []
    s = len(m)

    if i == j:
        # no need to swap
        return m

    for r in range(s):
        nRow = []
        tmpRow = m[r]
        if r == i:
            tmpRow = m[j]
        if r == j:
            tmpRow = m[i]
        for c in range(s):
            tmpEl = tmpRow[c]
            if c == i:
                tmpEl = tmpRow[j]
            if c == j:
                tmpEl = tmpRow[i]
            nRow.append(tmpEl)
        n.append(nRow)
    return n


def sort(m):
    size = len(m)

    zero_row = -1
    for r in range(size):
        sum = 0
        for c in range(size):
            sum += m[r][c]
        if sum == 0:
            # we have found all-zero row, remember it
            zero_row = r
        if sum != 0 and zero_row > -1:
            # we have found non-zero row after all-zero row - swap these rows
            n = swap(m, r, zero_row)
            # and repeat from the begining
            return sort(n)
    # nothing to sort, return
    return m


def normalize(m):
    n = []
    for r in range(len(m)):
        sum = 0
        cols = len(m[r])
        for c in range(cols):
            sum += m[r][c]

        nRow = []

        if sum == 0:
            nRow = m[r]
        else:
            for c in range(cols):
                nRow.append(Fraction(m[r][c], sum))
        n.append(nRow)
    return n


def subtract(i, q):
    if len(i) != len(i[0]) or len(q) != len(q[0]):
        raise Exception("non-square matrices")

    if len(i) != len(q) or len(i[0]) != len(q[0]):
        raise Exception("Cannot subtract matrices of different sizes")

    s = []
    for r in range(len(i)):
        sRow = []
        for c in range(len(i[r])):
            sRow.append(i[r][c] - q[r][c])
        s.append(sRow)
    return s


def multiply(a, b):
    m = []
    rows = len(a)
    cols = len(b[0])
    iters = len(a[0])

    for r in range(rows):
        mRow = []
        for c in range(cols):
            sum = 0
            for i in range(iters):
                sum += a[r][i] * b[i][c]
            mRow.append(sum)
        m.append(mRow)
    return m


def transposeMatrix(m):
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t


def getMatrixMinor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def getMatrixDeternminant(m):
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    d = 0
    for c in range(len(m)):
        d += ((-1) ** c) * m[0][c] * getMatrixDeternminant(getMatrixMinor(m, 0, c))

    return d


def getMatrixInverse(m):
    d = getMatrixDeternminant(m)

    if d == 0:
        raise Exception("Cannot get inverse of matrix with zero determinant")

    # special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1] / d, -1 * m[0][1] / d],
                [-1 * m[1][0] / d, m[0][0] / d]]

    # find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1) ** (r + c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / d
    return cofactors


def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return int(a * b / gcd(a, b))


def solution(m):
    m = sort(m)
    n = normalize(m)
    (q, r) = decompose(n)
    i = identity(len(q))
    s = subtract(i, q)
    v = getMatrixInverse(s)
    s = multiply(v, r)

    LCM = 1
    result = []
    for i in range(len(s[0]) - 1):
        if s[0][i].numerator == 0 or s[0][i + 1].numerator == 0:
            continue
        LCM = lcm(lcm(LCM, s[0][i].denominator), lcm(LCM, s[0][i + 1].denominator))

    for i in range(len(s[0])):
        result.append((s[0][i].numerator * LCM) // s[0][i].denominator)

    result.append(LCM)
    return result


class TestStringMethods(unittest.TestCase):

    def test_a(self):
        self.assertEqual(
            solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]),
            [7, 6, 8, 21])

    def test_b(self):
        self.assertEqual(solution(
            [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]), [0, 3, 2, 9, 14])


if __name__ == '__main__':
    unittest.main()
