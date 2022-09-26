import pandas
import csv
# user = input("What is your name?": )
user = "Vijit"
user_list = [alpha for alpha in user]
print(user_list)

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# data_dict = {letter:code for data.letter}
with open('nato_phonetic_alphabet.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]:rows[1] for rows in reader}

output = []