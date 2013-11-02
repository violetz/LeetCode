import csv

def climb(i_n):
    if i_n < 1:
        return 0
    i_two_lower = 0
    i_one_lower = 1

    for ind_storey in range(i_n):
        i_one_lower, i_two_lower = i_one_lower + i_two_lower, i_one_lower

    return i_one_lower

def climb_test():
    with open('ClimbingStairsTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            i_n = int(row[0])
            assert(climb(i_n) == int(row[1]))

if __name__ == '__main__':
    climb_test()
