import pyspark
from dictionary_creator import create_dictionary
from indexer import index_words

if __name__ == '__main__':
    sc = pyspark.SparkContext('local[*]')

    create_dictionary(sc)
    index_words(sc)





