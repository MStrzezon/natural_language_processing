from read_utils import *
from zipfs_law import *


def main():
    with open('../../resources/voynich.txt', 'r') as file:
        txt = file.read().replace('\n', '')

    words = getWordsFromVoinich(txt)
    words_occurrences, number_of_words = text_stats(words)
    df = pandas_text_stats(words_occurrences, number_of_words)
    print('Start creating zipf table...')
    create_zipf_table(df)
    print('Zipf table is saved')
    print('Start plotting rxf...')
    plot_rxf(df)
    print('Plotting rxf is finished')
    print('Start plotting bar plot...')
    plot_bar(df)
    print('Plotting bar plot is finished')


if __name__ == "__main__":
    main()
