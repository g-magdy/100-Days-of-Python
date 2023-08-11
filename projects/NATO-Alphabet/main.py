import pandas

#read csv into a dataframe
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# create a dict from dataframe rows using comprehension    
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

#prompt for input and validate it
while True:
    word = input("Enter a word : ")
    if word.isalpha():
        break
    else:
        print("Only alphabetic letters are allowed")

#create a list containing the phonetic sound of each letter
nato_list = [nato_dict[letter.upper()] for letter in word]

print(nato_list)