'''file = open("my_file.txt")
content = file.read()
print(content)
file.close() # to free up the resources'''
# better way :
# with open("../../../../Users/George Magdy/OneDrive - Cairo University - Students/Desktop/temp.txt") as file:
with open("../../../../temp.txt") as file:
    a = file.read()
    print(a)
print("emojis don't work in files 😢")