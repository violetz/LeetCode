import csv

def sqrt(i_x):
    if i_x < 0:
        return None
    if i_x <= 1:
        return i_x

    i_left = 0
    i_right = i_x

    while i_left < i_right - 1:
        i_mid = i_left + (i_right - i_left) / 2
        i_mid_square = i_mid ** 2
        if i_mid_square == i_x:
            return i_mid
        elif i_mid_square < i_x:
            i_left = i_mid
        else:
            i_right = i_mid

    return i_left

def sqrt_test():
    with open('SqrtTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            assert(sqrt(int(row[0])) == int(row[1]))

if __name__ == '__main__':
    sqrt_test()
