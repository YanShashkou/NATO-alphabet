
import pandas

data=pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def translate(word):
    word_list = list(word.upper())
    new_list=[alphabet_dict[letter] for letter in word_list]
    print(new_list)

translate('Hello')
