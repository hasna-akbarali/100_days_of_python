import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

def natoalphabet():

    inp = input('Enter a word: ').upper()
    try:
        csv_dict = {row['letter']: row['code'] for (index, row) in data.iterrows()}
        nato_dict = [csv_dict[letter] for letter in inp]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
    else:
        print(nato_dict)

while True:
    natoalphabet()

# with open('file1.txt', 'r') as f1:
#     file1 = f1.readlines()
#     file1 = [i.strip() for i in file1]
# with open('file2.txt', 'r') as f2:
#     file2 = f1.readlines()
#     file2 = [i.strip() for i in file2]
#
# common = [int(i) for i in file1 if i in file2]
# print(common)
#
# sentance = 'What is the Airspeed Velocity of an Unladen Swallow?'
# words = sentance.split(' ')
# result = {word:len(word) for word in words}
# print(result)
