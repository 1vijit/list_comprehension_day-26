import pandas
import csv
user = input("What is your name? :").upper()
user_list = [alpha for alpha in user]
# print(user_list)

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows() }
print(phonetic_dict)

for letter in user:
    phone = phonetic_dict[letter]
    print(f"{letter} : {phone}")