import csv
import math

pos = 4
neg = 0

def stop_word(wstr):
    w = wstr.strip()
    if not w or w[0] == '@' or w[0] == '.' or w[0] == '-':
        return True
    return False


def read_dir(dirn):
    cont_l = []
    s = []
    with open(dirn, encoding='latin-1') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for word in row[3].strip().split(" "):
                if not stop_word(word):
                    s.append(word)
            b = [row[0], row[1], row[2],  s]
            cont_l.append(b)
            s = []
    return cont_l


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


def calculate_neg_pos(word, n_words, neg_neg_word, alpha):
    if word in n_words:
        occurrence = n_words[word]
    else:
        occurrence = 0
    return (occurrence + 1) / (neg_neg_word + alpha)


def calculate_pos_pos(word, n_words, neg_pos_word, alpha):
    if word not in n_words:
        occurrence = 0
    else:
        occurrence = n_words[word]
    return (occurrence + 1) / (neg_pos_word + alpha)


def get_pos_neg_words(tweets: list, user_tw: dict):
    pos_list = neg_list = []
    for tweet in tweets:
        if tweet[2] not in user_tw:
            user_tw[tweet[2]] = []
        if tweet[0] == neg:
            neg_list += tweet[3]
        elif tweet[0] == pos:
            pos_list += tweet[3]
        user_tw[tweet[2]].append(tweet)


def get_transition_prob(user_tweets: dict, transition: dict):
    prev_state = None
    for u, tweets in user_tweets.items():
        tweets.sort(key=lambda t: tweets[2])
        for tweet in tweets[3]:
            if prev_state is not None:
                transition[prev_state][tweet[2]] +=1
            prev_state = tweet[0]
    switch_trans_with_prob()


def switch_trans_with_prob(transition: dict):
    for prev_state, val in transition.items():
        sum = 0.0
        for value in val.values():
            sum += value
        for next_state, num in val.items():
            transition[prev_state][next_state] = num / sum


def forward():
    # pos = (pos -> pos, pos -> neg)
    # neg = (neg -> pos, neg -> neg)
    # new_pos = pos[0] * prev_pos + neg[0] * prev_neg
    # new_neg = pos[1] * prev_pos + neg[1] * prev_neg
    # return new_pos, new_neg
    pass

if __name__ == '__main__':
    tweet_list = read_dir('users_5000.csv')

    user_tw = {}

    transition = {pos: {pos: 0, neg: 0}, neg: {pos: 0, neg: 0}}
    pos_words = create_dict_from_list(tweet_list[3])
    neg_words = create_dict_from_list(tweet_list[3])
    all_words = list(pos_words.keys()) + list(neg_words.keys())
    a = len(set(all_words))




