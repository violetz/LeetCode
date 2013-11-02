def plus_one(ls_digits):
    b_carry = False
    for ind_i in reversed(range(len(ls_digits))):
        if ls_digits[ind_i] != 9:
            ls_digits[ind_i] += 1
            break
        else:
            ls_digits[ind_i] = 0
            if not b_carry:
                b_carry = True
    if ind_i == 0 and b_carry:
        ls_digits.insert(0, 1)

    return ls_digits
        
