# use maxlen-prefix-suffix to calculate KMP NEXT array.

# passing a non-empty string in, give its prefix-suffix equal len array.
def maxlen_prefix_suffix(P):
    P = '0' + P # make the real string starting from index 1.
    L = len(P) - 1 # so real length is 'minus one'.
    Prefix = [0] * (L + 1) # prepend a 0 to make index start from 1.
    a = 0
    for b in range(2, L + 1): # iterating from 2 to L, (L - 2 + 1) times of iterations.
        while a > 0 and P[a + 1] != P[b]:
            a = Prefix[a]

        if P[a + 1] == P[b]:
            a += 1

        Prefix[b] = a

    return Prefix[1:]

def kmp(T, P):
    # find one match, and return, or nothing.
    NEXT = maxlen_prefix_suffix(P)

    LT, LP = len(T), len(P)
    i, j = 0, 0 # loop var used by TEXT and PATTERN.
    while i < LT:
        cand = i
        while j < LP and i < LT and T[i] == P[j]:
            i += 1
            j += 1
        if j >= LP:
            return cand
        else:
            if j - 1 >= 0:
                max_prefix_suffix_len = NEXT[j - 1]
                j = max_prefix_suffix_len
            else:
                i += 1
    return -1

def kmp_multi(T, P):
    # result array for holding indexes.
    res = []
    # calculate NEXT array.
    NEXT = maxlen_prefix_suffix(P)

    LT, LP = len(T), len(P)
    i, j = 0, 0 # loop var used by TEXT and PATTERN.
    while i < LT:
        cand = i
        while j < LP and i < LT and T[i] == P[j]:
            i += 1
            j += 1
        if j >= LP:
            res.append(cand)
            max_prefix_suffix_len = NEXT[LP - 1]
            j = max_prefix_suffix_len
        else:
            if j - 1 >= 0:
                max_prefix_suffix_len = NEXT[j - 1]
                j = max_prefix_suffix_len
            else:
                i += 1
    return res

if __name__ == "__main__":
    # run unit tests
    # case 1, no match
    T = 'abcdeabcd'
    P = 'fgh'
    res = kmp(T, P)
    if res == -1:
        print 'PASS'
    else:
        print 'FAILED'

    # case 2, one match
    T = 'abcdeabcd'
    P = 'eabcd'
    res = kmp(T, P)
    if res == 4:
        print 'PASS'
    else:
        print 'FAILED'






