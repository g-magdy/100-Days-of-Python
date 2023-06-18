import pandas

#read csv into a dataframe
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# create a dict from dataframe rows using comprehension    
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

#prompt for input
word = input("Enter a word : ")

#create a list containing the phonetic sound of each letter
nato_list = [nato_dict[letter.upper()] for letter in word]

print(nato_list)