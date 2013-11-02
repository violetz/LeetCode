def search_word(array_chars, s_word):
    i_row = len(array_chars)
    i_col = len(array_chars[0])
    for ind_row in range(i_row):
        for ind_col in range(i_col):
            set_visited = set()
            if search_char(array_chars, s_word, ind_row, ind_col, set_visited):
                return True

    return False

def search_char(array_chars, s_word, 
                ind_start_row, ind_start_col, set_visited):
    if s_word == '':
        return True
    if (ind_start_row, ind_start_col) in set_visited:
        return False
    elif array_chars[ind_start_row][ind_start_col] == s_word[0]:
        set_visited.add((ind_start_row, ind_start_col))
        ls_neighbor = find_neighbor(array_chars, ind_start_row, ind_start_col)
        b_find = False
        if ls_neighbor == [] and s_word[1:] == '':
            b_find = True
        else:
            for ind_neighbor in ls_neighbor:
                b_find = (b_find or search_char(array_chars, s_word[1:], 
                                                ind_neighbor[0], ind_neighbor[1], set_visited))
        if b_find is False:
            set_visited.remove((ind_start_row, ind_start_col))
        return b_find
        
    
def find_neighbor(array_chars, ind_start_row, ind_start_col):
    i_row = len(array_chars)
    i_col = len(array_chars[0])
    ls_neighbor = []
    if ind_start_row - 1 >= 0:
        ls_neighbor.append((ind_start_row - 1, ind_start_col))
    if ind_start_row + 1 < i_row:
        ls_neighbor.append((ind_start_row + 1, ind_start_col))
    if ind_start_col - 1 >= 0:
        ls_neighbor.append((ind_start_row, ind_start_col - 1))
    if ind_start_col + 1 < i_col:
        ls_neighbor.append((ind_start_row, ind_start_col + 1))

    return ls_neighbor

def search_word_test():
    import csv
    with open('WordSearchTest.csv') as tfile:
        csvf = csv.reader(tfile)
        next(csvf)
        for row in csvf:
            print row
            s_chars, s_word = row[0].split(', ')
            array_chars = map(list, s_chars.strip('[]"').split('","'))
            s_word = s_word.strip('"')
            b_actual = search_word(array_chars, s_word)
            b_expected = row[1] == 'true'
            print b_actual, b_expected
            assert(b_actual == b_expected)
    
def main():
    # array_chars = [list("ABCE"), list("SFCS"), list("ADEE")]
    # s_word = 'ABCCED'
    # print search_word(array_chars, s_word)
    search_word_test()
    
if __name__ == '__main__':
    main()
