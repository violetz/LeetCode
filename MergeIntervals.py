import csv
import numpy.random as nprnd

class Interval(object):
    def __init__(self, i_s, i_e):
        self.start = i_s
        self.end = i_e

    def __repr__(self):
        return str([self.start, self.end])

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def set_start(self, i_new_s):
        self.start = i_new_s

    def set_end(self, i_new_e):
        self.end = i_new_e

def sort_start(ls_intervals, ind_left, ind_right):
    if ind_right - ind_left < 1:
        return
    ind_rnd = nprnd.randint(ind_left, ind_right + 1)
    ls_intervals[ind_left], ls_intervals[ind_rnd] = \
      ls_intervals[ind_rnd], ls_intervals[ind_left]

    i_key = ls_intervals[ind_left].get_start()
    ind_part = ind_left
    for ind_cur in range(ind_left + 1, ind_right + 1):
        if ls_intervals[ind_cur].get_start() < i_key:
            ind_part += 1
            ls_intervals[ind_part], ls_intervals[ind_cur] = \
              ls_intervals[ind_cur], ls_intervals[ind_part]

    ls_intervals[ind_part], ls_intervals[ind_left] = \
      ls_intervals[ind_left], ls_intervals[ind_part]

    sort_start(ls_intervals, ind_left, ind_part - 1)
    sort_start(ls_intervals, ind_part + 1, ind_right)

    return

def merge(ls_intervals):
    if not ls_intervals:
        return []
    # sort_start(ls_intervals, 0, len(ls_intervals) - 1)
    # or python sort method
    # https://wiki.python.org/moin/HowTo/Sorting/
    ls_intervals.sort(key = lambda x: x.start)

    ls_merged = [ls_intervals[0]]
    for inter in ls_intervals[1:]:
        if inter.get_start() <= ls_merged[-1].get_end():
            ls_merged[-1].set_end(max(inter.get_end(), ls_merged[-1].get_end()))
        else:
            ls_merged.append(inter)

    return ls_merged

def merge_test():
    with open('MergeIntervalsTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            ls_vals = eval(row[0])
            ls_intervals = [Interval(sublist[0], sublist[1]) for sublist in ls_vals]
            ls_merged = merge(ls_intervals)
            assert(eval(str(map(repr, ls_merged)).replace("'", "")) == eval(row[1]))

if __name__ == '__main__':
    merge_test()
