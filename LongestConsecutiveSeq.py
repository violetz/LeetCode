import csv

def longest_seq(ls_nums):
    d_start = {}
    d_end = {}
    for i_num in ls_nums:
        if i_num in d_start or i_num in d_end:
            continue
        if i_num + 1 in d_start and i_num - 1 in d_end:
            i_end = d_start.pop(i_num + 1)
            i_start = d_end.pop(i_num - 1)
            d_start[i_start] = i_end
            d_end[i_end] = i_start
        elif i_num + 1 in d_start and i_num - 1 not in d_end:
            i_end = d_start.pop(i_num + 1)
            d_start[i_num] = i_end
            d_end[i_end] = i_num
        elif i_num + 1 not in d_start and i_num - 1 in d_end:
            i_start = d_end.pop(i_num - 1)
            d_end[i_num] = i_start
            d_start[i_start] = i_num
        else:
            d_start[i_num] = i_num
            d_end[i_num] = i_num

    i_longest = 0
    for k in d_start:
        i_longest = max(d_start[k] - k, i_longest)

    return i_longest + 1

def longest_seq_test():
    with open('LongestConsecutiveSeqTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            ls_nums = eval(row[0])
            print row[1]
            assert(longest_seq(ls_nums) == int(row[1]))

if __name__ == '__main__':
    longest_seq_test()
