import string
from typing import List

from homework2.task01.text_func.dict_and_text import dict_and_text
from homework2.task01.text_func.fill_weight_list import fill_word_weight_list
from homework2.task01.text_func.read_text_func import read_text_func


def get_longest_diverse_words(file_path: str) -> List[str]:
    all_words = []
    text = read_text_func(file_path)
    count_dict, text = dict_and_text(text)
    for word in text.split():
        all_words.append(word)
    """Combine each word with its weight"""
    weight_and_words = sorted(
        list(set(zip(fill_word_weight_list(all_words, count_dict), all_words)))
    )
    """Longest words will be those whose length is greater
    than the average value of the lengths of all words
    """
    len_list = [len(i) for i in all_words]
    avg_len = sum(len_list) / len(len_list)
    longest_diverse_words = [
        i[1]
        for i in weight_and_words
        if len(weight_and_words[weight_and_words.index(i)][1]) >= avg_len
    ]
    return longest_diverse_words[0:10]


"""Count every char and return the rarest"""


def get_rarest_char(file_path: str) -> str:
    text = read_text_func(file_path)
    count_dict = {}
    for char in text:
        if char not in count_dict.keys():
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    for key, value in count_dict.items():
        if value == min(count_dict.values()):
            return key


"""Count ascii and non ascii punctuation marks"""


def count_punctuation_chars(file_path: str) -> int:
    counter = 0
    text = read_text_func(file_path)
    for char in text:
        if char in string.punctuation or ord(char) in [
            171,
            187,
            2014,
            2013,
            8250,
            2039,
        ]:
            counter += 1
    return counter


"""Count char if they order > max order of ascii char"""


def count_non_ascii_chars(file_path: str) -> int:
    text = read_text_func(file_path)
    counter = 0
    for char in text:
        if ord(char) > 128:
            counter += 1
    return counter


"""Count every non-ascii char and then return the most common"""


def get_most_common_non_ascii_char(file_path: str) -> str:
    text = read_text_func(file_path)
    count_dict = {}
    for char in text:
        if ord(char) > 128:
            if char not in count_dict.keys():
                count_dict[char] = 1
            else:
                count_dict[char] += 1
    for key, value in count_dict.items():
        if value == max(count_dict.values()):
            return key
