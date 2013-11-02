def check_valid_palindrome(s_a):
    import string
    s_alpha_num = (string.ascii_lowercase + string.ascii_uppercase +
                   ''.join(str(i) for i in range(10)))
    len_a = len(s_a)
    ind_left = 0
    ind_right = len_a - 1
    while True:
        while ind_left < len_a and s_a[ind_left] not in s_alpha_num:
            ind_left += 1
            # print 'left', ind_left
        while ind_right > -1 and s_a[ind_right] not in s_alpha_num:
            ind_right -= 1
            # print 'right', ind_right
        if ind_left > ind_right:
            break
        c_left = s_a[ind_left].lower()
        c_right = s_a[ind_right].lower()
        if c_left != c_right:
            return False
        ind_left += 1
        ind_right -= 1

    return True

def check_valid_palindrome_test():
    import csv
    with open('ValidPalindromeTest.csv') as tfile:
        csvf = csv.reader(tfile)
        next(csvf)
        for row in csvf:
            s_a = row[0]
            b_expected = row[1] == 'true'
            print b_expected
            assert(check_valid_palindrome(s_a) == b_expected)

if __name__ == '__main__':
    check_valid_palindrome_test()
