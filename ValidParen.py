def check_paren(ls_parens):
    stk_left_parens = []
    for s_paren in ls_parens:
        if s_paren == '(' or s_paren == '{' or s_paren == '[':
            stk_left_parens.append(s_paren)
        elif len(stk_left_parens) == 0:
            return False
        elif s_paren == ')':
            s_left_paren = stk_left_parens.pop()
            if s_left_paren == '(':
                continue
            else:
                return False
        elif s_paren == ']':
            s_left_paren = stk_left_parens.pop()
            if s_left_paren == '[':
                continue
            else:
                return False
        elif s_paren == '}':
            s_left_paren = stk_left_parens.pop()
            if s_left_paren == '{':
                continue
            else:
                return False

    return True
        
