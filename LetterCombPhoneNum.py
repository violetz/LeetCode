import csv

def lett_comb(s_digits):
    if not s_digits:
        return ['']
    d_letters = dict(zip(map(str, range(10)), 
                         [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs',
                          'tuv', 'wxyz']))
    return get_lett_comb(d_letters, s_digits, 0)


def get_lett_comb(d_letters, s_digits, ind_start):
    if ind_start == len(s_digits) - 1:
        return list(d_letters[s_digits[-1]])
    ls_combs = []
    ls_sub_combs = get_lett_comb(d_letters, s_digits, ind_start + 1)
    # print ls_sub_combs
    for s_char in list(d_letters[s_digits[ind_start]]):
        for s_sub_comb in ls_sub_combs:
            # print s_char
            s_comb = s_char + s_sub_comb
            ls_combs.append(s_comb)
    return ls_combs

def lett_comb_iter(s_digits):
    if not s_digits:
        return ['']
    d_letters = dict(zip(map(str, range(10)), 
                         [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs',
                          'tuv', 'wxyz']))

    ind_end = len(s_digits) - 1
    while s_digits[ind_end] == '1':
        ind_end -= 1
    ls_combs = list(d_letters[s_digits[ind_end]])
    ind_end -= 1

    while ind_end >= 0:
        ls_sub_combs = ls_combs
        ls_combs = []
        for s_char in list(d_letters[s_digits[ind_end]]):
            for s_sub_comb in ls_sub_combs:
                s_comb = s_char + s_sub_comb
                ls_combs.append(s_comb)
        ind_end -= 1

    return ls_combs
        
def lett_comb_test():
    with open('LetterCombPhoneNumTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            s_digits = eval(row[0])
            set_expected = set(eval(row[1]))
            set_actual = set(lett_comb_iter(s_digits))
            print row
            assert(set_actual == set_expected)

if __name__ == '__main__':
    lett_comb_test()
