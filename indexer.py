def index_words(sc):
    word_dict = {}
    with open('./dictionary', 'r') as file:
        for line in file:
            key, value = line.split()
            word_dict[key] = value

    bc_word_dict = sc.broadcast(word_dict)
    files = sc.wholeTextFiles('./dataset')

    words_by_file = files.map(lambda content: (content[0].split('/')[-1], content[1].split()))

    fileId_word = words_by_file.flatMapValues(lambda words: [word for word in words])
    wordId_fileId = fileId_word.map(lambda pair: (bc_word_dict.value[pair[1]], int(pair[0])))

    files_by_word = wordId_fileId.combineByKey(create_combiner, merge_value, merge_combiners)
    sorted_files_by_word = files_by_word.map(lambda pair: (pair[0], sorted(list(set(pair[1])))))

    sorted_words = sorted_files_by_word.sortByKey().collect()

    with open('./inverted_index', 'w', encoding='UTF-8') as file:
        for pair in sorted_words:
            file.write(f'{pair[0]} {pair[1]}\n')


def create_combiner(a):
    return [a]


def merge_value(a, b):
    a.append(b)
    return a


def merge_combiners(a, b):
    a.extend(b)
    return a
