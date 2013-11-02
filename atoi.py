def atoi(str_a):
    if str_a == '':
        return None
    
    len_a = len(str_a)
    ind_c = 0
    while ind_c < len_a and str_a[ind_c] == ' ':
        ind_c += 1
    if ind_c == len_a:
        return None

    i_conv = 0
    i_sign = 1
    if str_a[ind_c] == '-':
        i_sign = -1
        ind_c += 1
    elif str_a[ind_c] == '+':
        ind_c += 1
    else:
        try:
            i_conv = int(str_a[ind_c])
            ind_c += 1
        except ValueError:
            return None

    while ind_c < len_a:
        try:
            i_conv = i_conv * 10 + int(str_a[ind_c])
        except ValueError:
            break
        ind_c += 1

    return i_conv * i_sign
