import string
from typing import List

from homework2.task01.fill_weight_list import fill_word_weight_list


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        all_words = []
        text = []
        count_dict = {}
        for lines in f:
            text.append(lines.encode().decode("unicode-escape").strip())
        text = " ".join(text)
        for char in text:
            if (
                char in string.punctuation
                or ord(char) in [171, 187, 2014, 2013]
                or char.isdigit()
            ):
                text = text.replace(char, "")
            elif char not in count_dict.keys():
                count_dict[char] = 1
            else:
                count_dict[char] += 1
        for word in text.split():
            all_words.append(word)
        """combine each word with its weight"""
        weight_and_words = sorted(
            list(set(zip(fill_word_weight_list(all_words, count_dict), all_words)))
        )
        """the longest words will be those whose length is greater
         than the average value of the lengths of all words"""
        len_list = [len(i) for i in all_words]
        avg_len = sum(len_list) / len(len_list)
        longest_diverse_words = [
            i[1]
            for i in weight_and_words
            if len(weight_and_words[weight_and_words.index(i)][1]) > avg_len
        ]
        return longest_diverse_words[0:10]


def get_rarest_char(file_path: str) -> str:
    text = []
    count_dict = {}
    with open(file_path, "r") as f:
        for lines in f:
            text.append(lines.encode().decode("unicode-escape").strip())
        text = " ".join(text)
        for char in text:
            if char not in count_dict.keys():
                count_dict[char] = 1
            else:
                count_dict[char] += 1
        for key, value in count_dict.items():
            if value == min(count_dict.values()):
                return key


def count_punctuation_chars(file_path: str) -> int:
    counter = 0
    with open(file_path, "r") as f:
        for line in f:
            for char in line.encode().decode("unicode-escape").strip():
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


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, "r") as f:
        counter = 0
        for line in f:
            for char in line.encode().decode("unicode-escape"):
                if ord(char) > 128:
                    counter += 1
        return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, "r") as f:
        count_dict = {}
        for line in f:
            for char in line.encode().decode("unicode-escape").strip():
                if ord(char) > 128:
                    if char not in count_dict.keys():
                        count_dict[char] = 1
                    else:
                        count_dict[char] += 1
        for key, value in count_dict.items():
            if value == max(count_dict.values()):
                return key
