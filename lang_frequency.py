# -*- coding: utf8 -*-


import re

def load_data(filepath):
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