import re
from collections import Counter
from sys import argv, exit


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_most_frequent_words(text_string, words_num):
    text_string.lower()
    words = re.findall(r'[a-zа-яё]+', text_string)

    words_counter = Counter(words)
    return list(map(lambda a: a[0], words_counter.most_common(words_num)))


if __name__ == '__main__':
    if len(argv) == 1:
       exit('Filepath was not specified.')
    file_path = argv[1]
    try:
        text = load_data(file_path)
    except IOError:
        print('Can not open file.')
    else:
        get_most_frequent_words(text)
