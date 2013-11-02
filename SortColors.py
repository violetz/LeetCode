import csv

def sort_colors(ls_colors):
    ind_rw = -1
    ind_wb = len(ls_colors)
    ind_cur = 0
    while ind_cur < ind_wb:
        if ls_colors[ind_cur] == 0:
            ind_rw += 1
            ls_colors[ind_rw], ls_colors[ind_cur] = ls_colors[ind_cur], ls_colors[ind_rw]
            ind_cur += 1
        elif ls_colors[ind_cur] == 1:
            ind_cur += 1
        else:
            ind_wb -= 1
            ls_colors[ind_wb], ls_colors[ind_cur] = ls_colors[ind_cur], ls_colors[ind_wb]
            # print ls_colors

    return ls_colors

def sort_colors_test():
    with open('SortColorsTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            ls_colors = eval(row[0])
            print ls_colors
            assert(sort_colors(ls_colors) == eval(row[1]))

if __name__ == '__main__':
    sort_colors_test()
