import csv

def candy_wrong(ls_ratings):
    i_candy = 0
    stk_children = []
    i_cur_candy = 1

    for i in range(len(ls_ratings)):
        if not stk_children:
            stk_children.append([ls_ratings[i], i_cur_candy])
        elif ls_ratings[i] < stk_children[-1][0]:
            i_cur_candy -= 1
            stk_children.append([ls_ratings[i], i_cur_candy])
        elif ls_ratings[i] == stk_children[-1][0]:
            stk_children.append([ls_ratings[i], i_cur_candy])
        elif ls_ratings[i] > stk_children[-1][0]:
            if stk_children[-1][1] <= 1:
                b_more = True
                i_cur_candy = 2
            else:
                b_more = False
                if len(stk_children) == 1:
                    i_cur_candy = stk_children[-1][1] + 1
                else:
                    i_cur_candy = 2
            i_delta = 1 - stk_children[-1][1]
            while stk_children:
                i_rating, i_pre_candy = stk_children.pop()
                i_candy += i_pre_candy + i_delta
            if b_more == False:
                i_candy -= i_delta
            stk_children.append([ls_ratings[i], i_cur_candy])
        if i == len(ls_ratings) - 1:
            if stk_children[-1][1] <= 1:
                b_more = True
            else:
                b_more = False
            i_delta = 1 - stk_children[-1][1]
            while stk_children:
                i_rating, i_pre_candy = stk_children.pop()
                i_candy += i_pre_candy + i_delta
            if b_more == False:
                i_candy -= i_delta

    return i_candy

def candy(ls_ratings):

def candy_test():
    with open('CandyTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            ls_ratings = eval(row[0])
            assert(candy(ls_ratings) == int(row[1]))

if __name__ == '__main__':
    candy_test()
