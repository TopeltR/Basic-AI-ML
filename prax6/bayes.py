import os
import numpy as np


def get_total_messages(ham_list: list, spam_list: list):
    return len(ham_list) + len(spam_list)


def get_total_words_count(words_dict: dict) -> int:
    count = 0
    for x in words_dict.values():
        count += x
    return count


def create_dict_from_list(words_list) -> dict:
    unique_dict = {}
    for word in words_list:
        for w in word:
            if w not in unique_dict:
                unique_dict[w] = 1
            else:
                value = unique_dict.get(w)
                value += 1
                unique_dict[w] = value
    return unique_dict


def stop_word(wstr):
    w = wstr.strip()
    if len(w) < 4:
        return True
    return False


def read_dir(dirn):
    cont_l = []
    for fn in os.listdir(dirn):
        with open(os.path.join(dirn, fn), encoding="latin-1") as f:
            words = [w.strip() for w in f.read().replace("\n", " ").split(" ") if not stop_word(w)]
            cont_l.append(words)
    return cont_l


def get_unique_words(dct_spam, dct_ham) -> set:
    v = set(dct_spam.keys())
    v.update(dct_ham.keys())
    return v


def filter_letter(letter, ham_d: dict, spam_d: dict):
    letter_s = create_set_from_letter(letter)
    for word in letter_s.copy():
        if word not in ham_d.keys():
            letter_s.remove(word)
    for word in letter_s.copy():
        if word not in spam_d.keys():
            letter_s.remove(word)
    return letter_s


def create_set_from_letter(letter) -> set:
    letter_s = set()
    for line in letter:
        for word in line:
            letter_s.add(word)
    return letter_s


def calculate_word_probability(occurrence: int, total_words_count: int, unique_words_count: int) -> float:
    return (occurrence + 1) / (total_words_count + unique_words_count)


def is_letter_spam(ham_l, spam_l, letter) -> bool:
    h_ham = 0.0
    h_spam = 0.0
    total = get_total_messages(ham_l, spam_l)

    h_ham += len(ham_l) / total
    h_spam += len(spam_l) / total

    dct_ham = create_dict_from_list(ham_l)
    dct_spam = create_dict_from_list(spam_l)
    letter_s = filter_letter(letter, dct_ham, dct_spam)
    unique_words = len(get_unique_words(dct_ham, dct_spam))

    h_ham, h_spam = calculate_letter_probability(dct_ham, dct_spam, h_ham, h_spam, letter_s, unique_words)

    if h_spam < h_ham:
        return False
    else:
        return True


def calculate_letter_probability(dct_ham, dct_spam, h_ham, h_spam, letter_s, unique_words):
    for word in letter_s:
        if word in dct_spam.keys():
            h_spam += np.log(
                calculate_word_probability(dct_spam.get(word), get_total_words_count(dct_spam), unique_words))
    for word in letter_s:
        if word in dct_ham.keys():
            h_ham += np.log(
                calculate_word_probability(dct_ham.get(word), get_total_words_count(dct_ham), unique_words))
    return h_ham, h_spam


def main():
    spam_l = read_dir("spam")
    ham_l = read_dir("ham")
    letter_1 = read_dir("letters")
    letter_2 = read_dir("letters_1")

    print(is_letter_spam(ham_l, spam_l, letter_1))
    print(is_letter_spam(ham_l, spam_l, letter_2))


main()
