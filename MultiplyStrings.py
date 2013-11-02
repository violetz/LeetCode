import csv

def add_string(s_num1, s_num2):
    if s_num1 == '':
        return s_num2
    if s_num2 == '':
        return s_num1
    i_max_len = max(len(s_num1), len(s_num2))
    s_num1 = '0' * (i_max_len - len(s_num1)) + s_num1 ## padding 0 in the front
    s_num2 = '0' * (i_max_len - len(s_num2)) + s_num2

    s_sum = ''
    for ind_num in reversed(range(i_max_len)):
        i_temp_sum = int(s_num1[ind_num]) + int(s_num2[ind_num])
        # print s_sum, i_temp_sum
        if len(s_sum) > i_max_len - ind_num - 1:
            i_temp_sum += int(s_sum[0])
            s_sum = str(i_temp_sum) + s_sum[1:]
        else:
            s_sum = str(i_temp_sum) + s_sum

    return s_sum

def multiply_string_char(s_num1, s_num2, ind_num2, ls_sub_prod):
    """int(s_num1) * int(s_num2[ind_num2]) as string
    store in ls_sub_prod"""

    s_prod = ''
    for ind_num1 in reversed(range(len(s_num1))):
        i_temp = int(s_num1[ind_num1]) * int(s_num2[ind_num2])
        if i_temp == 0:
            continue
        s_temp = str(i_temp) + '0' * (len(s_num1) - ind_num1 - 1)
        s_prod = add_string(s_temp, s_prod)

    if s_prod:
        s_prod = s_prod + '0' * (len(s_num2) - ind_num2 - 1)
    ls_sub_prod.append(s_prod)

    return
    
def multiply_strings(s_num1, s_num2):
    ls_sub_prod = []

    for ind_num2 in reversed(range(len(s_num2))):
        multiply_string_char(s_num1, s_num2, ind_num2, ls_sub_prod)

    s_prod = reduce(add_string, ls_sub_prod)

    if not s_prod:
        s_prod = '0'

    return s_prod

def multiply_strings_test():
    with open('MultiplyStringsTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            s_num1, s_num2 = eval(row[0])
            assert(multiply_strings(s_num1, s_num2) == eval(row[1]))

if __name__ == '__main__':
    multiply_strings_test()
