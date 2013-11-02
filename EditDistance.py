import csv

def min_dist(s_1, s_2):
    if not s_1:
        return len(s_2)
    if not s_2:
        return len(s_1)
    
    i_len1 = len(s_1)
    i_len2 = len(s_2)

    ls_dist = [[0] * (i_len2 + 1) for i in range(i_len1 + 1)]

    ls_dist[0] = [j for j in range(i_len2 + 1)]
    for i in range(1, i_len1 + 1):
        ls_dist[i][0] = i

    for i in range(1, i_len1 + 1):
        for j in range(1, i_len2 + 1):
            ls_dist[i][j] = min(1 - (s_1[i-1]==s_2[j-1]) + ls_dist[i-1][j-1],
                                1 + ls_dist[i][j-1], 1 + ls_dist[i - 1][j])

    return ls_dist[-1][-1]

def min_dist_test():
    with open('EditDistanceTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            s_1, s_2 = eval(row[0])
            assert(min_dist(s_1, s_2) == int(row[1]))

if __name__ == '__main__':
    min_dist_test()
