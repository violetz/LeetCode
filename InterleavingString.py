import csv

################### recursive solution ###########################
def is_interleave(s1, s2, s3):
    if len(s3) != len(s1) + len(s2):
        return False
    return find_interleave(s1, s2, s3, 0, 0, 0)

def find_interleave(s1, s2, s3, ind_s1, ind_s2, ind_s3):
    if ind_s1 == len(s1):
        if s2[ind_s2:] == s3[ind_s3:]:
            return True
        else:
            return False
    if ind_s2 == len(s2):
        if s1[ind_s1:] == s3[ind_s3:]:
            return True
        else:
            return False
        
    if s3[ind_s3] != s1[ind_s1] and s3[ind_s3] != s2[ind_s2]:
        return False

    if s3[ind_s3] == s1[ind_s1] and s3[ind_s3] != s2[ind_s2]:
        return find_interleave(s1, s2, s3, ind_s1 + 1, ind_s2, ind_s3 + 1)

    if s3[ind_s3] == s2[ind_s2] and s3[ind_s3] != s1[ind_s1]:
        return find_interleave(s1, s2, s3, ind_s1, ind_s2 + 1, ind_s3 + 1)

    if s3[ind_s3] == s1[ind_s1] and s3[ind_s3] == s2[ind_s2]:
        return (find_interleave(s1, s2, s3, ind_s1 + 1, ind_s2, ind_s3 + 1) or
                find_interleave(s1, s2, s3, ind_s1, ind_s2 + 1, ind_s3 + 1))

########################## dp ####################################
def is_interleave_dp(s1, s2, s3):
    if len(s3) != len(s1) + len(s2):
        return False
    i_len1 = len(s1)
    i_len2 = len(s2)
    ls_temp_state = [False] * (i_len2 + 1)
    for ind_s2 in range(i_len2 + 1):
        ls_temp_state[ind_s2] = s2[:ind_s2] == s3[:ind_s2]

    for ind_s1 in range(i_len1):
        ls_temp_state[0] &= s3[ind_s1] == s1[ind_s1]
        for ind_s2 in range(i_len2):
            ls_temp_state[ind_s2 + 1] = ((ls_temp_state[ind_s2] & 
                                          (s3[ind_s1 + ind_s2 + 1] == s2[ind_s2])) |
                                          (ls_temp_state[ind_s2 + 1]) &
                                          (s3[ind_s1 + ind_s2 + 1] == s1[ind_s1]))

    return ls_temp_state[-1]

########################## test ##################################
def find_interleave_test():
    with open('InterleavingStringTest.csv') as testf:
        csvf = csv.reader(testf)
        next(testf)
        for row in csvf:
            (s1, s2, s3) = eval(row[0])
            b_expected = row[1] == 'true'
            b_actual = is_interleave_dp(s1, s2, s3)
            print b_expected
            assert(b_expected == b_actual)

if __name__ == '__main__':
    find_interleave_test()
