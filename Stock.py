import csv

def max_prof(ls_prices):
    if not ls_prices:
        return (0, 0, 0)
    ind_buy = 0
    ind_sell = 0
    t_profit = (0, ind_buy, ind_sell)
    while ind_sell < len(ls_prices):
        if ls_prices[ind_sell] < ls_prices[ind_buy]:
            ind_buy = ind_sell

        while ind_sell + 1 < len(ls_prices) and ls_prices[ind_sell] < ls_prices[ind_sell + 1]:
            ind_sell += 1
            
        i_temp_profit = ls_prices[ind_sell] - ls_prices[ind_buy]
        if i_temp_profit > t_profit[0]:
            t_profit = (i_temp_profit, ind_buy, ind_sell)
        ind_sell += 1

    return t_profit

def max_prof_test():
    with open('StockTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            ls_prices = eval(row[0])
            print row
            assert(max_prof(ls_prices)[0] == int(row[1]))

def max_prof_multi(ls_prices):
    if not ls_prices:
        return 0
    ind_buy = 0
    ind_sell = 0
    i_profit = 0
    while ind_sell < len(ls_prices):
        ind_buy = ind_sell
        while ind_buy + 1 < len(ls_prices) and ls_prices[ind_buy] > ls_prices[ind_buy + 1]:
            ind_buy += 1
        ind_sell = ind_buy

        while ind_sell + 1 < len(ls_prices) and ls_prices[ind_sell] < ls_prices[ind_sell + 1]:
            ind_sell += 1
            
        i_profit += ls_prices[ind_sell] - ls_prices[ind_buy]
        
        ind_sell += 1

    return i_profit

def max_prof_multi_test():
    with open('Stock2Test.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            ls_prices = eval(row[0])
            print row
            assert(max_prof_multi(ls_prices) == int(row[1]))

if __name__ == '__main__':
    max_prof_multi_test()
