def TwoSum(ls_num, f_target):
    d_num = {}
    for i in range(len(ls_num)):
        f_other = f_target - ls_num[i]
        if f_other in d_num:
            return (d_num[f_other][0], i+1)
        else:
            if ls_num[i] in d_num:
                d_num[ls_num[i]].append(i+1)
            else:
                d_num[ls_num[i]] = [i+1]
        pass

def TwoSumTest():
    ls_num1 = [2, 5, 9, 4, 4]
    f_target1 = 7
    f_target2 = 8.0
    f_target3 = 6
    assert((1, 2) == TwoSum(ls_num1, f_target1))
    assert((4, 5) == TwoSum(ls_num1, f_target2))
    assert((1, 4) == TwoSum(ls_num1, f_target3))
    return

if __name__ == '__main__':
    TwoSumTest()


