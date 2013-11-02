import csv

def search_range(ls_ints, i_target):
    if not ls_ints:
        return [-1, -1]
    ind_left = -1
    ind_right = len(ls_ints)
    ind_lrange = -1
    ind_rrange = -1

    while ind_left < ind_right - 1:
        # print ind_left, ind_right
        ind_middle = (ind_left + ind_right) / 2
        if ls_ints[ind_middle] == i_target:
            if ind_middle > 0 and ls_ints[ind_middle - 1] == i_target:
                ind_right = ind_middle
            else:
                ind_lrange = ind_middle
                break
        elif ls_ints[ind_middle] < i_target:
            ind_left = ind_middle
        else:
            ind_right = ind_middle
            # print ind_left, ind_right

    if ind_lrange == -1:
        return [-1, -1]

    ind_right = len(ls_ints)

    while ind_left < ind_right - 1:
        ind_middle = (ind_left + ind_right) / 2
        if ls_ints[ind_middle] == i_target:
            if ind_middle < len(ls_ints) - 1 and ls_ints[ind_middle + 1] == i_target:
                ind_left = ind_middle
            else:
                ind_rrange = ind_middle
                break
        elif ls_ints[ind_middle] < i_target:
            ind_left = ind_middle
        else:
            ind_right = ind_middle

    return [ind_lrange, ind_rrange]

def search_range_test():
    with open('SearchRangeTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            ls_ints = map(int, row[0].split('], ')[0].strip('[]').split(','))
            i_target = int(row[0].split('], ')[1])
            assert(search_range(ls_ints, i_target) == eval(row[1]))

if __name__ == '__main__':
    search_range_test()
