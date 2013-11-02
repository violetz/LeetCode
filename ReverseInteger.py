import sys
MAX_INT = sys.maxint
MIN_INT = -sys.maxint - 1

def rev_int(i_x):
    b_sign = i_x >= 0
    i_x = abs(i_x)
    i_rev = 0
    b_overflow = False
    while i_x != 0:
        i_digit = i_x % 10
        if b_sign and i_rev <= (MAX_INT - i_digit) / 10:
            i_rev = i_rev * 10 + i_digit
        elif not b_sign and i_rev >= (MIN_INT + i_digit) / 10:
            i_rev = i_rev *10 - i_digit            
        else:
            b_overflow = True
            break
        i_x /= 10

    if not b_overflow:
        return i_rev
    else:
        return False    

def rev_int_test():
    import csv
    with open('ReverseIntegerTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            i_x = int(row[0])
            i_expected = int(row[1])
            i_actual = rev_int(i_x)
            print i_x, i_actual
            assert(i_expected == i_actual)

if __name__ == '__main__':
    rev_int_test()
