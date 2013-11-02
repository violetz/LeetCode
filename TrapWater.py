def trap_water_wrong(ls_height):
    i_water = 0
    i_lh = 0
    ind_lh = 0
    len_bar = len(ls_height)
    ind_bar = 0
    while True:
        while ind_bar < len_bar and ls_height[ind_bar] <= i_lh:
            i_water += i_lh - ls_height[ind_bar]
            if ls_height[ind_bar] == i_lh:
                ind_lh = ind_bar
            ind_bar += 1
            print '*', ind_bar, ls_height[ind_bar], ind_lh, i_lh, i_water
        if ind_bar == len_bar:
            i_water -= (i_lh - ls_height[-1]) * (ind_bar - 1 - ind_lh)
            break
        while ind_bar < len_bar and ls_height[ind_bar] >= ls_height[ind_bar - 1]:
            i_lh = ls_height[ind_bar]
            ind_lh = ind_bar
            ind_bar += 1
            print '#', ind_bar, ls_height[ind_bar], ind_lh, i_lh, i_water
        if ind_bar == len_bar:
            break
    return i_water
            
def trap_water(ls_height):
    i_water = 0
    len_bar = len(ls_height)
    ind_bar = 0
    stk_bars = []
    while ind_bar < len_bar:
        i_bar_h = ls_height[ind_bar]
        if stk_bars == [] or i_bar_h <= stk_bars[-1][1]:
            stk_bars.append((ind_bar, i_bar_h))
            print '*', ind_bar, stk_bars
        else:
            while len(stk_bars) > 0 and stk_bars[-1][1] < i_bar_h:
                (ind_right, i_right_h) = stk_bars.pop()
                if len(stk_bars) == 0:
                    break
                ind_left = stk_bars[-1][0]
                i_water += (ind_right - ind_left) * (i_bar_h - i_right_h)
                print '@', ind_bar, stk_bars, i_water
            if len(stk_bars) == 0:
                i_water -= (ind_bar - ind_right - 1) * (i_bar_h - i_right_h)
            stk_bars.append((ind_bar, i_bar_h))
            print '#', ind_bar, stk_bars, i_water
        ind_bar += 1
    return i_water
            
