def fill_word_weight_list(list_of_words, dict_of_chars_count):
    """Since we counted the number of repetitions of chars,
    and we have a list of all words, we will replace each char
     in the word with its number of repetitions, which represented
      its uniqueness, and then add these values and get the weight
       of the word, the less it is, the more unique the word"""
    words_weight = []
    summ = 0
    for i in list_of_words:
        for j in i:
            summ += dict_of_chars_count[j]
        words_weight.append(summ)
        summ = 0
    return words_weight
