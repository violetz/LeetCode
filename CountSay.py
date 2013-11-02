def get_next(s_ints):
    ls_counts = []
    ind_c = 0
    len_ints = len(s_ints)
    while ind_c < len_ints:
        i_count = 0
        c_int = s_ints[ind_c]
        while ind_c < len_ints and s_ints[ind_c] == c_int:
            i_count += 1
            ind_c += 1
        ls_counts.extend([str(i_count), c_int])

    return ''.join(ls_counts)

def count_say(i_n):
    s_ints = '1'
    for ind_iter in range(i_n - 1):
        s_ints = get_next(s_ints)

    return s_ints
            
