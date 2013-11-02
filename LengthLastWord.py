import csv
import string

def length_last_word(s_string):
    if not s_string:
        return 0
    i_len = 0
    ind_c = len(s_string) - 1
    while ind_c >= 0 and s_string[ind_c] == ' ':
        ind_c -= 1
    while ind_c >= 0 and s_string[ind_c] != ' ':
        i_len += 1
        ind_c -= 1
    return i_len

def len_last_word(s_string):
    if not s_string:
        return 0
    i_len = 0
    i_tmp = 0
    for c in s_string:
        if c == ' ':
            i_tmp = 0
        else:
            i_tmp += 1
            i_len = i_tmp
    return i_len
    
def length_last_word_test():
    with open('LengthLastWordTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            s_string = eval(row[0])
            i_expected = int(row[1])
            i_actual = len_last_word(s_string)
            
            assert(i_actual == i_expected)

if __name__ == '__main__':
    length_last_word_test()
