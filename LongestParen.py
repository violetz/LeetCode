def longest_parentheses(str_paren):
    dic_longest_paren = {}
    i_longest_paren = 0
    i_temp_paren = 0
    ls_paren = []
    for c in str_paren:
        if c == '(':
            i_temp_paren = 0
            ls_paren.append(c)
        if c == ')':
            if len(ls_paren) == 0:
                i_longest_paren = max([i_longest_paren] + [i_temp_paren] + dic_longest_paren.values())
                i_temp_paren = 0
                dic_longest_paren = {}
            elif ls_paren.pop() == '(':
                i_temp_paren += 2
                i_rem_lparen = len(ls_paren)
                if i_rem_lparen in dic_longest_paren:
                    dic_longest_paren[i_rem_lparen] += i_temp_paren
                elif i_rem_lparen + 1 in dic_longest_paren:
                    dic_longest_paren[i_rem_lparen] = dic_longest_paren[i_rem_lparen + 1] + 2
                else:
                    dic_longest_paren[i_rem_lparen] = 2
            # else:
            #     i_longest_paren = max([i_longest_paren] + dic_longest_paren.values())
            #     i_temp_paren = 0
            #     ls_paren = []
            #     dic_longest_paren = {}
            #print ls_paren, i_longest_paren, i_temp_paren, dic_longest_paren
    i_longest_paren = max([i_longest_paren] + [i_temp_paren] + dic_longest_paren.values())
    #print i_longest_paren
    return i_longest_paren

# def l_p(str_paren):
#     dic_longest_paren = {0:0}
#     i_longest_paren = 0
#     i_temp_paren = 0
#     i_counter = 0
#     for c in str_paren:
#         if c == '(':
#             i_temp_paren = 0
#             i_counter += 1
#             dic_longest_paren[i_counter] = 0
#         if c == ')':
#             if i_counter == 0:
#             else:
#                 i_counter -= 1
                

def l_p(str_paren):
    i_longest_paren = 0
    ls_paren = [['', 0]]
    for c in str_paren:
        if c == '(':
            ls_paren.append([c, 0])
        if c == ')':
            if len(ls_paren) == 1:
                i_longest_paren = max(i_longest_paren, ls_paren[0][1])
                ls_paren = [['', 0]]
            else:
                lparen = ls_paren.pop()
                ls_paren[-1][1] += lparen[1] + 1
        print ls_paren, i_longest_paren
    i_longest_paren = max([i_longest_paren] + map(lambda x: x[1], ls_paren))
    return 2 * i_longest_paren

def direct_longest_paren(str_paren):
    #    print '*', str_paren
    if str_paren == '(' or str_paren == ')':
        return 0
    if str_paren[0] == ')':
        return direct_longest_paren(str_paren[1:])
    ls_paren = [str_paren[0]]
    i_temp_paren = 0
    for c in str_paren[1:]:
        #        print ls_paren, i_temp_paren
        if c == '(':
            ls_paren.append(c)
        if c == ')':
            if len(ls_paren) == 0:
                break
            elif ls_paren.pop() == '(':
                i_temp_paren += 2
            else:
                break
    return max(i_temp_paren, direct_longest_paren(str_paren[1:]))
    
def longest_parentheses_test():
    # import random
    # for i_test in range(300):
    #     len_paren = random.randint(1, 10)
    #     str_paren = ''.join(random.choice('()') for i in range(len_paren))
    file_data = open('longest_valid_parentheses.data')
    for line in file_data:
        print line
        ls_line = line.split()
        print ls_line
        str_paren = ls_line[0]
        assert(l_p(str_paren) == int(ls_line[1]))
    file_data.close()

if __name__ == '__main__':
    longest_parentheses_test()
