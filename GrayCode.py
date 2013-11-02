import csv

def gray_code(i_n):
    ls_code = [0]
    for ind_bit in range(i_n):
        i_len_sub_code = len(ls_code)
        i_new_bit = 2 ** ind_bit
        for ind_sub_code in reversed(range(i_len_sub_code)):
            ls_code.append(i_new_bit | ls_code[ind_sub_code])

    return ls_code
    
def gray_code_test():
    with open('GrayCodeTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            i_n = int(row[0])
            print i_n
            assert(gray_code(i_n) == eval(row[1]))

if __name__ == '__main__':
    gray_code_test()
