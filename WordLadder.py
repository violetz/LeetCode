def neighbor_words(s_word, set_dict):
    import string
    s_lowercases = string.ascii_lowercase
    ls_neighbors = []
    for i in range(len(s_word)):
        for c in s_lowercases:
            if c != s_word[i]:
                s_neighbor = s_word[:i] + c + s_word[(i+1):]
                if s_neighbor in set_dict:
                    ls_neighbors.append(s_neighbor)

    return ls_neighbors

def find_word_ladder1(s_start, s_end, set_dict): # too much memory
    from collections import deque
    set_dict.add(s_end)
    q_inter_words = deque()
    q_inter_words.append([s_start])
    i_ladder_length = 0
    ls_ladders = []

    while q_inter_words:
        ls_tran_words = q_inter_words.popleft()
        if i_ladder_length == 0 and ls_tran_words[-1] == s_end:
            i_ladder_length = len(ls_tran_words)
            break
        if (i_ladder_length != 0 and ls_tran_words[-1] == s_end
            and len(ls_tran_words) == i_ladder_length):
            ls_ladders.append(ls_tran_words)
        if i_ladder_length != 0 and len(ls_tran_words) > i_ladder_length:
            break
        # print '#', i_ladder_length, ls_tran_words
        ls_neighbors = neighbor_words(ls_tran_words[-1], set_dict)
        # print '*', ls_neighbors
        for s_neighbor in ls_neighbors:
            if s_neighbor not in ls_tran_words:
                q_inter_words.append(ls_tran_words + [s_neighbor])
            # print '@', q_inter_words

    return i_ladder_length, ls_ladders

def find_word_ladder_length(s_start, s_end, set_dict):
    from collections import deque
    set_dict.add(s_end)
    q_inter_words = deque()
    q_inter_words.append([s_start, 1])
    set_visited = set()
    set_visited.add(s_start)
    
    while q_inter_words:
        ls_last_word = q_inter_words.popleft()
        ls_neighbors = neighbor_words(ls_last_word[0], set_dict)
        for s_neighbor in ls_neighbors:
            if s_neighbor not in set_visited:
                if s_neighbor == s_end:
                    return ls_last_word[1] + 1
                q_inter_words.append([s_neighbor, ls_last_word[1] + 1])
                set_visited.add(s_neighbor)
            # print '@', q_inter_words

    return 0

def find_word_ladder_length2(s_start, s_end, set_dict): # without remembering cur length
    from collections import deque
    set_dict.add(s_end)
    q_inter_words = deque()
    q_inter_words.append(s_start)
    set_visited = set()
    set_visited.add(s_start)
    i_cur_level_nodes = 1
    i_next_level_nodes = 0
    i_ladder_length = 1
    
    while q_inter_words:
        s_last_word = q_inter_words.popleft()
        i_cur_level_nodes -= 1
        ls_neighbors = neighbor_words(s_last_word, set_dict)
        for s_neighbor in ls_neighbors:
            if s_neighbor not in set_visited:
                if s_neighbor == s_end:
                    return i_ladder_length + 1
                q_inter_words.append(s_neighbor)
                i_next_level_nodes += 1
                set_visited.add(s_neighbor)
            # print '@', q_inter_words

        if i_cur_level_nodes == 0:
            i_ladder_length += 1
            i_cur_level_nodes = i_next_level_nodes
            i_next_level_nodes = 0

    return 0

def find_word_ladder_length_test():
    import csv
    with open('WordLadderTest.csv') as tfile:
        csvf = csv.reader(tfile)
        next(csvf)
        for row in csvf:
            s_start, s_end = row[0].replace('"', '').split(', [')[0].split(', ')
            set_dict = set(row[0].replace('"', '').split(', [')[1].strip('[]').split(','))
            i_expected = int(row[1])
            i_actual = find_word_ladder_length2(s_start, s_end, set_dict)
            print row, i_actual
            assert(i_actual == i_expected)

if __name__ == '__main__':
    find_word_ladder_length_test()
