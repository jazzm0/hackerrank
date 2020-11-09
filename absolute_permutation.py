def absolute_permutation(n, k):
    if k == 0:
        # When k=0 we just have to print 1 to n
        print(*(range(1, n + 1)))
    elif (n / k) % 2 != 0.0:
        # pattern is not possible when k*2 is not divisible by n
        print(-1)
    else:
        # initialize an empty list
        arr = []
        # create a for loop with k*2 difference, example when k=3 --> 1,7,13,19,25....
        for i in range(1, n, k * 2):
            # numbers from i to i+k*2 example when k=3 and i = 1 --> [1,2,3,4,5,6]
            d = list(range(i, i + k * 2))
            # Slice and interchange left and right part, example [1,2,3,4,5,6] --> [4,5,6,1,2,3]
            arr += d[k:] + d[:k]
        print(*arr)


absolute_permutation(100, 2)
