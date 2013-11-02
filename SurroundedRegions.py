import csv

def surround(ls_board):
    if not ls_board:
        return
    i_nrow = len(ls_board)
    i_ncol = len(ls_board[0])

    for ind_col in range(i_ncol):
        mark_edge_O(ls_board, 0, ind_col)
        mark_edge_O(ls_board, i_nrow - 1, ind_col)

    for ind_row in range(1, i_nrow - 1):
        mark_edge_O(ls_board, ind_row, 0)
        mark_edge_O(ls_board, ind_row, i_ncol - 1)

    for ind_row in range(i_nrow):
        for ind_col in range(i_ncol):
            if ls_board[ind_row][ind_col] == '*':
                ls_board[ind_row][ind_col] = 'O'
            elif ls_board[ind_row][ind_col] == 'O':
                ls_board[ind_row][ind_col] = 'X'

    return

def mark_edge_O(ls_board, ind_row, ind_col):
    if ls_board[ind_row][ind_col] != 'O':
        return
    else:
        ls_board[ind_row][ind_col] = '*'
        ls_neighbors = find_neighbor(ls_board, ind_row, ind_col)
        for neighbor in ls_neighbors:
            mark_edge_O(ls_board, neighbor[0], neighbor[1])

    return

def find_neighbor(ls_board, ind_row, ind_col):
    i_nrow = len(ls_board)
    i_ncol = len(ls_board[0])
    ls_neighbors = []
    
    if ind_row - 1 >= 0:
        ls_neighbors.append([ind_row - 1, ind_col])
    if ind_row + 1 < i_nrow:
        ls_neighbors.append([ind_row + 1, ind_col])
    if ind_col -1 >= 0:
        ls_neighbors.append([ind_row, ind_col - 1])
    if ind_col + 1 < i_ncol:
        ls_neighbors.append([ind_row, ind_col + 1])

    return ls_neighbors

def surround_test():
    with open('SurroundedRegionsTest.csv') as testf:
        csvf = csv.reader(testf)
        next(csvf)
        for row in csvf:
            print row
            ls_board = map(list, eval(row[0]))
            surround(ls_board)
            assert(ls_board == map(list, eval(row[1])))

if __name__ == '__main__':
    surround_test()
