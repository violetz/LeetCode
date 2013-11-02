def FindLongestLen(s_a):
    i_maxlen = 0
    i_curlen = 0
    d_chars = {}
    for i in range(len(s_a)):
        if s_a[i] not in d_chars:
            d_chars[s_a[i]] = i
            i_curlen += 1
        else:
            i_lentmp = i - d_chars[s_a[i]]
            d_chars[s_a[i]] = i
            i_curlen = min(i_curlen+1, i_lentmp)
            # print i_lentmp
        i_maxlen = max(i_maxlen, i_curlen)
        #        print i_maxlen, i_curlen, d_chars
    return i_maxlen

def RightLen(s_a):
    i_maxlen = 0
    for i in range(len(s_a)):
        for j in range(i, len(s_a)):
            ls_substr = list(s_a[i:j+1])
            set_substr = set(ls_substr)
            # print ls_substr
            # print set_substr
            if len(ls_substr) != len(set_substr):
                # print i, j, i_maxlen      
                i_maxlen = max(i_maxlen, j-i)
                break
            if j == len(s_a) -1:
                i_maxlen = max(i_maxlen, j-i+1)
    return i_maxlen
    
def FindLongestLenTest():
    import string
    import random

    for i in range(500):
        i_len = random.choice(range(50))
        s_a = ''.join(random.choice(string.ascii_lowercase) 
                      for j in range(i_len))
        print s_a
        print RightLen(s_a), FindLongestLen(s_a)
        assert(RightLen(s_a) == FindLongestLen(s_a))

if __name__ == '__main__':
    FindLongestLenTest()
