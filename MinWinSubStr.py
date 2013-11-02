class MyDict(dict):
    def __ge__(self, d_other):
        return all(self[c] >= d_other[c] for c in self.keys())

# def ge_dicts(d_1, d_2):
#     """all the values of d_1 are >= d_2 for keys in d_1"""
#     return all(d_1[c] >= d_2[c] for c in d_1.keys())

def find_min_window(s_text, s_sub):
    from collections import deque
    # from collections import Counter
    # cnt = Counter(s_sub)
    set_sub = set(s_sub)
    d_sub = MyDict((c, s_sub.count(c)) for c in set_sub)
    d_has_found = MyDict(zip(set_sub, [0] * len(set_sub)))
    q_key_pos = deque()
    s_window = ''

    for ind_c in xrange(len(s_text)):
        c_cur = s_text[ind_c]
        if c_cur in set_sub:
            d_has_found[c_cur] += 1
            q_key_pos.append((c_cur, ind_c))
            while d_has_found >= d_sub:
                c_left, ind_left = q_key_pos.popleft()
                d_has_found[c_left] -= 1
                if s_window == '':
                    s_window = s_text[ind_left : (ind_c + 1)]
                elif ind_c - ind_left + 1 < len(s_window):
                    s_window = s_text[ind_left : (ind_c + 1)]

    return s_window

def find_min_window_test():
    import csv
    with open('MinWinSubStrTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            s_text, s_sub = row[0].replace('"', '').split(', ')
            s_expected = row[1].strip('"')
            s_actual = find_min_window(s_text, s_sub)
            print s_actual
            assert(s_actual == s_expected)

if __name__ == '__main__':
    find_min_window_test()
        
