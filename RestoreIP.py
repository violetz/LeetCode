import csv

def partition_ip(s_digits, i_part):
    ls_part = []
    if i_part == 1 and 0 < len(s_digits) < 4 and 0 <= int(s_digits) <= 255:
        if not (len(s_digits) > 1 and s_digits[0] == '0'):
            ls_part.append([s_digits])
    if i_part > 1 and i_part <= len(s_digits) <= 3*i_part:
        for i in range(3):
            if s_digits[0] == '0' and i > 0:
                break
            i_ip = int(s_digits[:(i+1)])
            if 0 <= i_ip <= 255:
                ls_sub_part = partition_ip(s_digits[(i+1):], i_part - 1)
                for sub_part in ls_sub_part:
                    if len(sub_part) == i_part - 1:
                        ls_part.append([s_digits[:(i+1)]] + sub_part)
                # ls_part.append([i_ip] + sub_part for sub_part in ls_sub_part 
                #                 if len(sub_part) == i_part - 1)
                # above commented code result in generator!
    return ls_part

def restore_ip(s_digits):
    ls_part = partition_ip(s_digits, 4)
    return ['.'.join(s_part) for s_part in ls_part]
    
def restore_ip_test():
    with open('RestoreIPTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            s_digits = eval(row[0])
            set_expected = set(eval(row[1]))
            set_actual = set(restore_ip(s_digits))
            print row
            assert(set_expected == set_actual)

if __name__ == '__main__':
    restore_ip_test()
