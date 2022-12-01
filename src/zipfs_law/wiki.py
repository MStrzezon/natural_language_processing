from read_utils import *
from zipfs_law import *

with open('../../resources/solar_system.txt', 'r') as file:
    txt = file.read()

words = getWordsFromWiki(txt)
words_occurrences, number_of_words = text_stats(words)
df = pandas_text_stats(words_occurrences, number_of_words)
print('Start creating zipf table...')
create_zipf_table(df, 'solar_system')
print('Zipf table is saved')
print('Start plotting rxf...')
plot_rxf(df, 'solar_system')
print('Plotting rxf is finished')
print('Start plotting bar plot...')
plot_bar(df, 'solar_system')
print('Plotting bar plot is finished')
# printing result
