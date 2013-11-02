def map_word_to_char_count(d_char, s_word):
    ls_char_counts = [0 for i in range(len(d_char.keys()))]
    for c in s_word:
        ls_char_counts[d_char[c]] += 1
        # return ''.join(map(str, ls_char_counts))
    return ''.join(str(i) for i in ls_char_counts)

def find_anagrams(ls_words):
    import string
    lowercase = string.ascii_lowercase
    d_char = dict(zip(list(lowercase), range(len(lowercase))))
    d_words = {}
    ls_anagrams = []
    for s_word in ls_words:
        s_char_count = map_word_to_char_count(d_char, s_word)
        if s_char_count in d_words:
            d_words[s_char_count].append(s_word)
        else:
            d_words[s_char_count] = [s_word]

    for key in d_words.iterkeys():
        if len(d_words[key]) > 1:
            ls_anagrams.extend(d_words[key])

    return ls_anagrams

def find_anagrams_test():
    import csv
    with open('AnagramsTest.csv') as tfile:
        csvf = csv.reader(tfile)
        next(csvf)
        for row in csvf:
            print row
            ls_words = row[0].strip('[]').replace('"', '').split(',')
            print ls_words
            ls_expected = row[1].strip('[]').replace('"', '').split(',')
            if ls_expected == ['']:
                set_expected = set([])
            else:
                set_expected = set(ls_expected)
            set_actual = set(find_anagrams(ls_words))
            print set_expected, 'actual:', set_actual
            print
            assert(set_actual == set_expected)

if __name__ == '__main__':
    find_anagrams_test()

