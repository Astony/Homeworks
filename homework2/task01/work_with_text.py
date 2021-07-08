import string
import unicodedata
from typing import List

from homework2.task01.text_func.counter_func import char_counter_func
from homework2.task01.text_func.fill_weight_list import fill_word_weight_list
from homework2.task01.text_func.words_func import words_list


def get_longest_diverse_words(
    file_path: str, encoding="utf-8", errors="ignore"
) -> List[str]:
    all_words = list(set(words_list(file_path, encoding=encoding, errors=errors)))
    counter = char_counter_func(file_path, encoding=encoding, errors=errors)
    letter_count = {
        key: value
        for key, value in counter.items()
        if unicodedata.category(key).startswith("L")
    }
    """Combine each word with its weight in pairs"""
    words_weight = fill_word_weight_list(all_words, letter_count)
    """Longest words will be those whose length is greater
    than the average value of the lengths of all words
    """
    len_list = [len(i) for i in all_words]
    avg_len = sum(len_list) / len(len_list)
    longest_diverse_words = [
        i[1]
        for i in words_weight
        if len(words_weight[words_weight.index(i)][1]) >= avg_len
    ]
    return longest_diverse_words[0:10]


"""Count every char and return the rarest"""


def get_rarest_char(file_path: str, encoding="utf-8", errors="ignore") -> str:
    counter = char_counter_func(file_path, encoding=encoding, errors=errors)
    return counter.most_common()[:-2:-1][0][0]


"""Count ascii and non ascii punctuation marks"""


def count_punc(file_path: str, encoding="utf-8", errors="ignore") -> int:
    counter = char_counter_func(file_path, encoding=encoding, errors=errors)
    punc_marks = {
        key: value
        for key, value in counter.items()
        if unicodedata.category(key).startswith("P")
    }
    return sum(punc_marks.values())


"""Count char if they order > max order of ascii char"""


def non_ascii(file_path: str, encoding="utf-8", errors="ignore") -> int:
    counter = char_counter_func(file_path, encoding=encoding, errors=errors)
    non_ascii_dict = {key: value for key, value in counter.items() if ord(key) > 128}
    return sum(non_ascii_dict.values())


"""Count every non-ascii char and then return the most common"""


def most_common_non_ascii(file_path: str, encoding="utf-8", errors="ignore") -> str:
    counter = char_counter_func(file_path, encoding=encoding, errors=errors)
    non_ascii_dict = {key: value for key, value in counter.items() if ord(key) > 128}
    for key, value in non_ascii_dict.items():
        if value == max(non_ascii_dict.values()):
            return key
