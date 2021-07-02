import string
import unicodedata
from typing import List

from homework2.task01.text_func.char_dict import char_dict
from homework2.task01.text_func.fill_weight_list import fill_word_weight_list
from homework2.task01.text_func.letter_dict import letter_dict
from homework2.task01.text_func.words_func import words_list


def get_longest_diverse_words(
    file_path: str, encoding="utf-8", errors="ignore"
) -> List[str]:
    all_words = list(words_list(file_path, encoding=encoding, errors=errors))
    letter_count = letter_dict(file_path, encoding=encoding, errors=errors)
    """Combine each word with its weight in pairs"""
    uniq_pairs = set(zip(fill_word_weight_list(all_words, letter_count), all_words))
    weight_and_words = sorted(list(uniq_pairs))
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


def get_rarest_char(file_path: str, encoding="utf-8", errors="ignore") -> str:
    count_dict = char_dict(file_path, encoding=encoding, errors=errors)
    for key, value in count_dict.items():
        if value == min(count_dict.values()):
            return key


"""Count ascii and non ascii punctuation marks"""


def count_punc(file_path: str, encoding="utf-8", errors="ignore") -> int:
    with open(file_path, encoding=encoding, errors=errors) as file_input:
        counter = 0
        while char := file_input.read(1):
            if unicodedata.category(char).startswith("P"):
                counter += 1
    return counter


"""Count char if they order > max order of ascii char"""


def non_ascii(file_path: str, encoding="utf-8", errors="ignore") -> int:
    with open(file_path, encoding=encoding, errors=errors) as file_input:
        counter = 0
        while char := file_input.read(1):
            if ord(char) > 128:
                counter += 1
    return counter


"""Count every non-ascii char and then return the most common"""


def most_common_non_ascii(file_path: str, encoding="utf-8", errors="ignore") -> str:
    with open(file_path, encoding=encoding, errors=errors) as file_input:
        non_asc_dict = {}
        while char := file_input.read(1):
            if ord(char) > 128:
                if char not in non_asc_dict:
                    non_asc_dict[char] = 1
                else:
                    non_asc_dict[char] += 1
    for key, value in non_asc_dict.items():
        if value == max(non_asc_dict.values()):
            return key
