<<<<<<< HEAD
import re
from collections import Counter
=======
# -*- coding: utf8 -*-
>>>>>>> 5e38714806c0197de50ee4bcac85e767ebe1ffa1


import re

def load_data(filepath):
<<<<<<< HEAD
    with open(filepath, "r", encoding = "cp1251") as file:
        return file.read()


def get_most_frequent_words(text_string):
    text_string.lower()
    words = re.findall(r"[a-zа-яё]+", text_string)

    words_counter = Counter()
    for word in words:
        words_counter[word] += 1

    return list(map(lambda a: a[0], words_counter.most_common(10)))


if __name__ == '__main__':
    text_file = input("Enter textfile path: ")
    text = load_data(text_file)
    print(get_most_frequent_words(text))
=======
    with open(filepath, 'r') as fid:
        text = fid.read()
    return text


def get_most_frequent_words(text):
    text = text.lower()
    words = re.findall(r'[a-zа-яё]+', text)

    word_dict = {}
    for wd in words:
        if wd in word_dict:
            word_dict[wd] += 1		
        else:
            word_dict[wd] = 1
    word_nums = word_dict.items()
    word_nums.sort(key = lambda x: x[1], reverse = True)
    return [x[0] for x in word_nums[0:10]]


if __name__ == '__main__':
    filepath = input(u'Введите путь к файлу: ')
    text = load_data(filepath)
    most_freq_word = get_most_frequent_words(text)
    for word in most_freq_word:
        print(word)
>>>>>>> 5e38714806c0197de50ee4bcac85e767ebe1ffa1
