# %%
import pyspark
from os import listdir

# %%
sc = pyspark.SparkContext('local[*]')

# %%
dataset_dir = './dataset'
files = sc.wholeTextFiles(dataset_dir)

## %%
#collection = sc.parallelize(files)

# %%
acc = sc.accumulator(0)


# %%
def reduceWordsByKey(a, b):
    wordId = acc.value
    acc.add(1)
    return wordId


# %%
split_content = files.flatMap(lambda content: content[1].split()).map(lambda word: (word, 1))

# %%
words = split_content.reduceByKey(lambda a, b: a + b)

# %%
unique_words = words.collect()
