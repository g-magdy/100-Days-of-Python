# A simple way to generate multiple letters from a single template
# To multiple persons, given the original letter with a placholder [Name]
# and a list (in a separate file) of names
# 15 07 23
# the output files will be saved in ./output/ready-to-send

PLACEHOLDER = "[Name]"

# 3 important functions : readlines(), strip(), and replace()

# read the template letter in a string
with open("./input/letters/starting-letter.txt") as letter:
    original_message = letter.read()
    
# read the names and puth them in a list
with open("./input/names/invited-names.txt") as names_file:
    lines = names_file.readlines()
    people = []
    for line in lines:
        # remove the white space or \n from the line
        people.append(line.strip())

for person in people:
    heading = f"letter-to-{person}.txt"
    tailored_message = original_message.replace(PLACEHOLDER , person)
    with open("./output/ready-to-send/"+heading, mode='w') as letter:
        letter.write(tailored_message)
