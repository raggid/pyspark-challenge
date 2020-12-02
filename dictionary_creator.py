from hashlib import sha256


def create_dictionary(sc):
    dataset_dir = './dataset'
    files = sc.wholeTextFiles(dataset_dir)

    pairs = files.flatMap(lambda content: content[1].split()) \
        .map(lambda word: (word, sha256(word.encode('UTF-8')).hexdigest()))

    unique_pairs = pairs.reduceByKey(lambda a, b: a)

    with open('./dictionary', 'w', encoding='UTF-8') as file:
        for pair in unique_pairs.collect():
            file.write(f'{pair[0]} {pair[1]}\n')
