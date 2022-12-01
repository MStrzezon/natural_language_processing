import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class WordInfo(object):
    def __init__(self, number_of_occurrences, rank):
        self.number_of_occurrences = number_of_occurrences
        self.rank = rank

    number_of_occurrences: int
    rank: int

    def __repr__(self):
        return f'(number of occurrences: {self.number_of_occurrences}, rank: {self.rank})'


def text_stats(words):
    words_occurrences = dict()
    number_of_words = len(words)
    for word_index in range(number_of_words):
        word = words[word_index]
        if words[word_index] in words_occurrences:
            words_occurrences[word] = words_occurrences[word] + 1
        else:
            words_occurrences[word] = 1

    return {k: v for k, v in sorted(words_occurrences.items(), key=lambda item: item[1], reverse=True)}, number_of_words


def convert_map_to_word_info_map(words_map):
    sorted_words = list(words_map.keys())
    result = dict()
    rank = 1
    result[sorted_words[0]] = WordInfo(words_map[sorted_words[0]], rank)
    for i in range(1, len(sorted_words)):
        if result[sorted_words[i - 1]].number_of_occurrences != words_map[sorted_words[i]]:
            rank += 1
        result[sorted_words[i]] = WordInfo(words_map[sorted_words[i]], rank)

    return result


def create_array_from_map(words_info_map, number_of_all_words):
    data = list()
    for word in words_info_map:
        word_info = words_info_map[word]
        row = [word, word_info.number_of_occurrences, word_info.rank, word_info.number_of_occurrences /
               number_of_all_words * 100, word_info.rank * (word_info.number_of_occurrences /
                                                            number_of_all_words * 100)]
        data.append(row)

    return data


def pandas_text_stats(words_map, number_of_all_words):
    words_info_map = convert_map_to_word_info_map(words_map)
    array_from_map = create_array_from_map(words_info_map, number_of_all_words)

    return pd.DataFrame(array_from_map, columns=['word', 'number_of_occurrences', 'rank', 'frequency', 'rxf'])


def create_zipf_table(pandas_map: pd.DataFrame, text_name):
    file_name = '../../resources/' + text_name + '_table.csv'
    pandas_map.to_csv(file_name, index=False)


def plot_bar(df, text_name):
    df = df.head(50)
    word_info = df['word'] + ',' + df['number_of_occurrences'].astype(str) + ',' + df['rank'].astype(str) \
                + ',' + df['frequency'].astype(str)
    word_info = word_info.head(50)
    word_frequency = df['rxf']

    n = df.shape[0]

    fig, ax = plt.subplots(figsize=(10, n // 10))

    plt.yticks(fontsize=4)

    ax.barh(word_info, word_frequency, align='center', color='green', ecolor='black')
    ax.set_yticks(word_info)
    ax.set_yticklabels([str(x) for x in word_info])
    ax.set_xlabel('r x f')
    ax.set_ylim(0, n)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    file_name = '../../resources/bar50_' + text_name + '.png'

    plt.savefig(file_name, dpi=150)


def plot_rxf(df, text_name):
    df_without_duplicates = df.drop_duplicates(subset=['rank'], keep='first')
    r = np.log10(df_without_duplicates['rank'])
    f = np.log10(df_without_duplicates['frequency'])

    plt.scatter(r, f)
    plt.xlabel('log(rank)')
    plt.ylabel('log(frequency)')
    plt.title('r x f')

    file_name = '../../resources/rxf_' + text_name + '.png'

    plt.savefig(file_name, dpi=150)
