import csv

def longest_pre(ls_strs):
    if not ls_strs:
        return ''
    i_str_num = len(ls_strs)

    i_max_len = 0
    while i_max_len < len(ls_strs[0]):
        c_comp = ls_strs[0][i_max_len]
        for ind_str in range(1, i_str_num):
            if i_max_len >= len(ls_strs[ind_str]) or ls_strs[ind_str][i_max_len] != c_comp:
                return ls_strs[0][: i_max_len]
        i_max_len += 1

    return ls_strs[0]

def longest_pre_test():
    with open('LongestCommonPrefixTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            ls_strs = eval(row[0])
            assert(longest_pre(ls_strs) == eval(row[1]))

if __name__ == '__main__':
    longest_pre_test()
