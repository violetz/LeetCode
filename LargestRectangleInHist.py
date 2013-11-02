def largest_rec(ls_heights):
    stk_left_edges = [(0, 0)]
    i_max_rec = 0
    len_bars = len(ls_heights)
    # while len(stk_left_edges) > 0 or ind_bar < len_bars:
    #     if ind_bar < len_bars:
    #         i_height = ls_heights[ind_bar]
    #     if len(stk_left_edges) > 0:
    #         ind_redge = stk_left_edges[-1][0]
    for ind_bar in range(len_bars + 1):
        if ind_bar < len_bars:
            i_height = ls_heights[ind_bar]
        ind_redge = stk_left_edges[-1][0]
        while len(stk_left_edges) > 1 and (i_height <= stk_left_edges[-1][1] or ind_bar == len_bars):
            (ind_ledge, i_ledge) = stk_left_edges.pop()
            if len(stk_left_edges) > 1:
                i_temp_rec = i_ledge * (ind_redge - ind_ledge + 1)
            else:
                i_temp_rec = i_ledge * (ind_redge)
            print i_temp_rec
            i_max_rec = max(i_max_rec, i_temp_rec)
            print '*', stk_left_edges, i_max_rec
        if ind_bar < len_bars:
            stk_left_edges.append((ind_bar+1, i_height))
        print '@', stk_left_edges, ind_bar
            
            
        # if stk_left_edges == [] or i_height > stk_left_edges[-1][1]:
        #     stk_left_edges.append((ind_bar, i_height))
        # else:
        #     ind_redge = stk_left_edges[-1][0]
        #     while len(stk_left_edges) > 0 and i_height <= stk_left_edges[-1][1]:
        #         (ind_ledge, i_ledge) = stk_left_edges.pop()
        #         if len(stk_left_edges) > 0:
        #             i_temp_rec = i_ledge * (ind_redge - ind_ledge + 1)
        #         else:
        #             i_temp_rec = i_ledge * (ind_redge + 1)
        #         i_max_rec = max(i_max_rec, i_temp_rec)
                
        #     stk_left_edges.append((ind_bar, i_height))
            
    return i_max_rec
