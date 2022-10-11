import re
import matplotlib.pyplot as plt
import numpy as np


class WordInfo(object):
    def __init__(self, number_of_occurrences, rank):
        self.number_of_occurrences = number_of_occurrences
        self.rank = rank

    number_of_occurrences: int
    rank: int

    def __repr__(self):
        return f'(number of occurrences: {self.number_of_occurrences}, rank: {self.rank})'


def text_stats(text):
    res = re.findall(r'[a-zA-Z0-9_\(\)\|]+', text)
    words_occurrences = dict()
    all_words = len(res)
    for word_ in res:
        if word_ in words_occurrences:
            words_occurrences[word_] = words_occurrences[word_] + 1
        else:
            words_occurrences[word_] = 1

    return {k: v for k, v in sorted(words_occurrences.items(), key=lambda item: item[1], reverse=True)}, all_words


def zipfs_law(fileName):
    with open(fileName, 'r') as file:
        data = file.read().replace('\n', ' ')

    stats, all_words = text_stats(data)

    print(stats)

    sorted_words = list(stats.keys())

    result = dict()

    rank = 1
    result[sorted_words[0]] = WordInfo(stats[sorted_words[0]], rank)
    for i in range(1, len(sorted_words)):
        if result[sorted_words[i - 1]].number_of_occurrences != stats[sorted_words[i]]:
            rank += 1
        result[sorted_words[i]] = WordInfo(stats[sorted_words[i]], rank)

    x = list()
    y = list()

    for k in result:
        x.append(result[k].rank)
        y.append(result[k].number_of_occurrences)
        print(
            f'{result[k].number_of_occurrences}, {all_words}, {result[k].rank}, {result[k].number_of_occurrences / all_words * result[k].rank * 100}')

    plt.scatter(x, y)
    plt.xlim(0, 150)
    plt.ylim(0, 150)
    plt.gca().set_aspect('equal', adjustable='box')


zipfs_law('../../resources/voynich.txt')

zipfs_law('../../resources/spanish_wiki.txt')

plt.show()
