import csv

def simplify(s_path):
    stk_dir = []

    ind_c = 0
    while ind_c < len(s_path):
        while ind_c < len(s_path) and s_path[ind_c] == '/':
            ind_c += 1
        ind_start = ind_c
        while ind_c < len(s_path) and s_path[ind_c] != '/':
            ind_c += 1
        s_dir = s_path[ind_start : ind_c]
        if s_dir == '' or s_dir == '.':
            continue
        elif s_dir == '..':
            if stk_dir:
                stk_dir.pop()
        else:
            stk_dir.append(s_dir)

    return '/' + '/'.join(stk_dir)
            
def simplify_test():
    with open('SimplifyPathTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            s_path = eval(row[0])
            assert(simplify(s_path) == eval(row[1]))

if __name__ == '__main__':
    simplify_test()
