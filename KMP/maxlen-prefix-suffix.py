# logic copy from https://www.youtube.com/watch?v=2ogqPWJSftE
# here we define a function that caculates NEXT array of KMP algorithm.

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


if __name__ == "__main__": # run unit tests.
    # case 1, no prefix-suffix equal
    res = maxlen_prefix_suffix('abcdefg')
    if ''.join(map(str, res)) == '0000000':
        print 'PASS'
    else:
        print 'Case 1 failed!'
        exit()

    # case 2, prefix-suffix equal
    res = maxlen_prefix_suffix('abcdabc')
    if ''.join(map(str, res)) == '0000123':
        print 'PASS'
    else:
        print 'Case 2 failed!'
        exit()





