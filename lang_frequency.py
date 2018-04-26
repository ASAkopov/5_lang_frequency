import re
import chardet
from collections import Counter
from sys import argv


def load_data(filepath):
    with open(filepath, 'rb') as file:
        bytes_string = file.read()
        text_encoding = chardet.detect(bytes)['encoding']
        return bytes.decode(text_encoding)


def get_most_frequent_words(text_string, words_num):
    text_string = text_string.lower()
    words = re.findall(r'[a-zа-яё]+', text_string)

    words_counter = Counter(words)
    return words_counter.most_common(words_num)


if __name__ == '__main__':
    if len(argv) == 1:
       exit('Filepath was not specified.')
    file_path = argv[1]
    if len(argv) < 3:
        words_num = 10
    else:
        words_num = int(argv[2])
    try:
        text = load_data(file_path)
    except IOError:
        print('Can not open file.')
    else:
        print(get_most_frequent_words(text, words_num))
