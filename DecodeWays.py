import csv

def decode_ways(s_digits):
    if not s_digits or s_digits[0] == '0':
        return 0
    set_one_way = set(range(1, 11) + [20])
    set_two_ways = set(range(11, 20) + range(21, 27))
    i_pre_two = 1
    i_pre_one = 1
    for ind_dig in range(1, len(s_digits)):
        if s_digits[ind_dig] == '0':
            if int(s_digits[ind_dig - 1 : ind_dig + 1]) not in set_one_way:
                return 0
            else:
                i_pre_one, i_pre_two = i_pre_two, i_pre_one
        elif s_digits[ind_dig - 1] != '0':
            if int(s_digits[ind_dig - 1 : ind_dig + 1]) in set_two_ways:
                i_pre_one, i_pre_two = i_pre_one + i_pre_two, i_pre_one
            else:
                i_pre_one, i_pre_two = i_pre_one, i_pre_one
        else:
            i_pre_one, i_pre_two = i_pre_one, i_pre_one

    return i_pre_one

def decode_ways_test():
    with open('DecodeWaysTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            s_digits = eval(row[0])
            print row
            assert(decode_ways(s_digits) == int(row[1]))

if __name__ == '__main__':
    decode_ways_test()
