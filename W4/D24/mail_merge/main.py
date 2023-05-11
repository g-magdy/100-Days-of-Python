# with open("./input/names/invitees.txt",mode="w") as file:
#     file.write("Aang\nZuko\nAppa\nKatara\nSokka\nMomo\nUncle Iroh\nToph")

'''
for name in names:
    Read the name form the file invitees.txt -> currName
    Create a new file with the name <- currName
'''
PLACEHOLDER = "[Name]"

template = ""
with open("./input/letters/starting_letters.txt", mode="r") as letter:
    template = letter.read()

invitees_names = []
with open("./input/names/invitees.txt", mode="r") as file:
    invitees_names = file.readlines()

for person in invitees_names:
    person = person.strip()
    s = "msg_for_"+person
    with open(f"./output/final/{s}.txt", mode="w") as file:
        currentMsg = template
        currentMsg = currentMsg.replace(PLACEHOLDER, person)
        file.write(currentMsg)