def New2DInd(ind_a, n):
    i_row = ind_a % (2 * n - 2)
    i_col = ind_a / (2 * n - 2)
    if i_row >= 0 and i_row <= n-1:
        i_col = 2 * i_col
    if i_row >= n:
        i_row = n - 1 - i_row % (n - 1)
        i_col = 2 * i_col + 1
    return i_row, i_col

def NewIndMap(ind_a, n):

def ZigZagConv(str_a, n):
    if n == 1:
        str_conv = str_a
    else:
        len_a = len(str_a)
        ncol = 2 * (len_a / (2 * n - 2)) + 1
        array_new = [[None] * ncol for item in range(n)]
        for ind_a in range(len_a):
            (i_row, i_col) = New2DInd(ind_a, n)
            array_new[i_row][i_col] = str_a[ind_a]
        str_conv = ''
        for i in range(n):
            for j in range(ncol):
                if array_new[i][j] == None:
                    continue
                str_conv += array_new[i][j]
    return str_conv
    
    

def ZigZagConvTest():
    import string
    import random
    for i_test in range(100):
        len_a = random.randint(1, 26)
        str_a = ''.join(random.choice(string.ascii_uppercase) for i in range(len_a))
        n = 0
        while n == 0:
            n = random.randint(1, len_a)
    
    
