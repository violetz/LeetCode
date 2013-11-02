def full_justify(ls_words, i_l):
    ls_lines = []

    ind_line_end = 0
    while ind_line_end < len(ls_words):
        ind_line_start = ind_line_end
        i_len = 0
        while ind_line_end < len(ls_words) and i_len <= i_l + 1:
            i_len += len(ls_words[ind_line_end]) + 1
            ind_line_end += 1
        
        if ind_line_end == len(ls_words) and i_len <= i_l + 1:
            s_line = ' '.join(ls_words[ind_line_start:ind_line_end])
            s_line += ' ' * (i_l - len(s_line))
            
        else:
            ind_line_end -= 1
            i_len -= len(ls_words[ind_line_end]) + 1 + (ind_line_end - ind_line_start)
            i_spaces = i_l - i_len

            if ind_line_end == ind_line_start + 1:
                s_line = ls_words[ind_line_start] + ' ' * i_spaces
            else:
                i_interval_num = ind_line_end - ind_line_start - 1
                i_right_space = i_spaces / i_interval_num
                i_tot_left_space = i_spaces % i_interval_num
                s_line = ''
                for iter_word in xrange(ind_line_start, ind_line_start + i_tot_left_space):
                    s_line += ls_words[iter_word] + ' ' * (i_right_space + 1)
                for iter_word in xrange(ind_line_start + i_tot_left_space, ind_line_end - 1):
                    s_line += ls_words[iter_word] + ' ' * i_right_space
                s_line += ls_words[ind_line_end - 1]
        ls_lines.append(s_line)

    return ls_lines

def full_justify_recursion(ls_words, i_l):
    if sum(map(len, ls_words)) + len(ls_words) - 1 <= i_l:
        s_line = ' '.join(ls_words)
        i_line_len = len(s_line)
        s_line += ' ' * (i_l - i_line_len)
        return [s_line]
    
    ind_word = -1
    i_len = 0
    while ind_word < len(ls_words) and i_len <= i_l + 1:
        ind_word += 1
        i_len += len(ls_words[ind_word]) + 1
    i_len -= len(ls_words[ind_word]) + 1 + ind_word
    i_spaces = i_l - i_len
    
    if ind_word == 1:
        s_line = ls_words[0] + ' ' * i_spaces
    else:
        i_interval_num = ind_word - 1
        i_right_space = i_spaces / i_interval_num
        i_tot_left_space = i_spaces % i_interval_num
        s_line = ''
        for iter_word in xrange(i_tot_left_space):
            s_line += ls_words[iter_word] + ' ' * (i_right_space + 1)
        for iter_word in xrange(i_tot_left_space, ind_word - 1):
            s_line += ls_words[iter_word] + ' ' * i_right_space
        s_line += ls_words[ind_word - 1]
    return [s_line] + full_justify_recursion(ls_words[ind_word:], i_l)
    
def full_justify_recursion_test():
    import csv
    with open('TextJustificationTest.csv') as tfile:
        csvf = csv.reader(tfile)
        next(csvf)
        for row in csvf:
            ls_words = row[0].split('], ')[0].strip('[]"').split('","')
            i_l = int(row[0].split('], ')[1])
            ls_1 = full_justify(ls_words, i_l)
            ls_actual = full_justify_recursion(ls_words, i_l)
            print ls_words, ls_1
            assert(ls_1 == ls_actual)

if __name__ == '__main__':
    full_justify_recursion_test()
    
