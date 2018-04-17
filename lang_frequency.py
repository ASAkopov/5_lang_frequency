import re
from collections import Counter


def load_data(filepath):
    with open(filepath, "r", encoding = "cp1251") as file:
        return file.read()


def get_most_frequent_words(text_string, words_num):
    text_string.lower()
    words = re.findall(r"[a-zа-яё]+", text_string)

    words_counter = Counter()
    for word in words:
        words_counter[word] += 1

    return list(map(lambda a: a[0], words_counter.most_common(words_num)))


if __name__ == '__main__':
    words_num = 10
    text_file = input("Enter textfile path: ")
    text = load_data(text_file)
    print(get_most_frequent_words(text))
